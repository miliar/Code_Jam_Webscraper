//*
#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <deque>
#include <set>
#include <map>
#include <list>
#include <limits>
#include <queue>
#include <stdexcept>
#include <iomanip> 
#include <sstream>
using namespace std;

#define REP(i,n) for(i=0;i<(n);i++)
#define RR 102
#define CC 102

typedef long long ll;
typedef pair<ll, ll> pll;
typedef vector<ll,ll> vll;

char str[RR][CC];
int	power[RR][CC];	


#define TRY
#define SMALL
#define LARGE

ll Gcd(ll a,ll b);
int Solve();

struct A{
	ll index;
	ll rad;
	ll x,y;
	bool operator <(const A &p)const{
		return rad < p.rad;
	}
};
bool cmp(A x,A y)
{
	return x.index<y.index;
}
int main() 
{
#ifdef TRY
	freopen("1.txt", "rt", stdin);
	//freopen("2.out","wt",stdout);
#endif
#ifdef SMALL
	freopen("A-small-attempt1.in","rt",stdin);
	freopen("AA-small.txt","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.txt","wt",stdout);
#endif
	int Numcase;
	
	cin>>Numcase;
	for(int test=1;test<=Numcase;test++)
	{
		cout<<"Case #"<<test<<": ";
		cout<<Solve()<<endl;
		
	}
}
int Solve()
{
	int i,j,k,a,b,c,n,x;
	cin>>n>>x;
	vector<int> t;
	t.clear();
	REP(i,n){
		cin>>a;
		t.push_back(a);
	}
	sort(t.begin(),t.end());
	int cnt=0;
	j=0;k=n-1;
	while(j<k){
		while(k>j && t[j]+t[k]>x){
			k--;cnt++;
		}
		while(k>j && t[j]+t[k]<=x){
			j++;k--;cnt++;
		}
	}
	if(k==j)
		cnt++;
	return cnt;
}