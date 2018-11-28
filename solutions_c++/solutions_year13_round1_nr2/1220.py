#include<cstdio>
#include <cctype>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include <deque>
#include <math.h>
#include<stdio.h>
#include<memory.h>
using namespace std;


typedef stringstream ss;
typedef vector<string> vs;
typedef vector<int> vi;
typedef long long int64;
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;


#define pb push_back
#define fornm(i,n,m) for (int i=n; i<=(int)(m); i++)
#define forn(i,n) for (int i=0; i<(int)(n); i++)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define pb push_back
#define all(v) v.begin(),v.end()
#define sort(c) sort(all(c))
#define reverse(c) reverse(all(c))
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
#define ordC(v,cpm) qsort( (void *)&v[0], v.size(), sizeof( v[ 0 ] ), cpm )

const int oo = (int) 1e9;
const double PI = 2 * acos(0);
const double eps = 1e-9;

int dx[]={1,1,0,-1},dy[]={0,1,1,1};
#define MAXIMO 10000
int64 E,R,N;
vector<int64> v,resp;
void solve(int res, int pos, int sum)
{
	forn(i,res+1)
	{
		int r = (res-i)+R;
		if(r>E)r=E;
		if(pos==(N-1))
		{
		resp.pb(sum + v[pos]*i);
		}
		else
	 		solve(r,pos+1,sum + v[pos]*i);
    }
 	
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);	freopen("respuestaB-S.out", "w", stdout);	
//	freopen("B-large.in", "r", stdin);	freopen("respuestaB-L.out", "w", stdout);

	int T;
	
    cin>>T;
    fornm(tc,1,T)
    {
    	cin >> E >> R >> N;
    	v.clear();
    	int64 ll;
    	forn(i,N)
    	{
    		cin >> ll;
    		v.pb(ll);
    	}
    	int64 sum = 0;
    	if(E==R){
    		for(int64 i=0;i<N;i++)
    		  sum += E*v[i];
    		cout<<"Case #"<<tc<<": "<<sum<<endl;
    	}
    	else
    	{
    	   resp.clear();
    	   solve(E,0,0);
    	   int64 max= -1;
    	   forn(i,resp.size())
    	    if(max<resp[i])
    	     max=resp[i];
    	cout<<"Case #"<<tc<<": "<<max<<endl;
    	}
      
	}
	return 0;
}

