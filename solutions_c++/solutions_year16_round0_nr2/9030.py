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

bool ok(string s){
	FOR(i,s.length())if(s[i]!='+')return 0;
	return 1;
}

string flip(string s, int p){
	FOR(i,(p+1)/2)swap(s[i],s[p-i]);
	FOR(i,p+1)if(s[i]=='-')s[i]='+';else s[i]='-';
	return s;
}

void solve(int primer){
	string s;
	cin >> s;
	map<string, bool> mem;
	queue<pair<string,int> > q;
	q.push(mp(s,0));
	mem[s]=1;
	while(!ok(q.front().fs)){
		string t=q.front().fs;
		int st=q.front().sec;
		q.pop();
		FOR(i,t.size()){
			string nyu=flip(t,i);
			if(!mem[nyu]){
				mem[nyu]=1;
				q.push(mp(nyu,st+1));
			}
		}
	}
	cout << "Case #"<<primer<<": "<<q.front().sec<<"\n";
}

int main(){
	int n;
	cin >> n;
	FOR(i,n)solve(i+1);
	return 0;
}
