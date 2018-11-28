#include <bits/stdc++.h>

using namespace std;

tuple<vector<map<char,int>>,vector<int>, vector<vector<int>>>
 build_table(vector<string> const& patterns) {
	vector<map<char,int>> follow;
	vector<vector<int>> match;
	
	follow.push_back(map<char,int>());
	match.push_back(vector<int>());
	
	for (unsigned i=0; i<patterns.size(); i++) {
		int cur = 0;
		for (auto c : patterns[i]) {
			if (follow[cur].count(c) != 0) {
				cur = follow[cur][c];
			} else {
				follow[cur][c] = follow.size();
				cur = follow.size();
				follow.push_back(map<char,int>());
				match.push_back(vector<int>());
			}
		}
		match[cur].push_back(i);
	}
	
	vector<int> fail(follow.size(), -1);
	queue<pair<int, char>> work;
	for (auto kv : follow[0]) { work.push({0, kv.first}); }
	while (!work.empty()) {
		auto curfull = work.front();
		int cur = curfull.first;
		char followChar = curfull.second;
		work.pop();
		for (auto kv : follow[follow[cur][followChar]]) { 
			work.push({follow[cur][followChar], kv.first});
		}
		int curf = fail[cur];
		while (curf != -1) {
			if (follow[curf].count(followChar) == 0) { curf = fail[curf]; }
			else { curf = follow[curf][followChar]; break; }
		}
		if (curf == -1) { curf = 0; }
		fail[follow[cur][followChar]] = curf;
		if (curf != 0) {
			match[follow[cur][followChar]].insert(match[follow[cur][followChar]].end(),
				match[curf].begin(), match[curf].end());
		}
	}
	
	return make_tuple(follow, fail, match);
}

// cb has last char of match, index of matched word as args.
template<class F>
void match_table(string const& s, tuple<vector<map<char,int>>,vector<int>,
  vector<vector<int>>> const& table, F&& cb) {
	auto const& follow = get<0>(table);
	auto const& fail = get<1>(table);
	auto const& match = get<2>(table);
	
	int state = 0;
	for (unsigned i=0; i<s.size(); i++) {
		auto it = follow[state].find(s[i]);
		if (it == follow[state].end()) {
			if (state != 0) { state = fail[state]; i--; }
		} else {
			state = it->second;
			for (auto m : match[state])	{ cb(i, m); }
		}
	}
}

const int iter = 20000;

int getCount(int i, vector<vector<int>> const & enable, vector<int> &count) {
	if (count[i] == -1) {
		count[i] = 1;
		for (auto e : enable[i]) count[i] += getCount(e, enable, count);
	}
	return count[i];
}

void genOrder(int i, vector<int> &pos, int low, int high, vector<int> &order, vector<vector<int>> const & enable, vector<int> const & encount) {
	if (high - low == 1) {
		order[pos[low]] = i;
		return;
	}
	
	int lowest = 101;
	int lowesti = -1;
	for (int i=low; i<high; i++) {
		if (pos[i] < lowest) {
			lowest = pos[i];
			lowesti = i;
		}
	}
	
	swap(pos[low], pos[lowesti]);
	
	order[pos[low]] = i;
	low++;
	
	//if (enable[i].size() != 1) random_shuffle(pos.begin()+low, pos.begin()+high);
	
	for (auto e : enable[i]) {
		genOrder(e, pos, low, low + encount[e], order, enable, encount);
		low += encount[e];
	}
}

void doCase(int t) {
	int N;
	cin >> N;
	
	vector<int> prereq(N);
	vector<vector<int>> enable(N);
	vector<int> encount(N, -1);
	
	for (int i=0; i<N; i++) 
		cin >> prereq[i];
		
	for (int i=0; i<N; i++) {
		if (prereq[i] != 0) enable[prereq[i]-1].push_back(i);
	}
	
	for (int i=0; i<N; i++) getCount(i, enable, encount);
	
	vector<char> charmap(N);
	
	for (int i=0; i<N; i++) {
		cin >> charmap[i];
	}
	
	int M;
	cin >> M;
	
	vector<string> cool(M);
	
	for (int i=0; i<M; i++) cin >> cool[i];
	
	auto find_table = build_table(cool);
	map<string,int> scount;
	
	vector<int> occount(M,0);
	for (int i=0; i<iter; i++) {
		vector<int> order(N);
		vector<int> pos(N);
		for (int i=0; i<N; i++) pos[i] = i;
		random_shuffle(pos.begin(), pos.end());
		
		int used = 0;
		for (int i=0; i<N; i++) {
			if (prereq[i] != 0) continue;
			genOrder(i, pos, used, used+encount[i], order, enable, encount);
			used += encount[i];
		}
		
		string res(N, ' ');
		for (int i=0; i<N; i++) res[i] = charmap[order[i]];
		//scount[res]++;
		vector<bool> seen(M, false);
		
		match_table(res, find_table, [&](int i, int m) { seen[m] = true; });
		
		for (int i=0; i<M; i++) if (seen[i]) occount[i]++;
	}
	
	/*for (auto kv : scount) {
		cerr << kv.first << ": " << double(kv.second)/double(iter) << endl;
	}*/
	cerr << t << endl;
	cout << "Case #" << t << ":";
	
	for (int i=0; i<M; i++) cout << " " << fixed << setprecision(2) << double(occount[i])/double(iter);
	cout << endl;
}

int main() {
	int T;
	cin>> T;
	for (int i=1; i<=T; i++) doCase(i);
	return 0;
}
