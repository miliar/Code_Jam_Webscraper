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
double F,C,X;

template <class T>
bool rough_lt(T lhs, T rhs, T epsilon = 1e-7) // operator<
{
  return rhs - lhs >= epsilon;
}


double res(double f){
	double firstOpt = X/f;
	double cost = C/f;
	if(cost+X/(f+F)<firstOpt) {
		auto val = cost+res(f+F);
		return val;
	}
	else{
		return firstOpt;
	}
}
int main( int argc, char** argv )
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w+",stdout);
	int t;
	S(t);
	REP(test,t){
		cout<<"Case #"<<test+1<<": ";
		S(C);S(F);S(X);
		cout<<setprecision(7)<<fixed<<res(2.0)<<endl;
	}
	return 0;
	}
