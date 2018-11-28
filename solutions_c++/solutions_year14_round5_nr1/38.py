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
lint num[1234567];
int main()
{
	lint p,q,r,s;int t,n;
	cin>>t;
	rep(i,t){
		cin>>n>>p>>q>>r>>s;
		rep(j,n) num[j]=(j*p+q)%r+s;
		lint sum=0;
		rep(j,n) sum+=num[j];
		if(n==1){
			printf("Case #%d: %.12f\n",i+1,0.0);continue;
		}
		if(n==2){
			printf("Case #%d: %.12f\n",i+1,1.0*min(num[0],num[1])/sum);continue;
		}
		lint lo=0,hi=sum;
		while(hi>lo){
			lint mi=(hi+lo)/2,ns=0;int ch=0;
			rep(j,n){
				if(num[j]>mi){ch=10;break;}
				if(ns+num[j]>mi){ns=num[j];ch++;}
				else ns+=num[j];
			}
			if(ch>2) lo=mi+1;else hi=mi;
		}
		printf("Case #%d: %.12f\n",i+1,1.0*(sum-lo)/sum);
	}
}
