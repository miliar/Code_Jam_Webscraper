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
typedef vector< vi > matrix;

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

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);	freopen("respuestaA-S.out", "w", stdout);	
//	freopen("A-large.in", "r", stdin);	freopen("respuestaA-L.out", "w", stdout);

	int T, r, t;
	cin>>T;
    fornm(tc,1,T)
    {
    	cin >> r >> t;
    	int i = 0;
    	int A = 0;
    	for(i;;i++)
    	{
    		A += 2*r + 2*(2*i+1)-1;
    		if(A > t)break;
    	}
      cout<<"Case #"<<tc<<": "<<i<<endl;
	}
	return 0;
}

