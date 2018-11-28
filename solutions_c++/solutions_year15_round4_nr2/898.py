// Created by alex_mat21. And it works!

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <sstream>
#include <stdio.h>
#include <math.h>
#include <bitset>
#include <string> 
#include <iomanip>
#include <cmath>
#include <utility>
 
#define FOR(i,n) for(int i=0,_n=n;i<_n;i++)
#define FORR(i,s,n) for(int i=s,_n=n;i<_n;i++)
#define mp make_pair
#define vi vector<int>
#define fs first
#define sd second
#define pii pair<int,int>

using namespace std;

int main (){
int t111;
cin >> t111;
int n;
double r[101];
double c[101];
double t,rt,lt,t0,v1,v,x;
int u;

double con=0.00000001;

for (int i111=0 ; i111<t111; i111++){
	cin >> n >> v >> x;
	FOR(i,n)
		cin >> r[i] >> c[i];
	lt=-1;
	rt=0;
	if (n>1 && c[0]>c[1]){
		t=c[0];
		c[0]=c[1];
		c[1]=t;
		t=r[0];
		r[0]=r[1];
		r[1]=t;
		}
	FOR(i,1){ // !!!
		t0=v/r[i];
		if (t0>rt)
			rt=t0;
		}
	u=1;
	rt+=10;
	if (n==1){
		if (c[0]!=x)
			u=0;
		else{
			t=v/r[0];
			}
		//cout << u << endl;
		}
	else if (c[0]>x || c[1]<x) {
		u=0;
		}
	else if (c[0]==c[1]){
		t=v/(r[0]+r[1]);
		}
	else if (c[0]==x)
		t=v/r[0];
	else if (c[1]==x)
		t=v/r[1];
	else {
		/*while (lt+con<rt){
			t=lt+(rt-lt)/2;
			if ((c[1]-x)*v < (c[1]-c[0])*r[0]*t)
				rt=t;
			else
				lt=t;
			}*/
		t=(v*(c[1]-x))/(r[0]*(c[1]-c[0]));
		v1=v-r[0]*t;
		
		if (v1>=0){
			t0=v1/r[1];
			//cout << v*x << ' ' << c[0]*r[0]*t + c[1]*r[1]*t0 << endl;
			if (t0>t)
				t=t0;
			}
		else
			u=0;
		/*if (t<-con || t*r[0]>v)
			u=0;
		else if (v-r[0]*t>r[1]*t){
			t=(v-r[0]*t)/r[1];
			}*/
		}
	cout.setf( std::ios::fixed, std:: ios::floatfield );
	if (u==1)
		cout << "Case #"<< i111 +1 << ": " << setprecision(10) << t << endl;
	else
		cout << "Case #"<< i111 +1 << ": IMPOSSIBLE"<< endl;
	}
return 0;
}
