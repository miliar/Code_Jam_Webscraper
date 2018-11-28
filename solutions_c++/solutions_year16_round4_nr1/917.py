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

int p,r,s,n;

string gen(char c, int dep){
	string ret;
	if(dep==0){
		ret=" ";
		ret[0]=c;
		return ret;
	}
	char c1=c,c2;
	if(c=='P')c2='R';
	if(c=='R')c2='S';
	if(c=='S')c2='P';
	string temp[2]={gen(c1,dep-1),gen(c2,dep-1)};
	sort(temp,temp+2);
	return temp[0]+temp[1];
}

void solve(int prim){
	cin>>n >> r >> p >> s;
	string rez[3];
	rez[0]=gen('P',n);
	rez[1]=gen('S',n);
	rez[2]=gen('R',n);
	FOR(i,3){
		int trr=0,trs=0,trp=0;
		FOR(j,(1<<n)){
			if(rez[i][j]=='P')trp++;
			if(rez[i][j]=='R')trr++;
			if(rez[i][j]=='S')trs++;
		}
		if(trp!=p || trs!=s || trr!=r)rez[i]="Z";
	}
	sort(rez,rez+3);
	if(rez[0]=="Z")rez[0]="IMPOSSIBLE";
	cout << "Case #"<<prim<<": "<<rez[0]<<"\n";
}

int main(){
	int n;
	scanf("%d",&n);
	FORR(i,1,n+1)solve(i);
	return 0;
}
