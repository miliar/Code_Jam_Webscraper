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

int t,n,ans;

string s;

int main() {
	// freopen("inp", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin>>t;

	for(int a=1;a<=t;a++) {
		cin>>s;

		n=s.length();

		if(s[n-1] == '+')
			ans = 0;
		else
			ans = 1;

		for(int i = n-2; i >= 0; i--) {
			if(s[i] != s[i+1])
				ans++;
		}


		printf("Case #%d: %d\n",a,ans);
	}




	return 0;
}