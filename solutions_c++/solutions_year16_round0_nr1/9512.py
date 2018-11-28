#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
using namespace std;

bool f[10];
long long n, tmp, cnt, x, cases, now;
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	ios::sync_with_stdio(false);
	cin >> cases;
	for (int i = 1; i <= cases; i++) {
		cout << "Case #" << i << ": ";
		cin >> n;
		if (n == 0) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		memset(f, false, sizeof f);
		tmp = cnt = 0;
		
		while (++tmp) {
			now = tmp * n;
			while (now) {
				x = now % 10LL;
				if (!f[x]) {
					cnt++;
					f[x] = true;
				}
				now /= 10LL;
			}
			if (cnt == 10) break;
		}
		
		cout << tmp * n << endl;
	}

} 
