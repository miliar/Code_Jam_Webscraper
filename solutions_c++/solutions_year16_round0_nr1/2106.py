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
bool sumi[19];
int main()
{
	int n,t;
	cin>>t;
	rep(i,t){
		cin>>n;
		printf("Case #%d: ",i+1);
		if(n==0){
			cout<<"INSOMNIA"<<endl;continue;
		}
		memset(sumi,0,sizeof(sumi));
		int ret=1,num=0;
		for(;num<10;ret++){
			int x=ret*n;
			while(x>0){
				if(!sumi[x%10]){
					sumi[x%10]=true;num++;
				}
				x/=10;
			}
		}
		cout<<n*(ret-1)<<endl;
	}
}
