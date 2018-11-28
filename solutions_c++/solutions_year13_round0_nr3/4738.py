#include<algorithm>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<deque>
#include<iostream>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<string>
#include<vector>
using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define ITER(i,a) for(typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define MOD 1000000007

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long int ll;

int main(){
	freopen("new1.txt","r",stdin);
	freopen("out1.txt","w",stdout);
	int A[]={1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002,10000001,10011001,10100101,10111101,11000011,11011011,11100111,11111111,20000002};
	int test;
	int cases=0;
	for(scanf("%d",&test);test>0;test--){
		ll a,b;
		scanf("%lld%lld",&a,&b);
		int n1=ceil(sqrt(a*1.0));
		int n2=floor(sqrt(b*1.0));
		int count=0;
		for(int i=0;i<48;i++) if(n1<=A[i] && A[i]<=n2) ++count;
		printf("Case #%d: %d\n",++cases,count);
	}
	return 0;
}
