// ConsoleApplication1.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>

using namespace std;

int countLowLevelAudience(const string& table, int level);

int main(void) {

	int T;
	cin >> T;

	for( int ti=1; ti <= T; ti++) {

	string s_max, s_table;
	cin >> s_max >> s_table;

	int result = 0;

	for(int i = atoi(s_max.c_str()); i > 0; i--) {
		int low_level_sum = countLowLevelAudience(s_table, i);
		if( i > low_level_sum + result) {
			result = i - low_level_sum;
		}
	
	}

	printf("Case #%d: %d\n", ti, result);

	}
	return 0;
}

// 指定したレベルより低い人数を返す
int countLowLevelAudience(const string &table, int level) {
	int result = 0;

	for(int i = 0; i < level; i++) {
		result += (table[i] - '0');
	}

	return result;
}