#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

struct Block {
	double mass;
	char owner;
	bool used = false;
	bool operator<(const Block& other) const {
		return mass < other.mass;
	}
};

int playDeceit(vector<Block>& blocks) {
	auto forward = blocks.begin();
	auto backward = blocks.rbegin();
	int score = 0;
	while(backward != blocks.rend()) {
		if(backward->owner == 'n') {
			auto ken = backward;
			while(ken->used || ken->owner == 'n') {
				++ken;
			}
			backward++->used = true;
			ken->used = true;
			++score;
		} else {
			while(forward->used || forward->owner == 'k') {
				++forward;
			}
			forward++->used = true;
			backward++->used = true;
		}
		while(backward != blocks.rend() && backward->used) {
			++backward;
		}
	}
	return score;
}

int playWar(vector<Block>& naomi, vector<Block>& ken) {
	auto next = naomi.begin(), light = ken.begin(), heavy = ken.begin();
	int score = 0;
	while(next != naomi.end()) {
		while(heavy != ken.end() && heavy->mass < next->mass) {
			++heavy;
		}
		if(heavy == ken.end()) {
			while(light->used) {
				++light;
			}
			light++->used = true;
			++score;
		} else {
			heavy++->used = true;
		}
		next++->used = true;
	}
	return score;
}

int main() {
	int tests, blocks;
	cin >> tests;
	for(int test = 1; test <= tests; ++test) {
		cin >> blocks;
		vector<Block> naomi(blocks), ken(blocks);
		for(auto& block : naomi) {
			cin >> block.mass;
			block.owner = 'n';
		}
		sort(naomi.begin(), naomi.end());
		for(auto& block : ken) {
			cin >> block.mass;
			block.owner = 'k';
		}
		sort(ken.begin(), ken.end());
		auto naomiNext = naomi.begin(), kenNext = ken.begin();
		vector<Block> all(blocks * 2);
		for(auto& block : all) {
			if(naomiNext == naomi.end()) {
				block = *kenNext++;
			} else if(kenNext == ken.end()) {
				block = *naomiNext++;
			} else if(*naomiNext < *kenNext) {
				block = *naomiNext++;
			} else {
				block = *kenNext++;
			}
		}
		cout << "Case #" << test << ": " << playDeceit(all) << ' ' << playWar(naomi, ken) << '\n';
	}
	return 0;
}
