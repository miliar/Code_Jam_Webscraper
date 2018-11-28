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

int num[27];
string arr[]={"ZERO","ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

string rec(int ps){
	if(ps>=10){
		FOR(i,26)if(num[i]!=0)return "X";
		return "";
	}
	string ret=rec(ps+1);
	if(ret!="X")return ret;
	bool ok=1;
	FOR(j,arr[ps].length())
		if(num[arr[ps][j]-'A']<=0)ok=0;
	if(!ok)return "X";
	FOR(j,arr[ps].length())
		num[arr[ps][j]-'A']--;
	ret=rec(ps);
	FOR(j,arr[ps].length())
		num[arr[ps][j]-'A']++;
	if(ret=="X")return ret;
	else return (char)(ps+'0')+ret;
}


void solve(int prim){
	cout << "Case #"<<prim<<": ";
	string s;
	cin >> s;
	memset(num,0,sizeof(num));
	FOR(i,s.length())num[s[i]-'A']++;
	cout << rec(0)<<"\n";
}

int main(){
	int n;
	scanf("%d",&n);
	FORR(i,1,n+1)solve(i);
	return 0;
}
