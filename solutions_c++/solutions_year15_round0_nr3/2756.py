//#include<bits/stdc++.h>
#include<iostream>
#include<string>
#include<cstring>
#include<iomanip>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cmath>
#include<set>
#include<ctime>
#include<cctype>
#include<memory>
#include<cstdlib>
#include<map>
#include<list>
#include<queue>
#include<stack>
#include<climits>
#include<complex>
#include<utility>
#include<functional>
#define INF 0x7fffffff
#define FILL_NINF 0xef
#define FILL_INF 0x3f
#define RE cerr<<"REdebuge"<<endl;
#define M7 1000000007
#define M9 1000000009
#define ifor(s,n) for(int i=(s);i<(n);i++)
#define rep(rep_val) for(int REP_i=0;REP_i<(rep_val);REP_i++)
#define tmin(a,b,c) min((a),min((b),(c)))
#define tmax(a,b,c) max((a),max((b),(c)))
#define eps 1e-8
using namespace std;
typedef long long ll;
typedef pair<int, int> Poi;

const int maxv=10020;
int muti[4][4]={{0,1,2,3},{1,4,3,6},{2,7,4,1},{3,2,5,4}};
struct quater{
	bool s;
	int a;
	quater(){
		this->s=0;
	}
	quater operator * (quater const &C){
		quater ans;
		ans.s=s^C.s;
		ans.a=muti[a][C.a];
		if(ans.a>3){
			ans.s^=1;
			ans.a%=4;
		}
		return ans;
	}
	bool operator == (quater const &C){
		return a==C.a&&s==C.s;
	}
};
quater inv(quater const &a){
	quater ans;
	if(a.a==0){
		ans.a=0;
		ans.s=a.s;
	}
	else{
		ans.a=a.a;
		ans.s=!a.s;
	}
	return ans;
}
int T,t=0;
////1,i,j,k,-1,-i,-j,-k=0,1,2,3,4,5,6,7
quater a[maxv];
quater muls[maxv];
int l,x;
string s;
quater trymul(int b,int e){
	if(b==0)
		return muls[e];
	quater ans=inv(muls[b-1])*muls[e];
	return ans;
}
int main(){
  freopen("in.txt","r",stdin);
   freopen("out.txt","w",stdout);
	//quater a,b;
/*	while(cin>>a.a>>b.a){
		cout<<(a*b).s<<" "<<(a*b).a<<endl;
	}*/
	quater I,J,K;
	I.a=1,I.s=0;
	J.a=2,J.s=0;
	K.a=3,K.s=0;
	cin>>T;
	while(T--){
		t++;
		cin>>l>>x;
		cin>>s;
		for(int i=0;i<l*x;i++){
			a[i].s=0;
			a[i].a=s[i%l]-'h';
			muls[i]=a[i];
		//	if(i==0)
		//	cout<<"mul"<<muls[i].a<<endl;
			if(i>0){
				muls[i]=muls[i-1]*muls[i];
		//		cout<<"mul"<<muls[i].a<<endl;
		//		cout<<(inv(muls[i])*muls[i]).a<<endl;
			}
		}
		int b1=0,b2=1;
		int flag=0;
		while(b1<=l*x-3){
			if(trymul(0,b1)==I){
		//		cout<<"try1     "<<"  "<<trymul(0,b1).a<<"b1   "<<b1<<endl;
				if(trymul(b1+1,b2)==J){
		//			RE
					if(trymul(b2+1,l*x-1)==K){
						flag=1;
						break;
					}
				}
			}
			if(b2==l*x-2){
				b1++,b2=b1+1;
		//		cout<<b1<<endl;
			}
			else b2++;
	//		cout<<b1<<"  "<<b2<<endl;
		}
		if(flag)
		printf("Case #%d: YES\n",t);
		else 
			printf("Case #%d: NO\n",t);
	}
    return 0;
}