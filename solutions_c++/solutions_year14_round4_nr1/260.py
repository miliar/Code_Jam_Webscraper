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
	freopen("inputa2.in","r",stdin);
	freopen("outputa2.out","w",stdout);
	int T;
	cin >> T;
	for (int TT = 1; TT <= T; TT++){
		printf("Case #%d: ", TT);
				
		cin >> n >> x;
		for (int i = 0; i < n; i++){
			cin >> a[i];
			b[i] = 0;
		}

		sort(a, a + n);

		int j = n - 1;
		int ans = 0;
		for (int i = 0; i < n; i++){
			if (b[i] == 1) continue;

			while (j > i){
				if (b[j] == 1) j--; else
					if (a[j] + a[i] > x) j--; else break;
			}

			if (j > i){
				b[j] = 1;
				j--;
			}
			b[i] = 1;
			ans++;
		}
		cout << ans << endl;
	}
    return 0;
}
