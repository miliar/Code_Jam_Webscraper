#include<bits/stdc++.h>

using namespace std;
#define CLR(a,val) memset(a, val, sizeof(a))
#define SZ(V) (LL)V.size()
#define ALL(V) V.begin(),V.end()
#define RALL(V) V.rbegin(),V.rend()
#define FORN(i, n) for(LL i = 0; i < n; i++)
#define FORAB(i, a, b) for(LL i = a; i <= b; i++)
#define MOD 1000000007LL
#define PB push_back
#define MP make_pair
#define F first
#define S second

typedef long long LL;
typedef pair<LL,LL> pll;

double a[1005],b[1005];
int main()
{
	LL test;
	cin >> test;
	FORAB(tc,1,test){
		LL n;
		cin >> n;
		FORN(i,n) cin >> a[i];
		FORN(i,n) cin >> b[i];
		sort(a,a+n);
		sort(b,b+n);
 		LL ct1=0,ct2=n;
 		LL l=n-1,r=n-1;
 		while(l>=0 && r>=0){
 			if(a[l]>b[r]){
 				ct1++;
 				l--;
 			}
 			r--;
 		}
 		l=0,r=0;
 		while(l<n && r<n){
 			if(a[l]<b[r]){
 				ct2--;
 				l++;
 			}
 			r++;
 		}
		printf("Case #%lld: %lld %lld\n",tc,ct1,ct2 );
	}
	return 0;
}