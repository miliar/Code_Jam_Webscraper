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
int n,t,res,x,l;
int A[5][5];
string cad,s;
bool ok;
char  *C;
int getvalue(char value){
	if(value == 1) return 1;
	if(value == 'i') return  2;
	if(value == 'j')return 3;
	if(value == 'k') return 4;
	return -1;
}
int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.in.out","w",stdout);
	ios_base::sync_with_stdio(0);
	A[1][1] = 1;
	A[1][2] = A[2][1] = 2;
	A[1][3] = A[3][1] = 3;
	A[1][4] = A[4][1] = 4;
	A[2][2]=A[3][3]=A[4][4]=-1;
	A[2][3] = 4;
	A[2][4] = -3;
	A[3][2] = -4;
	A[3][4] = 2;
	A[4][2] = 3;
	A[4][3] = -2;
	cin>>t;
	A[0][0] = 0;
	for(int w=1;w<=t;w++){
		cin>>x>>l;
		cin>>cad;
		s = "";
		for(int i=1;i<=l;i++)
			s+=cad;
		ok = false;
		n = s.length();
		bool isI = false;
		bool isK = false;
		int ini = 1;
		int neg = 0;
		for(int i = 0; i < n;i++){
			int v = A[ini][getvalue(s[i])];
			if(v < 0) neg = (neg + 1)%2;
			v = abs(v);
			if(v == 2 && neg == 0){
				isI = true;
			}else if(v == 4 && neg == 0 && isI){
				isK = true;
			}
			ini = v;
			//cout<<ini<<" "<<neg<<endl;
		}
		if(neg) ini*=-1;
		if(isK && ini == -1){
			C = "YES";
		}else
		    C = "NO";
		printf("Case #%d: %s\n",w,C);
	}
	return 0;
}
