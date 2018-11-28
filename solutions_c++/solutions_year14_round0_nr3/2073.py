#include <iostream>
#include <cstdio>
#include <iomanip>
#include <cmath>
#include <vector>
#include <algorithm>
#include <functional>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <cstdlib>
#include <stack>
#include <queue>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

#define REP(v, hi) for (int v=0;v<(hi);v++)
#define REPD(v, hi) for (int v=((hi)-1);v>=0;v--)
#define FOR(v, lo, hi) for (int v=(lo);v<(hi);v++)
#define FORD(v, lo, hi) for (int v=((hi)-1);v>=(lo);v--)
#define REP1(v, hi) for (int v=1;v<=(hi);v++)
#define REPD1(v, hi) for (int v=(hi);v>=1;v--)
#define FOR1(v, lo, hi) for (int v=(lo);v<=(hi);v++)
#define FORD1(v, lo, hi) for (int v=(hi);v>=(lo);v--)

const double eps = 1 / (double)1000000000;

// if (M <= (R - 2)*(C - 2))
bool zeroFunction(int R, int C, int M) {
	string tmp = "....................................................................................";
	vector<string> str;
	REP(i, R) str.push_back(tmp.substr(0, C));
	int cntM = 0;
	REP(row, R) {
		REP(col, C) {
			if (cntM < M) {
				if (col < C - 2) {
					++cntM;
					str[row][col] = '*';
				}
			}
		}
	}
	str[R - 1][C - 1] = 'c';
	REP(i, str.size()) cout << str[i] << endl;
	return true;
}

// if (R == 2 || C == 2)
bool firstFunction(int R, int C, int M) {
	if (!((R*C - M) >= 4 && (R*C - M) % 2 == 0)) {
		return false;
	}
	string tmp = "....................................................................................";
	vector<string> str;
	REP(i, R) str.push_back(tmp.substr(0, C));
	int cntM = 0;
	if (R == 2) {
		REP(col, M / 2) {
			str[0][col] = '*';
			str[1][col] = '*';
		}
	} else if (C == 2) {
		REP(row, M / 2) {
			str[row][0] = '*';
			str[row][1] = '*';
		}
	}
	str[R - 1][C - 1] = 'c';
	REP(i, str.size()) cout << str[i] << endl;
	return true;
}

// if (R == 1 || C == 1 || M == R*C - 1)
bool secondFunction(int R, int C, int M) {
	string tmp = "....................................................................................";
	vector<string> str;
	REP(i, R) str.push_back(tmp.substr(0, C));
	int cntM = 0;
	REP(row, R) {
		REP(col, C) {
			if (cntM < M) {
				++cntM;
				str[row][col] = '*';
			}
		}
	}
	str[R - 1][C - 1] = 'c';
	REP(i, str.size()) cout << str[i] << endl;
	return true;
}

// 적어도 3*3 이상의 맵이 들어온다.
bool thirdFunction(int R, int C, int M) {
	int B = (R*C - M); // 공백 갯수
	string tmp = "**************************************************************";
	vector<string> str;
	REP(i, R) str.push_back(tmp.substr(0, C));
	if (B <= 3 || B == 5 || B == 7)
	{
		return false;
	}
	int cntB = B;
	// 왼쪽 위를 공백으로 하는 경우
	// 일단 4 개 정사각형으로 채우고 시작함.
	REP(row, 2) REP(col, 2) str[row][col] = '.';
	cntB -= 4;

	// 그 다음 오른쪽으로 2 개씩 붙여서 늘려나감
	// 그러다 남은게 3이면 한줄 위에 3개 늘리고 끝.
	FOR(col, 2, C) {
		if (cntB == 3) {
			cntB -= 3;
			REP(i, 3) str[2][i] = '.';
		}
		if (cntB == 0){
			str[0][0] = 'c';
			REP(i, str.size()) cout << str[i] << endl;
			return true;
		}
		cntB -= 2;
		str[0][col] = '.';
		str[1][col] = '.';
	}

	// 왼쪽 2 열에 .. 을 써내려감
	// 그러다 남은게 1 개면 [2,2] 에 . 쓰고 끝냄
	FOR(row, 2, R) {
		if (cntB == 1) {
			cntB -= 1;
			str[2][2] = '.';
		}
		if (cntB == 0){
			str[0][0] = 'c';
			REP(i, str.size()) cout << str[i] << endl;
			return true;
		}
		cntB -= 2;
		str[row][0] = '.';
		str[row][1] = '.';
	}

	FOR(row, 2, R) {
		FOR(col, 2, C) {
			if (cntB > 0) {
				--cntB;
				str[row][col] = '.';
			}
		}
	}
	str[0][0] = 'c';
	REP(i, str.size()) cout << str[i] << endl;
	return true;
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
	int t;
	cin >> t;
	REP1(tt, t)
	{
		int R, C, M;
		cin >> R >> C >> M;
		cout << "Case #" << tt << ":" << endl;
		//cout << "Case #" << tt << ": " << R << " " << C << " " << M << endl;
		bool isPossible = false;
		if (R == 1 || C == 1 || M == R*C - 1)
		{
			isPossible = secondFunction(R, C, M);
		}
		if (isPossible) continue;

		if (R == 2 || C == 2)
		{
			isPossible = firstFunction(R, C, M);
			if (!isPossible) cout << "Impossible" << endl;
			continue;
		}
		if (isPossible) continue;

		if (M <= (R - 2)*(C - 2))
		{
			isPossible = zeroFunction(R, C, M);
		}
		if (isPossible) continue;
		
		isPossible = thirdFunction(R, C, M);

		if (!isPossible) cout << "Impossible" << endl;
	}
	return 0;
}

