#include <iostream>
#include <vector>
#include <map>
#include <math.h>
#include <cmath>
#include <set>
#include <algorithm>
#include <stack>
#include <stdio.h>
#include <string>
using namespace std;

#define forsn(i,s, n) for(int i=(int)s; i<(int)(n); i++)
#define forn(i, n) forsn(i,0,n)
#define fore(i,n) forn(i,n.size())
#define fori(i, n) for(typeof n.begin() i=n.begin(); i!=n.end();i++)
#define RAYA cout<<"-----------------"<<endl;
#define dbg(x) cout<<#x<<":"<<(x)<<endl;

typedef long long int tint;
typedef long double ldouble;
typedef  pair <tint,tint> pii;
typedef  pair <string,string> pss;
typedef  pair <tint,pii> piii;
typedef  pair <piii,pss> piiiss;

#define pb push_back
#define mp make_pair
#define f first
#define s second
#define all(n) n.begin(),n.end()

const tint INF=2000000000;

double tab[300][300];



int main(){
	int T;
	cin>>T;
	forn(caso,T){
		int N,K; cin>>N>>K;
		vector<double> list(N);
		double res=0;
		forn(i,N)cin>>list[i];
		sort(all(list));
		vector<double> l (K);
		forn(i,K)l[i]=list[i];
	
		forn(i,300)forn(j,300)tab[i][j]=0;
		tab[0][0]=l[0];
		tab[0][1]=1-l[0];
		forsn(i,1,K){
			tab[i][0]=tab[i-1][0]*l[i];
			forsn(j,1,i+2) tab[i][j]=tab[i-1][j]*l[i]+tab[i-1][j-1]*(1-l[i]);
		}
		res=max(res,tab[K-1][K/2]);

		forn(kk,K){
			l[K-1-kk]=list[N-1-kk];
			int sum=-0;
			forn(i,K)sum+=l[i];
				
			forn(i,300)forn(j,300)tab[i][j]=0;
			tab[0][0]=l[0];
			tab[0][1]=1-l[0];
			forsn(i,1,K){
				tab[i][0]=tab[i-1][0]*l[i];
				forsn(j,1,i+2) tab[i][j]=tab[i-1][j]*l[i]+tab[i-1][j-1]*(1-l[i]);
			}
			res=max(res,tab[K-1][K/2]);
		}
		
		cout<<"Case #"<<caso+1<<": ";
		printf ("%.10f",res);
		cout<<endl;
	}
    return 0;
}
