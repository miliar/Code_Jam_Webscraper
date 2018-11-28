#include <iostream>
#include <iomanip>
#include <climits>
#include <stack>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <cassert>

#define FOR(i,n) for(int i=0,_n=n;i<_n;i++)
#define FORR(i,s,n) for(int i=s,_n=n;i<_n;i++)
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

const ll MOD = 1000000007LL;

void solve(int prim){
	string s;
	int k;
	cin>> s >> k;
	int n=0;
	FOR(i,s.length()){
		if(i+k>s.length())break;
		if(s[i]=='+')continue;
		n++;
		FORR(j,i,i+k)if(s[j]=='+')s[j]='-';else s[j]='+';
	}
	FOR(i,s.length())if(s[i]=='-')n=-1;
	if(n==-1)
		cout << "Case #"<<prim<<": IMPOSSIBLE\n";
	else
		cout << "Case #"<<prim<<": "<<n<<"\n";
}

int main(){
	int n;
	scanf("%d",&n);
	FORR(i,1,n+1)solve(i);
	return 0;
}
