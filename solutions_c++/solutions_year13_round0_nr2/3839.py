#include <iostream>
#include <vector>
#include <map>
#include <cstdio>
#include <cmath>

using namespace std ;

#define forsn(i, s, n) for (int i = s ; i < n ; i++)
#define forn(i, n) forsn(i, 0, n)
#define fore(i, n) forn(i, n.size())
#define fori(i, n) for (typeof (n.begin()) i = n.begin() ; i != n.end() ; i++)
#define all(n) n.begin(), n.end()
#define pb push_back

#define x first
#define y second


#define eps 0.0001
#define INF 1000000
#define mp make_pair
#define dbg(x) cout<<#x<<' '<<x<<endl

typedef long double ldouble;

int tab[128][128];
int main()
{
	int t,n,m;
	cin>>t;
	forn(caso,t){
		cin>>n>>m;
		forn(i,n)forn(j,m)cin>>tab[i][j];
		bool flag=true;
		forn(i,n)forn(j,m){
			bool flagF=true;
			bool flagC=true;
			forn(k,n)if(tab[k][j]>tab[i][j])flagF=false;
			forn(k,m)if(tab[i][k]>tab[i][j])flagC=false;
			if(!flagF && !flagC)flag=false;
		}
		cout<<"Case #"<<1+caso<<": ";
		if(flag)cout<<"YES"<<endl;
		else cout<<"NO"<<endl;
	}
}


