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
int k,c,s;

int main() {
	// freopen("inp", "r", stdin);
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin>>t;

	for(int a=1;a<=t;a++) {
		cin>>k>>c>>s;

		printf("Case #%d:",a);

		if(s==k) {
			for(int i = 1; i <= k; i++)
				printf(" %d", i);
			printf("\n");
			continue;
		}

	}




	return 0;
}