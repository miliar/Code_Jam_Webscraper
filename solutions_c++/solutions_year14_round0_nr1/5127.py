#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
using namespace std;
 
#define ll long long
#define ld long double
#define Fox(i,n) for (i=0; i<n; i++)
#define Fox1(i,n) for (i=1; i<=n; i++)
#define FoxI(i,a,b) for (i=a; i<=b; i++)
#define FoxR(i,n) for (i=n-1; i>=0; i--)
#define FoxR1(i,n) for (i=n; i>0; i--)
#define FoxRI(i,a,b) for (i=b; i>=a; i--)
#define Foxen(i,s) for (i=s.begin(); i!=s.end(); i++)
#define Min(a,b) a=min(a,b)
#define Max(a,b) a=max(a,b)
#define sz(s) int((s).size())
#define all(s) (s).begin(),(s).end()
#define FILL(s,v) memset(s,v,sizeof(s))
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define rep(i,a,n) for (int i=a;i<(int)n;i++)
#define per(i,a,n) for (int i=n-1;i>=a;i--)
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> PII;
typedef pair<ll,ll> PLL;
typedef vector<ll> vl;
const ll mod=1000000007;
const double eps=1e-9;
const double pi=acos(0)*2;

int main()
{
int t,n,m,a[5][5],b[5][5],k=1;
cin>>t;
while(t-->0)
{
	vector <int> v1;
	vector <int> v2;
	v1.clear();
	v2.clear();
	set <int> s;
	cin>>n;
	rep(i,0,4)
	{
		rep(j,0,4)
		{
			cin>>a[i][j];
			if(n==i+1)
			{
				v1.pb(a[i][j]);
				s.insert(a[i][j]);
			}
		}
	}

	cin>>m;
	rep(i,0,4)
	{
		rep(j,0,4)
		{
			cin>>b[i][j];
			if(m==i+1)
			{
				v2.pb(b[i][j]);
				s.insert(b[i][j]);
			}
		}
	}	
	if(s.size()<7)
	cout<<"Case #"<<k<<": "<<"Bad magician!"<<endl;
	else if(s.size()==8)
	cout<<"Case #"<<k<<": "<<"Volunteer cheated!"<<endl;
	else if(s.size()==7)
	{
		rep(i,0,v1.size())
		if(find(all(v2),v1[i])!=v2.end())
		cout<<"Case #"<<k<<": "<<v1[i]<<endl;
	}
	k++;
}
}
