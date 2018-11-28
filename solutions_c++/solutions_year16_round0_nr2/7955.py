/* ***************************************************************
 * Program Name :Set.Insert()
 * Date:Feb 19, 2016
 * Author:Mahmoud Ismail
 *Copyright:Your copyright notice
 ************************************************************/
#define _CRT_SECURE_NO_WARNINGS 
#include<bits/stdc++.h>
#include<stdio.h>
#include<sstream>
#include <stdlib.h> 
#include<iostream>
#include<string>
#include<algorithm>
#include <limits>
#include<queue>
#include<vector>
#include<set>
#include <cstdio>
#include <cstring>
#include<map>
#include<cmath>
#include<climits>
#include<iomanip>
#include<utility>
#include<set>
#include<iterator>
using namespace std;
int main() {

	int t;
	scanf("%d", &t);
	int c = 1;

	while (t--) {
		string s = "", st;
		cin >> st;
		int sz = st.size();
		char top;
		for (int i = 0; i < sz; i++) {
			if (i == 0) {
				top = st[0];
				s += st[i];
			} else {
				if (st[i] != top) {
					top = st[i];
					s += st[i];
				}

			}
		}

		bool po = false, ne = false;
		int cnt = 0;
		sz = s.size();

		for (int i = 0; i < sz; i++) {
			if (s[i] == '-') {
				ne = true;
			}
			if (s[i] == '+') {
				po = true;

			}
			if (i == sz - 1) {

				if (s[i] == '-' && po) {
					cnt += 2;

				} else if (s[i] == '-' && !po) {

					cnt++;
				}
				break;
			}
			if (s[i] == '-' && !po) {
				cnt++;
				ne=false;
				po=true;

			} else if (s[i] == '+' && ne) {

				cnt++;
				ne = false;
				po = true;

			} else if (s[i] == '-' && po) {
				cnt += 2;
				po = true;
				ne = false;
			}

		}

		printf("Case #%d: %d\n", c, cnt);
		c++;

	}
	return 0;
}
