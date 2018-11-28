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

#define forsn(i,s,n) for(int i=(int)s; i<(int)(n); i++)
#define forn(i,n) forsn(i,0,n)
#define fore(i,n) forn(i,n.size())
#define fori(i,n) for(typeof n.begin() i=n.begin(); i!=n.end();i++)
#define RAYA cout<<"-----------------"<<endl;
#define dbg(x) cout<<#x<<":"<<(x)<<endl;

typedef long long int tint;
typedef  pair <tint,tint> pii;

#define pb push_back
#define mp make_pair
#define f first
#define s second
#define all(n) n.begin(),n.end()

const double eps=0.000001;


double x[10000];
double y[10000];
double z[10000];
bool visi[10000];

int n;

double sq(double t){
	return t*t;
}

double dist(int a,int b){
	return sqrt(sq(x[a]-x[b])+sq(y[a]-y[b])+sq(z[a]-z[b]));
}

void bfs(int a, double d){
	visi[a]=true;
	forn(i,n)if(!visi[i])if(dist(a,i)<d)bfs(i,d);
	return;
}

int main(){
	int T;
	cin>>T;
	int q;
	forn(caso,T){
		cin>>n;
		int s; cin>>s;
		forn(i,n){
			cin>>x[i]>>y[i]>>z[i];
			cin>>q>>q>>q;
		}
		double mx=10000;
		double mn=0;
		while(mx-mn>eps){
			double mid=(mx+mn)/2;
			forn(i,n)visi[i]=false;
			bfs(0,mid);
			if(visi[1]){
				mx=mid;
			}else{
				mn=mid;
			}
		}
		cout<<"Case #"<<caso+1<<": ";
		printf ("%.10f",mx);
		cout<<endl;
	}
    return 0;
}
