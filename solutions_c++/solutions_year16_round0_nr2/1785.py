// ConsoleApplication6.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <cstring>
#include <queue>
#include <algorithm>
#include <climits>
#include <string>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <cmath>
#include <cctype>
#include <iomanip>
#include <cstdio>
#include <list>
#include <set>
#include <iterator>
#include <bitset>


using namespace std;




int T;
vector<bool> S;
char str[100] = { 0, };


int isAllSame() {

	if (all_of(S.begin(), S.end(), [](bool i) {return i; }))
	{
		return 10;
	}
	else if (all_of(S.begin(), S.end(), [](bool i) {return !i; }))
	{
		return 20;
	}

}
void operate_in_range(int m_idx) {

	int cnt;

	for (cnt = 0; cnt < m_idx; cnt++) {
		if (S[cnt] == true) {
			S[cnt] = false;
		}
		else if (S[cnt] == false) {
			S[cnt] = true;
		}
	}

	for (cnt = 0; cnt < m_idx / 2; cnt++) {
		S[cnt] = S[(m_idx - cnt) - 1];
	}

}

void char_to_bool() {

	for (int cnt = 0; cnt < sizeof(str); cnt++) {

		if (str[cnt] == '+') {
			S.push_back(true);
		}

		else if (str[cnt] == '-') {
			S.push_back(false);
		}
	}
}

int get_idx() {
	for (int cnt = 1; cnt < S.size(); cnt++) {
		if (S[cnt] != S[0]) return cnt;
	}
}

int main() {

	int cnt, answer_cnt = 1, maneuver_cnt = 0, idx = 0;
	
	ifstream fin;
	ofstream fout;

	fin.open("input.in");
	fout.open("output.out");

	fin >> T;
	int n_T = T;

	for (int i = 0; i < n_T; i++) {
		fin >> str;
		char_to_bool();
		while (true) {
			if (isAllSame() == 10) {
				fout << "Case #" << answer_cnt << ": " << maneuver_cnt << endl;
				answer_cnt++;

				maneuver_cnt = 0;
				S.clear();
				break;
			}
			else if (isAllSame() == 20) {
				maneuver_cnt++;
				fout << "Case #" << answer_cnt << ": " << maneuver_cnt << endl;
				answer_cnt++;

				maneuver_cnt = 0;
				S.clear();

				break;
			}

			operate_in_range(get_idx());
			maneuver_cnt++;
		}
		for (cnt = 0; cnt < 100; cnt++) 	str[cnt] = 0;
		
	}

	fin.close();
	fout.close();
	system("pause");

	return 0;
}








