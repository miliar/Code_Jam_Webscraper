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

const int INF=1000000000;


int tab[20000][4];
int d [20000];
int b;

int dist(int i,int j){
	int a=0;
	int b=0;
	if(tab[i][0]>tab[j][2])a=tab[i][0]-tab[j][2];
	if(tab[j][0]>tab[i][2])a=tab[j][0]-tab[i][2];
	if(tab[i][1]>tab[j][3])b=tab[i][1]-tab[j][3];
	if(tab[j][1]>tab[i][3])b=tab[j][1]-tab[i][3];
	//dbg(i);
	//dbg(j);
	//dbg(max(max(a-1,b-1),0));
	return max(max(a-1,b-1),0);	
}


void djk(int s){
	set<pair<int,int> > q;
	d[s] = 0;
	q.insert(mp(0,s));
	while(!q.empty()){
		pair<int,int> ini = *q.begin();
		q.erase(q.begin());
		int n = ini.s;
		forn(i,b+2){
			int ddd = dist(i,n);
			if (d[i] > d[n] + ddd){
				if (d[i] != INF) q.erase(q.find(mp(d[i], i)));
				d[i] = d[n] + ddd;
				q.insert(mp(d[i], i));
			}
		}
	}
}


int main(){
	freopen("CJ3.out","w",stdout);
	int T;
	cin>>T;
	forn(caso,T){
		int w,h;cin>>w>>h>>b;
		tab[0][0]=-1;
		tab[0][1]=0;
		tab[0][2]=-1;
		tab[0][3]=h-1;
		tab[1][0]=w;
		tab[1][1]=0;
		tab[1][2]=w;
		tab[1][3]=h-1;
		forsn(i,2,b+2)cin>>tab[i][0]>>tab[i][1]>>tab[i][2]>>tab[i][3];
		//forn(i,b+2)forn(j,b+2)dist(i,j);
		forn(i,b+2)d[i]=INF;
		djk(0);
		//forn(i,b+2)cout<<d[i]<<endl;
		cout<<"Case #"<<caso+1<<": "<<d[1]<<endl;
	}
    return 0;
}
