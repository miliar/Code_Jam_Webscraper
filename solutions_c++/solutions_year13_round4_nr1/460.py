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
typedef pair<lint,lint> pint;
#define All(s) s.begin(),s.end()
#define rAll(s) s.rbegin(),s.rend()
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
lint num[2100];
map<lint,int> de;
vector <lint> ba,ba2;
lint a[1100],b[1100],c[1100];
lint n,mo=1000002013;
lint cal(lint a){
	return (n*a)+mo-(500001007*a)%mo*(a-1)%mo;
}

int main()
{
	int m,t;
	cin>>t;
	rep(i,t){
		ba.clear();ba2.clear();memset(num,0,sizeof(num));
		cin>>n>>m;lint ret=0,ret2=0;
		rep(j,m){
			cin>>a[j]>>b[j]>>c[j];
			ba.pb(a[j]);ba.pb(b[j]);
			ret=(ret+c[j]*cal(b[j]-a[j]))%mo;
		}
		sort(All(ba));
		ba2.pb(ba[0]);
		rep(j,ba.size()-1){
			if(ba[j+1]!=ba[j]) ba2.pb(ba[j+1]);
		}
		int p=ba2.size();de.clear();
		rep(j,p) de[ba2[j]]=j;
		rep(j,m){
			int s=de[a[j]],g=de[b[j]];
			REP(k,s,g) num[k]+=c[j];
		}
		rep(j,3*m){
			int s=-1;lint mi;
			rep(k,p+10){
				if(s>=0){
					if(num[k]<1){
						ret2=(ret2+mi*cal(ba2[k]-ba2[s]))%mo;
						REP(l,s,k) num[l]-=mi;s=-1;mi=-1;
					}
					else mi=min(mi,num[k]);
				}
				else{
					if(num[k]>0){
						s=k;mi=num[k];
					}
				}
			}
		}
		printf("Case #%d: %d\n",i+1,(int)((ret+mo-ret2)%mo));
	}
};
