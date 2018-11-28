#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<fstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<ctime>
#include<queue>
#include<deque>
#include<complex>
using namespace std;
#define pb push_back
#define pf push_front
typedef long long lint;
typedef complex<double> P;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
#define All(s) s.begin(),s.end()
#define rAll(s) s.rbegin(),s.rend()
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
int a[10010];
int main()
{
	int n,x,t;
	cin>>t;
	rep(i,t){
		cin>>n>>x;
		rep(j,n) cin>>a[j];sort(a,a+n);
		int ret=0,it=n-1;
		rep(j,it){
			while(it>j && a[j]+a[it]>x) it--;
			if(it>j && a[j]+a[it]<=x){ret++;it--;}
		}
		printf("Case #%d: %d\n",i+1,n-ret);
	}
}
