#include <iostream>
#include <map>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <algorithm>
#include <iomanip>
#include <cmath>
#include <vector>
#include <cstring>
#include <cstdlib>

#define mp make_pair
#define pb push_back
#define ppb pop_back
#define X first
#define Y second

using namespace std;

int a[20000];
int b[20000];
int n, x;

int main(){
	freopen("inputb2.in","r",stdin);
	freopen("outputb2.out","w",stdout);
	int T;
	cin >> T;
	for (int TT = 1; TT <= T; TT++){
		printf("Case #%d: ", TT);
				
		cin >> n;
		for (int i = 0; i < n; i++){
			cin >> a[i];
			b[i] = 0 ;
		}
		a[n] =  2000000000;

		int ans = 0;
		for (int i = 0; i < n; i++){
			int l = n;
			for (int j = 0; j < n; j++){
				if (b[j] == 0)
					if (a[l] > a[j]) l = j;
			}

			b[l] = 1;

			int a1 = 0, a2 = 0;
			for (int j = 0; j < n; j++){
				if (b[j] == 0){
					if (j < l) a1++; else a2++;
				}
			}

			ans += min(a1, a2);
		}
		cout << ans << endl;
	}
    return 0;
}
