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
#define vs vector<string>
#define vpi vector<pi>
#define vpll vector<pll>
#define ALL(x) (x).begin(),(x).end()
#define Max (1<<30)
#define LLMax (1ll<<60)
template<class T>string ToString(T t){stringstream s;s<<t;return s.str();}
template<class T>void ToOther(T&t,string a){stringstream s(a);s>>t;}


#define vll vector<ll>
#define mod 1000002013
#define MAXN 200


int A[2005];
int B[2005];
int r[2005];
int n;
int pos[2005];
bool use[2005];
int d1[22];
int d2[22];
bool END=0;
void go(int x,int be){

	if(x==n+1){


		d2[n]=1;
		for(int i=n-1;i>=1;i--){
			d2[i]=1;
			for(int k=n;k>i;k--)if(r[i]>r[k])d2[i]=max(d2[i],d2[k]+1);
			if(d2[i]!=B[i])return;
		}
		END=1;
		return;
	}

	int s=1,e=n;
	if(A[x-1]<A[x]){
		s=be+1;
	}else e=be-1;


	for(int i=s;i<=e;i++)if(!use[i]){
		use[i]=1;
		r[x]=i;
		d1[x]=1;
		for(int k=1;k<x;k++)if(i>r[k])d1[x]=max(d1[x],d1[k]+1);
		if(d1[x]!=A[x])goto NO;
		go(x+1,i);
		NO:;
		if(END)return;
		use[i]=0;
	}
}

int main(){
	freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
	int T;
	cin>>T;

	for(int test=1;test<=T;test++){

		cin>>n;
		for(int i=1;i<=n;i++)cin>>A[i];
		for(int i=1;i<=n;i++)cin>>B[i];

		END=0;
		memset(use,0,sizeof(use));
		d1[1]=1;
		for(int i=1;i<=n;i++){
			r[1]=i;
			use[i]=1;
			go(2,i);
			if(END)break;
			use[i]=0;
		}
		cout<<"Case #"<<test<<": ";
		for(int i=1;i<=n;i++)cout<<r[i]<<" ";
		cout<<endl;
	}

}


