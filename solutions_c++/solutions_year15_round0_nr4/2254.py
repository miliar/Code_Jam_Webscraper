/*
 * $File: solve.cc
 * $Date: Sun Apr 12 01:10:06 2015 +0800
 * $Author: Xinyu Zhou <zxytim[at]gmail[dot]com>
 */


#include <limits>
#include <cassert>
#include <cstdio>
#include <unordered_map>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

typedef std::pair<int, int> Position;
struct Patch {
	std::vector<Position> pos;

	inline bool operator < (const Patch &patch) const {
		return pos < patch.pos;
	}
	inline bool operator == (const Patch &patch) const {
		return pos == patch.pos;
	}

	bool has_position(const Position &p) {
		for (auto &q: pos)
			if (q.first == p.first && q.second == p.second)
				return true;
		return false;
	}

	Patch &standarize_self() {
		std::sort(pos.begin(), pos.end());
		int min_x = std::numeric_limits<int>::max(),
			min_y = std::numeric_limits<int>::max();
		for (auto &p: pos) {
			if (p.first < min_x)
				min_x = p.first;
			if (p.second < min_y)
				min_y = p.second;
		}
		for (auto &p: pos) {
			p.first -= min_x;
			p.second -= min_y;
		}
		return *this;
	}

	int rows() const {
		int r = -1;
		for (auto &p: pos)
			r = std::max(r, p.first);
		return r + 1;
	}

	int cols() const {
		int c = -1;
		for (auto &p: pos)
			c = std::max(c, p.second);
		return c + 1;
	}

	Patch rotate90() const {
		Patch ret;
		int r = rows();
		for (auto &p: pos)
			ret.pos.emplace_back(p.second, r - p.first);
		ret.standarize_self();
		return ret;
	}

	Patch flip(int axis) const {
		assert(axis == 0 || axis == 1);
		Patch ret;
		if (axis == 0) {
			int r = rows();
			for (auto &p: pos)
				ret.pos.emplace_back(r - p.first, p.second);
		} else {
			int c = cols();
			for (auto &p: pos)
				ret.pos.emplace_back(p.first, c - p.second);
		}
		ret.standarize_self();
		return ret;
	}

	std::vector<Patch> all_possible_variations() const {
		std::vector<Patch> ret;
		auto tmp = *this;

		auto patch_exists = [&](const Patch &patch) {
			for (auto &p: ret)
				if (p == patch)
					return true;
			return false;
		};
		for (int i = 0; i < 4; i ++) {
			for (auto &p: {tmp, tmp.flip(0), tmp.flip(1)})
				if (!patch_exists(p))
					ret.emplace_back(p);
			tmp = tmp.rotate90();
		}
		return ret;
	}

	Patch translate(const Position &p) const {
		Patch ret = *this;
		for (auto &q: ret.pos)
			q.first += p.first, q.second += p.second;
		return ret;
	}

	Patch translate(int x, int y) const {
		return translate(std::make_pair(x, y));
	}

};

void print_hash(const std::vector<bool> &hash, int n, int m) {
	for (int i = 0; i < n; i ++) {
		for (int j = 0; j < m; j ++)
			printf("%c", hash[i * m + j] ? 'x' : '.');
		printf("\n");
	}
}

void print_patch(const Patch &patch) {
	int r = patch.rows(),
		c = patch.cols();
	std::vector<bool> hash(r * c, false);
	for (auto &p: patch.pos)
		hash[p.first * c + p.second] = 1;
	print_hash(hash, r, c);
}

void print_patches(const std::vector<Patch> &patches) {
	int idx = 0;
	for (auto &patch: patches) {
		idx += 1;
		printf("print %d/%d patches:\n", idx, (int)patches.size());
		print_patch(patch);
		printf("----------\n");
	}
}


bool patch_hash_lookup(const std::set<Patch> &patch_hash,
		const Patch &cur_patch) {
	auto tmp = cur_patch;

	for (int i = 0; i < 4; i ++) {
		if (patch_hash.count(tmp))
			return true;
		if (patch_hash.count(tmp.flip(0)))
			return true;
		if (patch_hash.count(tmp.flip(1)))
			return true;
		tmp = tmp.rotate90();
	}
	return false;
}

void do_generate_k_patches(
		std::vector<std::set<Patch>> &patch_hash,
		std::vector<Patch> &patches,
		Patch &cur_patch,
		int nr_remain) {
	auto &cur_hash = patch_hash[nr_remain];

	if (patch_hash_lookup(cur_hash, cur_patch))
		return;
	cur_hash.insert(cur_patch);
	if (nr_remain == 0) {
		patches.emplace_back(cur_patch);
		return;
	}
	static const std::vector<std::pair<int, int>> dir{
		{0, 1}, {0, -1}, {1, 0}, {-1, 0}
	};

	int r = cur_patch.rows(),
		c = cur_patch.cols();
	std::vector<bool> hash(r * c, false);
	for (auto &p: cur_patch.pos)
		hash[p.first * c + p.second] = 1;

	for (auto &p: cur_patch.pos) {
		for (auto &d: dir) {
			auto new_p = std::make_pair(
					p.first + d.first,
					p.second + d.second);
			if (new_p.first >= 0 && new_p.first < r
					&& new_p.second >= 0 && new_p.second < c
					&& hash[new_p.first * c + new_p.second])
				continue;
			auto next_patch = cur_patch;
			next_patch.pos.emplace_back(new_p);
			next_patch.standarize_self();
			do_generate_k_patches(patch_hash, patches, next_patch, nr_remain - 1);
		}
	}
}

std::vector<Patch> generate_k_patches(int k) {
	std::vector<Patch> patches;
	std::vector<std::set<Patch>> patch_hash(k + 1);

	// XXX
	patch_hash[0].size();
	Patch().all_possible_variations();
	print_patch(Patch());
	print_patches(patches);

	Patch cur_patch;
	cur_patch.pos.emplace_back(0, 0);

	do_generate_k_patches(patch_hash, patches, cur_patch, k - 1);

	return patches;
}

bool fill(std::vector<bool> &hash, int n, int m, Patch &patch) {
	for (auto &p: patch.pos) {
		if (p.first < 0 || p.first >= n || p.second < 0 || p.second >= m)
			return false;
		if (hash[p.first * m + p.second])
			return false;
	}
	for (auto &p: patch.pos)
		hash[p.first * m + p.second] = 1;
	return true;
}

void clear(std::vector<bool> &hash, int n, int m, Patch &patch) {
	for (auto &p: patch.pos)
		hash[p.first * m + p.second] = 0;
}


size_t nr_ones(const std::vector<bool> &hash) {
	size_t ret = 0;
	for (size_t i = 0; i < hash.size(); i ++)
		ret += hash[i];
	return ret;
}

bool can_fill_all(std::vector<bool> &hash,
		std::set<std::vector<bool>> &hash_set,
		int n, int m, std::vector<Patch> &all_patch_pool) {
	if (nr_ones(hash) == hash.size())
		return true;
	if (hash_set.count(hash))
		return false;
	hash_set.insert(hash);
	for (auto &patch: all_patch_pool) {
		int r = patch.rows(),
			c = patch.cols();

		for (int i = 0; i + r <= n; i ++)
			for (int j = 0; j + c <= m; j ++) {
				auto cur_patch = patch.translate(i, j);
				if (fill(hash, n, m, cur_patch)) {
					if (can_fill_all(hash, hash_set, n, m, all_patch_pool))
						return true;
					clear(hash, n, m, cur_patch);
				}
			}
	}
	return false;
}

bool solve(int k, int n, int m) {
	auto k_patches = generate_k_patches(k);

	std::vector<Patch> patch_pool;
	for (auto &patch: k_patches)
		for (auto &v: patch.all_possible_variations())
			patch_pool.emplace_back(v);

	std::vector<Patch> all_patch_pool;
	for (auto &patch: patch_pool) {
		int r = patch.rows(),
			c = patch.cols();

		for (int i = 0; i + r <= n; i ++)
			for (int j = 0; j + c <= m; j ++) {
				auto cur_patch = patch.translate(i, j);
				all_patch_pool.emplace_back(cur_patch);
			}
	}

	std::set<std::vector<bool>> hash_set;
	for (auto &kp: k_patches) {
		bool succeed = false;

		for (auto &patch: kp.all_possible_variations()) {
			int r = patch.rows(),
				c = patch.cols();

			for (int i = 0; i + r <= n && !succeed; i ++)
				for (int j = 0; j + c <= m && !succeed; j ++) {
					auto cur_patch = patch.translate(i, j);
					std::vector<bool> hash(n * m, 0);
					fill(hash, n, m, cur_patch);
					if (can_fill_all(hash, hash_set, n, m, all_patch_pool))
						succeed = true;
				}
		}
		if (!succeed)
			return false;
	}

	return true;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int case_id = 1; case_id <= T; case_id ++) {
		int X, R, C;
		scanf("%d%d%d", &X, &R, &C);
		printf("Case #%d: %s\n", case_id, solve(X, R, C) ? "GABRIEL" : "RICHARD");
		fflush(stdout);
	}
	return 0;
}


/*
 * vim: syntax=cpp11.doxygen foldmethod=marker foldmarker=f{{{,f}}}
 */
