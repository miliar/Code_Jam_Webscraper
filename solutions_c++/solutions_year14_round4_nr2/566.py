#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <climits>
#include <cassert>

#define FOR(i,n) for(int i=0,_n=n;i<_n;i++)
#define FORD(i,n) for(int i=n;i>=0;i--)
#define FORR(i,s,n) for(int i=s,_n=n;i<_n;i++)
#define FORRD(i,n,s) for(int i=n,_s=s;i>=_s;i--)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define pli pair<ll,int>
#define vi vector<int>
#define fs first
#define sec second

#define oo 1000000000
#define maxn 2000
using namespace std;
typedef long long ll;

int big_left[maxn],big_right[maxn],a[maxn],is[maxn],n;

bool cmpx(int x,int y){
	return a[x] < a[y];
}
int d[maxn][maxn];
int f(int x,int r){
	if(x == n - 1) return 0;
	if(d[x][r] != -1) return d[x][r];
	
	int &res = d[x][r];
	res = oo;
	res = min(res,f(x + 1,r + 1) + big_right[x]);
	res = min(res,f(x + 1,r) + big_left[x]);
	return res;
}
int main(){
	int T;
	cin>>T;
	FORR(tt,1,T + 1){
		cin>>n;
		FOR(i,n)
		{ 
			cin>>a[i];
			is[i] = i;
			big_left[i] = 0;
			big_right[i] = 0;
		}
		sort(is,is + n,&cmpx);
		
		memset(d,-1,sizeof d);
		FOR(i,n)
			a[is[i]] = i;
		FOR(i,n){
			FORD(j,i - 1)
				if(a[j] > a[i]) big_left[i]++;
			FORR(j,i + 1,n)
				if(a[j] > a[i]) big_right[i]++;
		}
		cout<<"Case #"<<tt<<": "<<f(0,0)<<"\n";
	}
	return 0;
}
