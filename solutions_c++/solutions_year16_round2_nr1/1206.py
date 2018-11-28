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

int arr[26];

void menha(string tmp,int meqdar){
	FOR(i,tmp.sz)
	arr[tmp[i]-'A']-=meqdar;
}

string solve(string x){
	FOR(i,26)arr[i]=0;
	FOR(i,x.sz){
		arr[x[i]-'A']++;
	}
	int number[10];
	FOR(i,10) number[i] =0 ;
	int z = arr['Z'-'A'];
	number[0] = z;
	menha("ZERO",z);
	int xx = arr['X'-'A'];
	number[6]=xx;
	menha("SIX",xx);
	int g = arr['G'-'A'];
	number[8]=g;
	menha("EIGHT",g);
	int s = arr['S'-'A'];
	number[7] = s;
	menha("SEVEN",s);
	int v = arr['V'-'A'];
	number[5] = v;
	menha("FIVE",v);
	int f = arr['F'-'A'];
	number[4] = f;
	menha("FOUR",f);
	int w = arr['W'-'A'];
	number[2] = w;
	menha("TWO",w);
	int t = arr['T'-'A'];
	number[3] = t;
	menha("THREE",t);
	int o = arr['O'-'A'];
	number[1] = o;
	menha("ONE",o);
	int n = arr['N'-'A']/2;
	number[9] = n;
	string ans = "";
	FOR(i,10){
		FOR(j,number[i])
			ans+=(i+'0');
	}
	return ans;
}

int main()
{
	ios::sync_with_stdio(false);
	int T; cin>>T;
	int test=0;
	string x;
	while(T--)
	{
		test++;
		cin>>x;
		cout<<"Case #"<<test<<": "<<solve(x)<<endl;

	}
}
