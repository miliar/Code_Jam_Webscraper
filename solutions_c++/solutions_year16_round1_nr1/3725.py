#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <bitset>
#include <cstring>
#include <string>
#include <cmath>
#include <queue>
#define lli long long int
#define ii pair<int,int>
#define mp make_pair
#define mod 1000000007
#define inf 999999999

using namespace std;

int t,n;

string s,ans;

char A[110000];

int main() {
	// freopen("inp", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin>>t;

	for(int a=1;a<=t;a++) {
		cin>>s;

		n = s.length();

		A[0]=s[0];

		for(int i=1;i <= n; i++) {
			A[i] = max(s[i], A[i-1]);
		}

		ans = s;

		int l = 0, r = n-1;

		for(int i = n-1; i  >= 0; i--) {
			if(s[i] >= A[i-1]) {
				ans[l] = s[i];
				l++;
			}
			else {
				ans[r] = s[i];
				r--; 
			}
		}

		printf("Case #%d: ",a);
		cout << ans <<endl;
	}




	return 0;
}