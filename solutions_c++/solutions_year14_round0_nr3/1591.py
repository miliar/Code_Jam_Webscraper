#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <sstream>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <cstdlib>
#include <cstdio>
#include <iterator>
#include <functional>
#include <bitset>
#include <iostream>
#include <iomanip>

using namespace std;

#define INF (1<<29)
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#define TIMESTAMP(x) eprintf("["#x"] Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)

bool b[55][55];
int dx[] = {-1,-1,-1,0,0,1,1,1};
int dy[] = {-1,0,1,-1,1,-1,0,1};

void print(int R, int C, vector<int>& qx, vector<int> & qy) {
	set<pair<int, int> > s;
	for(unsigned i = 0; i < qx.size(); ++i)
		s.insert(make_pair(qx[i], qy[i]));
	for(int i = 0; i < R; ++i) {
		for(int j = 0; j < C; ++j) {
			if(i == qx[0] && j == qy[0])
				cout << "c";
			else{
				if(s.find(make_pair(i, j)) != s.end())
					cout << ".";
				else
					cout << "*";
			}
		}
		if(i != R-1)
			cout << endl;
	}		
}

bool search(int x, int y, vector<int>& qx, vector<int>& qy, int R, int C, int M) {
	unsigned empty = R * C - M;
	int put = 0;
	
	if(qx.size() == empty){
		print(R, C, qx, qy);
		return true;
	}
	
	if(qx.size() > empty) {
		return false;
	}
	
	for(int i = 0; i < 8; ++i)	
		if(x+dx[i]<R && x+dx[i] >= 0 && y+dy[i] >= 0 && y+dy[i] < C && !b[x+dx[i]][y+dy[i]])
			b[x+dx[i]][y+dy[i]] = 1, qx.push_back(x+dx[i]), qy.push_back(y+dy[i]), ++put;
	
	if(put == 0)
		return false;
	
	if(qx.size() > empty) {
		for(int i = 0; i < put; ++i)
			b[qx.back()][qy.back()] = 0, qx.pop_back(), qy.pop_back();
		return false;
	}
	if(qx.size() == empty){
		print(R, C, qx, qy);
		for(int i = 0; i < put; ++i)
			b[qx.back()][qy.back()] = 0, qx.pop_back(), qy.pop_back();
		return true;
	}
	else {
		unsigned sz = qx.size();
		for(unsigned i = 0; i < sz; ++i) {
			if(search(qx[i], qy[i], qx, qy, R, C, M) == true) {		
				for(int i = 0; i < put; ++i)
					b[qx.back()][qy.back()] = 0, qx.pop_back(), qy.pop_back();
				return true;
			}
		}
	}
	
	for(int i = 0; i < put; ++i)
		b[qx.back()][qy.back()] = 0, qx.pop_back(), qy.pop_back();
	
	return false;
}

bool test(int x, int y, int R, int C, int M) {
	memset(b, false, sizeof(b));
	vector<int> qx, qy;
	qx.push_back(x), qy.push_back(y);
	b[x][y] = 1;
	return search(x, y, qx, qy, R, C, M);
}

void solve(int R, int C, int M) {
	for(int i = 0; i < R; ++i)
		for(int j = 0; j < C; ++j)
			if(test(i, j, R, C, M))
				return;
	cout << "Impossible";
}

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		int R, C, M;
		cin >> R >> C >> M;
		cout << "Case #" << t << ": " << endl;
		solve(R, C, M);
		cout << endl;
	}
	return 0;
}
