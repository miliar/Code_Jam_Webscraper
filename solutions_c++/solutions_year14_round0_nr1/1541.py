#include<iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#define _USE_MATH_DEFINES
#include <math.h>
#include<string>
#include<vector>
#include<cmath>
#include<stack>
#include<queue>
#include<sstream>
#include<algorithm>
#include<map>
#include<complex>
#include<ctime>
#include<set>
using namespace std;


#define li			long long int
#define rep(i,to)	for(li i=0;i<((li)(to));i++)
#define repp(i,start,to)	for(li i=(li)(start);i<((li)(to));i++)
#define pb			push_back
#define sz(v)		((li)(v).size())
#define bgn(v)		((v).begin())
#define eend(v)		((v).end())
#define allof(v)	(v).begin(), (v).end()
#define dodp(v,n)		memset(v,(li)n,sizeof(v))
#define bit(n)		(1ll<<(li)(n))
#define mp(a,b)		make_pair(a,b)
#define rin	rep(i,n)
#define EPS 1e-10
#define ETOL 1e-8
#define MOD 100000000
#define F first
#define S second
#define p2(a,b)		cout<<a<<"\t"<<b<<endl
#define p3(a,b,c)		cout<<a<<"\t"<<b<<"\t"<<c<<endl

int main(){
	li cases;
	cin>>cases;
	rep(i,cases){
		li row[2];
		li card[2][4][4];
		rep(j,2){
			cin>>row[j];
			rep(k,4){
				rep(l,4){
					cin>>card[j][k][l];
				}
			}
		}
		vector<li> v1,v2;
		rep(j,4){
			v1.pb(card[0][row[0]-1][j]);
			v2.pb(card[1][row[1]-1][j]);
		}
		sort(allof(v1));
		sort(allof(v2));

		vector<li> v;
		set_intersection(allof(v1), allof(v2), back_inserter(v));
		cout<<"Case #"<<i+1<<": ";
		//rep(j,sz(v))cout<<v[j]<<" ";puts("");
		if(sz(v)==1)cout<<v[0]<<endl;
		else if(sz(v)>1)cout<<"Bad magician!"<<endl;
		else cout<<"Volunteer cheated!"<<endl;
	}

	return 0;
}