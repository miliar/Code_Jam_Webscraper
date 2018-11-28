#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <stack>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>

using namespace std;

#define ll long long
#define pi pair<int,int>
#define pll pair<ll,ll>
#define pii pair<int,pi>
#define X first
#define Y second
#define pb push_back
#define ab(x) ((x)<0?(-(x)):(x))
#define xx(x) ((x)*(x))
#define mp make_pair
#define vi vector<int>
#define vll vector<ll>
#define vs vector<string>
#define vpi vector<pi>
#define vpll vector<pll>
#define ALL(x) (x).begin(),(x).end()
#define Max (1<<30)
#define LLMax (1ll<<60)
template<class T>string ToString(T t){stringstream s;s<<t;return s.str();}
template<class T>void ToOther(T&t,string a){stringstream s(a);s>>t;}



#define mod 1000000007
#define mod2 (1ll<<55)

// cout<<"Case #"<<test<<": "<<;

int N,M,P;
int d[22];

vi U,V,A[2];
vi v[22];
vi cnt[22];
vi s[2][22];
vi a;


void di(int st){

	bool ck[22]={0};

	ck[2]=1;
	priority_queue<pi,vector<pi>, greater<pi> > q;
	q.push(pi(0,2));
	d[2]=0;

	while(q.size()){
		int k=q.top().Y;
		int dis=q.top().X; q.pop();

		ck[k]=1;

		for(int i=0;i<v[k].size();i++){
			int &t=v[k][i];
			int c=cnt[k][i];

			if(d[t]>d[k]+s[st>>c&1][k][i]){
				d[t]=d[k]+s[st>>c&1][k][i];
				q.push(pi(d[t],t));
			}
		}
	}
}

int main(){
	freopen("output.txt","w",stdout);freopen("input.txt","r",stdin);
	int TT;
	cin>>TT;
	for(int test=1;test<=TT;test++){

		//////////////////////////////////////////////
		for(int i=1;i<=20;i++){
			v[i].clear();
			s[1][i].clear();
			s[0][i].clear();
			cnt[i].clear();
		}
		a.clear();
		U.clear();
		V.clear();
		A[0].clear();
		A[1].clear();
		cin>>N>>M>>P;

		for(int i=0;i<M;i++){
			int X,Y,S,E;
			cin>>X>>Y>>S>>E;
			v[Y].pb(X);
			s[0][Y].pb(S);
			s[1][Y].pb(E);
			cnt[Y].pb(i);
			

			U.pb(X);
			V.pb(Y);
			A[0].pb(S);
			A[1].pb(E);

		}
		for(int i=0;i<P;i++){int t;cin>>t;a.pb(t);}
		
		int rst=-1;
		for(int st=0;st<(1<<M);st++){
			memset(d,63,sizeof(d));

			di(st);

			int now=-1;
			int val=0;
			int dis=d[1];
			for(int k=0;k<P;k++){
				int t=a[k];
				t--;
				val+=A[st>>t&1][t];

				if(dis>=val+d[V[t]])now=k;
				else break;
			}
			rst=max(rst,now);
		}

		rst++;
		cout<<"Case #"<<test<<": ";
		if(rst==P){
			cout<<"Looks Good To Me";
		}else cout<<a[rst];
		cout<<endl;
		//////////////////////////////////////////////
	}
}

