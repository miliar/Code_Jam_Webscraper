#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <stack>
#include <queue>
#define fr(i,m,n) for(i=m;i<n;i++)
#define ifr(i,m,n) for(i=m;i>n;i--)
#define ll long long
#define sc scanf
#define pf printf
#define var(x) x i=0,j=0,k=0,tmp1=0,tmp2=0,tmp3=0,tmp=0,tmp4=0,tmp5=0,flag=0
#define pb push_back
#define vi vector<int>
#define vii vector<pair<int,int> >
#define vl vector<ll>
#define vll vector<pair<ll,ll> >
using namespace std;

int main() {
	int T;
	var(int);
	string inp,opt;
	sc("%d",&T);
	fr(k,1,T+1) {
		opt="";
		cin>>inp;
		opt+=inp[0];
		fr(i,1,inp.length()) {
			if(inp[i]>=opt[0]) opt=inp[i]+opt;
			else opt=opt+inp[i];
		}
		cout<<"Case #"<<k<<": "<<opt<<endl;
	}
	return 0;
}