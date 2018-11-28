#include <cassert>
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <utility>
#include <iomanip>
#define PR(x) cout<<#x<<"="<<x<<endl
#define READ2(x,y) scanf("%d %d",&x,&y)
#define REP(i,a) for(int i=0;i<a;i++)
#define RP(i,init,a) for(int i=init;i<a;i++)
#define S(x) cin>>x
#define PRARR(x,n) for(int i=0;i<n;i++)printf(#x"[%d]=\t%d\n",i,x[i])
#define rd(arr,i,n) for(int i=0;i<n;i++) cin>>arr[i]
#define PB push_back
#define SUM(arr,n,sum) {sum=0;for(int i=0;i<n;i++) sum+=arr[i]; }
#define VC vector
#define CLR(arr) memset(arr,0,sizeof(arr))
#define FILL(arr,val) memset(arr,val,sizeof(arr))
#define TR(iter, container) for(auto iter = container.begin();iter!=container.end();iter++ )
using namespace std;
inline long long Tr(long long &a, long long &b){
	long long gc= __gcd(a,b);
	a/=gc;
	b/=gc;
}
 
int main( int argc, char** argv )
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w+",stdout);
	int t;
	S(t);
	REP(test,t){
		
		int cntr = 0;
		cout<<"Case #"<<test+1<<": ";
		long long a,b;
		scanf("%lld/%lld",&a,&b);
		Tr(a,b);
		if(!(b&(b-1))){
				int cntr = 0;
				while(b&&b>a){
					b>>=1;
					cntr++;
				}
				cout<<cntr<<endl;
		}else{
			cout<<"impossible"<<endl;
		}
	}
	return 0;
}
