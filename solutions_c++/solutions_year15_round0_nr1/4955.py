//============================================================================
// Name        : code.cpp
// Author      : vlade087
// Version     : 1.0
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include<stdio.h>
#include<iostream>
#include<sstream>
#include<math.h>
#include<ctype.h>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<string.h>
#include<algorithm>
#include <complex>
#include <numeric>
#include<list>
#include<deque>
#include <stdlib.h>
#define printnVector(R) cout<<R.size()<<endl;for(int i =0;i<R.size();i++) cout<<R[i]<<" ";
#define mod 1000000007
#define inf 9223372036854775807L
#define countbits __builtin_popcount
#define sz sizeof
#define mp make_pair
#define pb push_back
#define ll long long
#define ull unsigned long long
#define mset memset
#define sz sizeof
#define maxn 3200005
#define EPS 1e-9
#define par pair<int,int>
using namespace std;
int n,s,t;
string cad;
bool check(int num){
	int ini = num + cad[0] - '0';
	for(int i = 1; i < cad.length();i++){
		int v = cad[i]-'0';
		if(i > ini) return false;
		ini+=v;
	}
	return true;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.in.out","w",stdout);
	ios_base::sync_with_stdio(0);
	cin>>t;
	for(int w=1;w<=t;w++){
		cin>>s>>cad;
		int res = 0;
		int ini = 0;
		int fin = maxn;
		while(ini<=fin){
			int med = (ini+fin)/2;
			if(check(med)){
				res = med;
				fin = med-1;
			}else
				ini = med+1;
		}
		printf("Case #%d: %d\n",w,res);
	}
	return 0;
}
