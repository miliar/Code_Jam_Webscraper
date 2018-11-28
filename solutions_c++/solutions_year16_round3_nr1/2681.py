// codejam_1c_A_Senate_Evacuation.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <bitset>
#include <unordered_map>
#include <unordered_set>
#include <queue>

using namespace std;

#pragma warning(disable:4996)

#define REP(i, a, b) for(int i=a; i<b; i++)
#define REP0(i, n) REP(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl

//#define DEBUG

#ifdef DEBUG
#define		fin		cin
#define		fout	cout
#endif

int main()
{
#ifndef DEBUG
	fstream fin, fout;
	fin.open("A-large.in", ios::in);
	fout.open("A-large.out", ios::out);
#endif

	int T;
	fin >> T;

	for (int cases = 1; cases <= T; cases++) {
		int N; fin >> N;

		priority_queue<pair<int, char>> pq;
		char P = 'A';
		int tot = 0;
		REP0(i, N) {
			int n; fin >> n;
			pq.push(make_pair(n, P++));
		}

		fout << "Case #" << cases << ":";

		if (pq.size() == 2) {
			while (!pq.empty()) {
				pair<int, char> pp = pq.top(); pq.pop();
				string res = "";
				pp.first--;
				res += pp.second;

				if (pp.first > 0)
					pq.push(pp);

				pp = pq.top(); pq.pop();
				pp.first--;
				res += pp.second;

				if (pp.first > 0)
					pq.push(pp);

				fout << " " << res;
			}

			fout << endl;
		}
		else {
			while (!pq.empty()) {
				pair<int, char> pp = pq.top(); pq.pop();
				string res = "";
				pp.first--;
				res += pp.second;

				if (pp.first > 0)
					pq.push(pp);

				if (pq.size() == 1) {
					pp = pq.top(); pq.pop();
					pp.first--;
					res += pp.second;

					if (pp.first > 0)
						pq.push(pp);
				}

				fout << " " << res;
			}

			fout << endl;
		}
	}

#ifndef DEBUG
	fin.close();
	fout.close();
#endif

	return 0;
}