#include <iostream>
#include <vector>
#include <map>
#include <math.h>
#include <cmath>
#include <set>
#include <algorithm>
#include <stack>
#include <stdio.h>
using namespace std;

#define forsn(i,s, n) for(int i=(int)s; i<(int)(n); i++)
#define forn(i, n) forsn(i,0,n)
#define fore(i,n) forn(i,n.size())
#define fori(i, n) for(typeof n.begin() i=n.begin(); i!=n.end();i++)
#define RAYA cout<<"-----------------"<<endl;
#define dbg(x) cout<<#x<<":"<<(x)<<endl;

typedef long long int tint;
typedef long double ldouble;
#define pii pair <int,int>

#define pb push_back
#define mp make_pair
#define f first
#define s second

const tint INF=2000000000;


int s[20000];

int main(){
	freopen("CJ1.out","w",stdout);
	int T;
	cin>>T;
	forn(caso,T){
		int n,x; cin>>n>>x;
		forn(i,n)cin>>s[i];
		int pos1=0;
		int pos2=n-1;
		int res=0;
		sort(s,s+n);
		while(pos2>=pos1){
			if(pos2!=pos1 && s[pos2]+s[pos1]<=x) pos1++;
			pos2--;
			res++;		
		}
		cout<<"Case #"<<caso+1<<": "<<res<<endl;
	}
    return 0;
}
