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

#define maxn 1000
using namespace std;
typedef long long ll;

int n,m,X,Y;
int to[maxn];
string S[maxn];

// trie
int nxt[10][1000][30];
bool root[10];
int cnt[10];

void calc(){
	memset(nxt,0,sizeof nxt);
	memset(root,0,sizeof root);
	memset(cnt,0,sizeof cnt);
	
	int ans = 0;
	FOR(i,m){
		if(!root[to[i]]){ ans++; root[to[i]] = true; }
		
		int type = to[i];
		int curr = 0;
		
		FOR(j,S[i].length()){
			if(nxt[type][curr][S[i][j] - 'A'] == 0){
				nxt[type][curr][S[i][j] - 'A'] = ++cnt[type];
				ans++;
			}
			curr = nxt[type][curr][S[i][j] - 'A'];
		}
	}
	if(ans > X){ X = ans; Y = 1; }
	else if(ans == X) Y++;
}
void fkk(int x){
	if(x == m){ calc(); return; }
	FOR(i,n)
	{
		to[x] = i;
		fkk(x + 1);
	}
}

int main(){
	int T;
	cin>>T;
	FORR(tt,1,T + 1){
		cin>>m>>n;
		X = Y = 0;
		FOR(i,m)
			cin>>S[i];
		fkk(0);
		
		cout<<"Case #"<<tt<<": "<<X<<" "<<Y<<"\n";
	}
	return 0;
}
