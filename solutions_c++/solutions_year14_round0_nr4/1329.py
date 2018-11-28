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

double a[10000], b[10000];

bool allok_b(li n, li x){
	rep(i,n-x){
		if(a[i]>=b[i+x])return false;
	}
	return true;
}



li war(li n){
	li x=0;
	while(!allok_b(n, x)){
		x++;
	}
	return x;
}

bool allok(li n, li x){
	rep(i,n-x){
		if(a[i+x]<=b[i])return false;
	}
	return true;
}

li dwar(li n){
	li x=0;
	while(!allok(n, x)){
		x++;
	}
	return n-x;
}

int main(){
	li cases;
	cin>>cases;
	rep(i,cases){
		li x,y;
		li n;
		cin>>n;
		rep(j,n){cin>>a[j];}
		rep(j,n){cin>>b[j];}
		sort(a, a+n);
		sort(b, b+n);
		//rep(j,n)p3("",a[j], b[j]);
		y=war(n);
		x=dwar(n);

		printf("Case #%I64d: %I64d %I64d\n", i+1, x, y);
	}

	return 0;
}