#include <iostream>
#include <cassert>
#include <fstream>
#include <sstream>
#include <math.h>
#include <memory>
#include <string>
#include <vector>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <time.h>
#include <stdio.h>
#include <direct.h>
#include <windows.h>
#include <mutex>
#include <process.h>
#include <deque>

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)
#define POW(n) (n*n)

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned char CharactorID;
typedef unsigned char Space;
typedef unsigned char sPos;
typedef short Pos;

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;
typedef vector<unsigned long long> vull;

int T;

typedef vector<bool> Data;

struct DataSet {
	Data data;
	int c;
};

bool chk(const Data& data) {
	for (bool f : data) {
		if (!f)return false;
	}
	return true;
}

int getEval(const Data& data) {
	int ret = 0;

	int l = data.size();
	bool f = data[0];
	for (int i = 1; i < l; ++i) {
		if (data[i] != f) {
			ret++;
			f = data[i];
		}
	}
	return ret + 1;
}

//0~N-1
void flip(Data& data, int index) {

	int l = index / 2;
	for (int i = 0; i <= l; ++i) {
		if (i == index - i) {
			data[i].flip();
			continue;
		}
		bool s = data[i];
		bool e = data[index - i];
		data[i] = e; data[i].flip();
		data[index - i] = s; data[index - i].flip();
	}
}

int BFS(const Data& in) {
	if (chk(in))return 0;
	unordered_map<ll, bool> hash;

	deque<DataSet> que;
	que.push_back(DataSet{ in,0 });

	while (!que.empty()) {
		DataSet ds = que.front(); que.pop_front();

		const int length = ds.data.size();
		REP(i, length) {
			Data buf(ds.data);
		
			flip(buf, i);

			if (hash.count(buf.hash()))continue;
			hash[buf.hash()] = true;

			if (chk(buf))return ds.c+1;

			que.push_back(DataSet{ buf,ds.c + 1 });
		}
	}

	return -1;
}

int BFS2(const Data& in) {
	if (chk(in))return 0;
	
	Data data = in;

	for (int t = 1; t < 10000; ++t) {
		int min = 9999;
		Data minData;

		const int length = data.size();
		REP(i, length) {
			Data buf(data);
			flip(buf, i);

			if (chk(buf))return t;

			int eval = getEval(buf);

			if (min > eval) {
				min = eval; minData = buf;
			}
		}

		data = minData;
	}

	return -1;
}

int main() {
	cin >> T;

	for (int t = 1; t <= T; ++t) {
		Data data;
		string str;
		cin >> str;

		int l = str.length();
		REP(i,l) {
			data.push_back(str[i] == '+');
		}
		int ans = BFS2(data);
		cout << "Case #" << t << ": " << ans << endl;
	}

	return 0;
}