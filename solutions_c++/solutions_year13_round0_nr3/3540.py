#include <iostream>
#include <vector>
#include <map>
#include <cstdio>
#include <cmath>

using namespace std ;

#define forsn(i, s, n) for (tint i = s ; i < n ; i++)
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
#define DBG(x) cout<<#x<<' '<<x<<endl;
#define RAYA cout<<"-------------"<<endl;

typedef long long tint;

bool espal(tint n){
	if(n==0)return true;
	tint pot=1;
	while(n>=pot)pot*=10;
	pot/=10;
	if(n/pot==n%10)return espal((n-(n/pot)*pot)/10);
	return false;
}



int main()
{
	vector <tint> w;
	forn(i,100000000)if(espal(i) && espal(i*i))w.pb(i*i);
	int t,a,b;
	cin>>t;
	forn(caso,t){
		int res=0;
		cin>>a>>b;
		fore(i,w)if(a<=w[i] && w[i]<=b)res++;
		cout<<"Case #"<<1+caso<<": "<<res<<endl;
	}
}


