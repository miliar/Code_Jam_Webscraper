#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>
#include <string>
using namespace std;

typedef pair<int,int> pii;
typedef vector<int,int> vii;
#define ll long long
const int MaxN = 200005;
const double eps = 1e-7;
const double DINF = 1e100;
const int INF = 1000000006;
const ll LINF = 1000000000000000005ll;

int n;
double C,F,X;
int main(){
	#ifndef ONLINE_JUDGE
	    freopen("in.txt","r",stdin);
	    freopen("out.txt","w",stdout);
	#endif
	 cin>>n;
	 for (int u = 1; u <= n; ++u){
	 	 cin>>C>>F>>X;
	 	 double cook=0.0;
	 	 double prod=2.0;
	 	 double T=0.0;
	 	 double acumAnt=X;
	 	 double nuevoT=X;
	 	 do{
	 	 	acumAnt=nuevoT;
	 	 	double second=C/prod;
	 	 	double str=X/prod;
	 	 	prod+=F;
	 	 	nuevoT=T+str;
	 	 	T+=second;
	 	 }while(acumAnt>nuevoT);
	 	 printf("Case #%d: %.7f\n",u,acumAnt);
	 }
	return 0;
}