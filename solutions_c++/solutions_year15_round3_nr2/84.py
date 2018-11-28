/*
	In the Name Of GOD
	TRIPLE NARENGIES:)
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
int k,l,s;
string keyboard;
string target;
int maximum ;

int tavan(int a,int b){
	int ans = 1;
	FOR(i,b){
		ans*=a;
	}
	return ans;
}
bool allok(){
	FOR(i,target.sz){
		bool flag = 1;
		FOR(j,keyboard.sz){
			if(keyboard[j]==target[i])
				flag = 0;
		}
		if(flag)
			return 0;
	}
	return 1;
}


int beshmar(string a,string b){
	int ans = 0;
	FOR(i,b.sz-a.sz+1){
		bool flag = 1;
		FOR(j,a.sz){
			if(a[j]!=b[j+i])
				flag = 0;
		}
		if(flag)
			ans++;
	}
	// sh(a);
	// sh(b);
	// sh(ans);
	maximum = max(ans,maximum);
	return ans;
}

int findbestpish(){
	for(int i=1;i<=target.sz;i++){
		bool flag = 1;
		for(int j=0;j<target.sz-i;j++){
			if(target[j]!=target[j+i])
				flag = 0;
		}
		if(flag)
			return i;
	}
	return target.sz;
}


int findtedad(){
	if(!allok())
		return 0;
	int pish = findbestpish();
	sh(pish);
	if(pish==target.sz)
		return s/target.sz;
	return (s-target.sz+pish)/(pish);
}


double findp(){
	double ans = 1;
	FOR(i,target.sz){
		int cnt = 0;
		FOR(j,keyboard.sz){
			if(keyboard[j]==target[i])
				cnt++;
		}
		ans*=(double)cnt/(double)keyboard.sz;
	}
	return ans;
}

int main()
{
	ios::sync_with_stdio(false);
	int T; cin>>T;
	int test = 0;
	while(T--)
	{
		test++;
		cin>>k>>l>>s;
		maximum = 0;
		cin>>keyboard;
		cin>>target;
		/*string tmp;
		int tedad =0;
		FOR(i,tavan(k,s)){
			string here;
			int h = i;
			FOR(j,s){
				int now = h%k;
				here+=keyboard[now];
				h/=k;
			}
			//sh(here);
			tedad+=beshmar(target,here);
			//sh(tedad);
		}
	//	sh(maximum);
		double ans = (double)maximum - (double)tedad/double(tavan(k,s));*/

		int tedad = findtedad();
		sh(tedad);
		double p = findp();
		//sh(p);
		p*=(double)(-target.size()+s+1);
		//sh(target.sz-s+1);
		//sh(target.sz);
		//sh(s);
		double ans = (double)tedad - p;
		cout<<"Case #"<<test<<": ";
		printf("%.7lf\n",ans);
	}
}
