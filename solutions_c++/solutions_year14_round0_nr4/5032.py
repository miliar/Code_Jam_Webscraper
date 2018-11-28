#include <iostream>
#include <stdio.h>
#include <math.h>
#include <list>
#include <queue>
#include <vector>
#include <functional>
#include <stack>
#include <utility> 
#include <stdlib.h>
#include <map>
#include <string.h>
#include <algorithm>
typedef long long int ll;
#define SWAP(a, b) (((a) ^= (b)), ((b) ^= (a)), ((a) ^= (b)))
#define gc getchar_unlocked
#define CLR(a) memset(a, 0, sizeof(a))
int ri() { char c = gc(); while(c<'0' || c>'9') c = gc(); int ret = 0; while(c>='0' && c<='9') { ret = 10 * ret + c - 48; c = gc(); } return ret; }
using namespace std;
int main() {
	double a[1001], b[1001];
	int n, t, i, j, m, temp, win2, win1;
	cin>>t;
	for(int lol = 1; lol <= t; ++lol) {
		cin>>n;
		for(i=0;i<n;++i) {
			cin>>a[i];
		}
		for(i=0;i<n;++i) {
			cin>>b[i];
		}
		sort(a, a+n);
		sort(b, b+n);
		temp = n;
		m = n - 1;
		--n;
		win1 = win2= 0;
		i = 0;
		j = 0;
		while(i<=m && j<=n) {
			if(a[i] < b[j]) {
				--n;
				++i;
			} else if(a[m] < b[n]) {
				++i;
				--n;
			} else if(a[m] > b[n]) {
				win2++;
				--m; --n;
			}
		}
		n = temp-1;
		m = n;
		i = 0; j =0;
		while(i<=m && j<=n) {
			if(a[i] < b[j]) {
				++i;++j;
			} else if(a[i] > b[j]) {
				//cout<<a[i]<<b[j];
				int found = 0, where;
				for(int kk = j+1; kk <= n; ++kk) {
					if(a[i] < b[kk]) {
						found = 1; where = kk; break;
					}
				}
				
				if(found) {
					b[where] = 999999.0;
					sort(b, b+temp);
					--n;
					++i;
				} else {
					++i;
					++j;
					win1++;
				}
			}
		}
		printf("Case #%d: %d %d\n", lol, win2, win1);
	}
	return 0;
}