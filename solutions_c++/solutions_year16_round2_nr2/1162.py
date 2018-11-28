/*
	In the Name Of GOD
*/
#include <vector>
#include <map>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <complex>
#include <queue>
#include <stack>
#include <map>
#include <bitset>
#include <iomanip>
#include <set>
#include <stack>
#include <stdio.h>

using namespace std;
#define N 10020
#define MAXN 60
#define X first
#define Y second
#define CLR(x,a) memset(x,a,sizeof(x))
#define FOR(i,b) for(ll i=0;i<(b);i++)
#define FOR1(i,b) for(ll i=1;i<=(b);i++)
#define FORA(i,a,b) for(ll i=(a);i<=(b);i++)
#define FORB(i,b,a) for(ll i=(b);i>=(a);i--)
#define sh(x) cerr<<(#x)<<" = "<<(x)<<endl
#define EPS 0.00001
#define ull unsigned long long int
#define ll long long 
#define MP make_pair
#define PB push_back
#define ALL(v) (v).begin(),(v).end()
#define sz size()
#define EXIST(a,b) find(ALL(a),(b))!=(a).end()
#define Sort(x) sort(ALL(x))
#define UNIQUE(v) Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define timestamp(x) printf("Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)
//const double PI = acos(-1);
typedef complex<double> point;
typedef pair<int,int> pii;
typedef pair<int, pii> piii;
typedef vector<int> vi;
typedef vector<vi > vii;
typedef vector<pii> vpii;
typedef vector<piii> vpiii;

bool ok(int a,string x){
	for(int i=x.sz-1;i>=0;i--){
		if(x[i]!='?' && x[i]-'0'!=a%10)
			return 0;
		a/=10;
	}
	return 1;
}


void solve(string a,string b){
	int minimum = 1000*1000;
	int ans1;
	int ans2;
	FOR(i,pow(10,a.sz)){
		FOR(j,pow(10,a.sz)){
			if(ok(i,a) && ok (j,b) && abs(i-j)<minimum){
				minimum = abs(i-j);
				ans1 = i;
				ans2 = j;
			}
		}
	}
	for(int i=a.sz-1;i>=0;i--){
		a[i] = (ans1%10)+'0';
		b[i] = (ans2%10)+'0';
		ans1/=10;
		ans2/=10;
	}
	cout<<a<<" "<<b;
}

int main()
{
	ios::sync_with_stdio(false);
	int T; cin>>T;
	int test=0;
	string x,y;
	while(T--)
	{
		test++;
		cin>>x>>y;

		cout<<"Case #"<<test<<": ";solve(x,y);cout<<endl;

	}
}
