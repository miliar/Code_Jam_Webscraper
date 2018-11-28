#include <cstdio>
#include <cassert>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>
using namespace std;

bool cmp(const pair<int, char> &p1, const pair<int, char> &p2) {
	return p1.first > p2.first;
}

pair<int, int> next(vector<pair<int, char> > &P, int N) {
	int peak = P[0].first, len = 1, valley = 0;
	for(int i = 1; i < N; i++) {
		if(P[i].first < peak) {
			valley = P[i].first;
			break;
		}
		len++;
	}
	return make_pair(valley, len);
}

void fill(pair<int, int> &c, vector<pair<int, char> > &P, string &f) {
	int loops = P[0].first - c.first;
	for(int i = 0; i < loops; i++) {
		if(c.second%2 == 1) {
			f += ' ';
			f += P[c.second - 1].second;
			P[c.second - 1].first--;			
		}
		for(int start = 0; (start + 1) < c.second; start += 2) {
			f += ' ';
			f += P[start].second;
			f += P[start+1].second;	
			P[start].first--; P[start+1].first--;		
		}		
	}
}

int main() {
	int T, N;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++) {
		scanf("%d", &N);
		//N > 2
		vector<pair<int, char> > P;
		int temp;
		for(int i = 0; i < N; i++) {
			scanf("%d", &temp);
			P.push_back(make_pair(temp, 'A' + i));
		}
		sort(P.begin(), P.end(), cmp);
		pair<int, int> check = next(P, N);
		string ret = "";
		while(check.first != 0) {
			fill(check, P, ret);
			check = next(P, N);
		}
		fill(check, P, ret);
		printf("Case #%d:%s\n", t, ret.c_str());
	}	
	return 0;
}