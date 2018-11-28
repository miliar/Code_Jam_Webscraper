#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstdlib>
#include <string>
#include <climits>
#define ull unsigned long long
#define ll long long
#define ul unsigned long
#define vi vector<int>
#define vll vector<long long>
#define pb push_back
#define pii pair<int, int>
#define pll pair<long long, long long>
#define mp make_pair
#define pq priority_queue

using namespace std;

bool has_blank(const char * pk) {
	for(int i = 0, len = strlen(pk); i < len; ++i) {
		if(pk[i] == '-') return true;
	}
	return false;
}

int main() {
	int tc;
	scanf("%d", &tc);
	for(int itc = 1; itc <= tc; ++itc) {
		char pk[128];
		scanf("%s", pk);
		int nflip = 0;
		while(has_blank(pk)) {
			for(int i = strlen(pk) - 1; i >= 0; --i) {
				if(pk[i] == '+') continue;
				int idx = 0;
				while(idx <= i) {
					pk[idx] = pk[idx] == '+' ? '-' : '+';
					if(idx < i) {
						pk[i] = pk[i] == '+' ? '-' : '+';
					}
					++idx;
					--i;
				}
				break;
			}
			++nflip;
		}
		printf("Case #%d: %d\n", itc, nflip);
	}
	return 0;
}
