#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker,"/STACK:100000000000")
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include<complex>

using namespace std;
#define FR(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,c,n) for(int (i)=(c);(i)<(n);(i)++)
#define REP(it,v,cont) for(cont::iterator (it)=(v).begin();(it)!=(v).end();++(it)) 
#define CLR(a,c) memset((a),(c),sizeof (a))
#define ALL(v) (v).begin(),(v).end()
#define SQR(a) ((a)*(a))
typedef long long ll;
typedef unsigned long long  ull;
typedef long double lld;
typedef pair<int,int> PII;
typedef pair<ll,ll> PLL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;

bool can[5][5];
bool can2[5][5];
int n;
int res;

bool f2(string perm,int ind,int mask){
	if(ind==n){
		if(mask==(1<<n)-1) return true;
		return false;
	}
	bool cur=true;
	bool hit=false;
	int worker=perm[ind]-'0';
	FR(i,n)
		if(can2[worker][i] && !(mask&(1<<i))){
			hit=true;
			cur &= f2(perm,ind+1,mask|(1<<i));
		}
	
	if(!hit) return false;
	return cur;
}

bool f(){
	string perm="";
	FR(i,n) perm.push_back(i+'0');
	do{
		if(!f2(perm,0,0)) return false;
	}while(next_permutation(ALL(perm)));
	return true;
}

void bt(int row,int col,int dollar){
	if(col==n){
		if(row!=n-1) {
			bt(row+1,0,dollar);
			return;
		}else{
			//do stuff hereeee

			if(f()) res=min(res,dollar);
			return;
		}
	}
	can2[row][col]=can[row][col];
	bt(row,col+1,dollar);
	if(!can2[row][col]){
		can2[row][col]=true;
		bt(row,col+1,dollar+1);
		can2[row][col]=false;
	}
}

int main(){
	freopen("a.in","r",stdin);	
	freopen("a.out","w",stdout);
	int tt;cin>>tt;
	FR(cas,tt){
		printf("Case #%d: ",cas+1);
		CLR(can,false);
		cin>>n;
		FR(i,n){
			string s;cin>>s;
			FR(j,s.size()) if(s[j]=='1') can[i][j]=true;
		}
		res=1e9;
		bt(0,0,0);
		cout<<res<<endl;
	}
}