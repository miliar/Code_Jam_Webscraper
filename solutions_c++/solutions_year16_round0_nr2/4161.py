#pragma once

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <string>
#include <memory.h>
using namespace std;

#include <cctype>
#include <cstdio>
#include <cstdarg>
#include <ctime>
#include <cmath>
#include <cassert>


const int INF = (1 << 30) - 1;
const float PI = (float)acos(-1.0);
const float EPS = 1e-5;
const float BASE2 = 1.0/log(2);

int cases;
string s;
int ans;

int main ()
{
	scanf("%d", &cases);
	for (int k = 1; k <= cases; k++) {
		cin >> s;
		ans = 1;
		for (int i = 1; i < s.size(); i++) {
			if (s[i]!=s[i-1]) ans++;
		}
		if (s[s.size()-1] == '+') ans--;
		printf("Case #%d: %d\n", k, ans);
	}
	return 0;
}


