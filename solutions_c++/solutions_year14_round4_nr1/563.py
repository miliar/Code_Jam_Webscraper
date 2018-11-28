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

#define maxn 100000
using namespace std;
typedef long long ll;

int s[maxn];
int main(){
	int T;
	cin>>T;
	FORR(tt,1,T + 1){
		int n,x,ans = 0;
		cin>>n>>x;
		FOR(i,n) cin>>s[i];
		sort(s,s+n);
		
		int l = 0,r = n - 1;
		for(;l <= r;){
			if(l == r){ ans++; break; }
			if(s[l] + s[r] <= x){ l++; r--; ans++; }
			else{ ans++; r--; }
		}
		cout<<"Case #"<<tt<<": "<<ans<<"\n";
	}
	return 0;
}
