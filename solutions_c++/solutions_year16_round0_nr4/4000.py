#include <bits/stdc++.h>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define ll long long
#define ii pair<int,int>
#define mp make_pair
#define pb push_back
#define INF 1000000000
int tc,k,c,s;
int main() {
	scanf("%d",&tc);
	for (int kk=0;kk<tc;kk++) {
		scanf("%d%d%d",&k,&c,&s);
		ll x=1ll;
		for (int i=0;i<c-1;i++) {
			x*=(ll)k;
		}
		printf("Case #%d:", kk+1);
		for (int i=0;i<k;i++) {
			printf(" %lld",x*(ll)i+1ll);
		}
		printf("\n");
	}
}