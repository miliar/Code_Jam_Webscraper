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

double d[1<<20];
bool ck[1<<20];
int n;

double go(int st){
	if(st==0)return 0.0;

	double &r=d[st];
	if(ck[st])return r;r=0;
	ck[st]=1;

	int be=0;
	for(int i=n-1;i>=0;i--){
		if(st>>i&1)break;
		be--;
	}
	queue<int> q;
	double cnt=double(n);

	for(int i=0;i<n*2;i++){
		int k=i%n;
		if(i<n)q.push(i);

		if(st>>k&1){
			while(q.size()){
				int t=q.front();q.pop();
				int wait=i-t;
				int cost=n-wait;

				r+= (cost+go( st ^ (1<<k) ) )/cnt;
			}
		}
	}

	return r;
}

int main(){
	freopen("output.txt","w",stdout);freopen("input.txt","r",stdin);
	int TT;
	cin>>TT;
	for(int test=1;test<=TT;test++){

		//////////////////////////////////////////////

		memset(d,0,sizeof(d));
		memset(ck,0,sizeof(ck));

		int st=0;

		string S;cin>>S;
		n=S.size();
		for(int i=0;i<n;i++)if(S[i]=='.')st|=(1<<i);


		double rst=go(st);
		cout<<"Case #"<<test<<": ";
		printf("%.9lf\n",rst);
		//////////////////////////////////////////////
	}
}

