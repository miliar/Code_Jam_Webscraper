#include "StdAfx.h"
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;
const int N = 102;
int aa[N];
int main(int argc, char** argv){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tt;
	scanf(" %d", &tt);
	for (int qq = 1; qq <= tt; qq++){
		for (int i = 0; i < N; i++) aa[i] = 0;
		string ss;
		cin >> ss;
		int sl = ss.length();
		for (int i = 0; i < sl; i++){
			aa[i] = ss[i] == '-' ? 0 : 1;
		}
		int ii = 0;
		bool ones;
		bool zeros;
		int res = 0;
		while (true){
			ones = false;
			zeros = false;
			for (; ii < sl; ii++){
				if (aa[ii] == 1) ones = true;
				if (aa[ii] == 0){
					ii++;
					zeros = true;
					break;
				}
			}
			if (zeros == true){
				while (aa[ii] == 0 && ii < sl) { ii++; }
			}
			if (ones && zeros) {
				res += 2;
			}
			else if (zeros) res += 1;
			if (ii >= sl) break;
		}
		printf("Case #%d: %d\n", qq, res);
	}
}

