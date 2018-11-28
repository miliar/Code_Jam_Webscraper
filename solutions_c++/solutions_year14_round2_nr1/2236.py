#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <numeric>
#include <algorithm>

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <limits.h>

using namespace std;

typedef long long ll;

#define mem(a,b) memset(a,b, sizeof a)
#define SZ(x)	(int)x.size()
#define FOREACH(it,x) for(__typeof((x).begin()) it=(x.begin());it!=(x.end());++it)
#define ERR 1e-7
#define PI (2.0*acos(0))
#define ALL(x) x.begin(),x.end()
#define pb push_back
#define rep(i,n,m) for(int i = (int)n,_m=(int)m;i<_m;++i)
#define bj(stat,b) (stat & (1<<b))
#define bc(stat,b) (stat & (~(1<<b)))
#define vi vector<int> 
#define vs vector<string>

template <class T> T Abs(T x) {return x<0?-x:x;}

int N;

int rec(const string &s1, const string &s2) {
	if(s1==s2) return 0;
	int i=0;
	int j=0;
	bool ok=true;
	int s1_moves = 0;
	int s2_moves = 0;
	int common = 0;
	while(i<SZ(s1) || j<SZ(s2)) {
		if(i<SZ(s1) && j<SZ(s2) && s1[i]==s2[j]) {i++;j++;common++;}
		else if(i>0 && i<SZ(s1) && s1[i]==s1[i-1]) {i++;s1_moves++;}
		else if(j>0 && j<SZ(s2) && s2[j]==s2[j-1]) {j++;s2_moves++;}
		else {ok=false;break;}
	}
	if(!ok) return -1;
	else return s1_moves+s2_moves;
}
string getLcs(const string &s1, const string &s2) {
	int i=0;
	int j=0;
	string ans;
	while(i<SZ(s1) && j<SZ(s2)) {
		if(s1[i]==s2[j]) {ans.pb(s1[i]);i++;j++;}
		else if(i>0 && s1[i]==s1[i-1]) i++;
		else if(j>0 && s2[j]==s2[j-1]) j++;
		else break;
	}
	return ans;
}

int
main()
{
	int T;
	scanf("%d\n",&T);
	for(int t=1;t<=T;t++) {
		cin>>N;
		vs a;
		string tmp;
		rep(i, 0, N) {
			cin>>tmp;
			a.pb(tmp);
			//tmp.resize(distance(tmp.begin(), unique(ALL(tmp))));
			//a.pb(tmp);
		}
		
		int min_=-1;
		//string lcs;
		rep(i,0,N) {
			int ans = 0;
			bool ok=true;
			string lcs(a[i]);
			rep(j,0,N) {
				int cnt = rec(a[i],a[j]);
				lcs = getLcs(lcs,a[j]);
				//printf("%s %s : %d\n",a[i].c_str(),a[j].c_str(),cnt);
				if(cnt==-1) {ok=false;break;}
				else ans += cnt;
			}
			if(ok) {
				int ans2 = 0;
				rep(j,0,N) ans2 += (SZ(a[j])-SZ(lcs));
				if(min_==-1) min_=min(ans,ans2);
				else min_=min(min_,min(ans,ans2));
			}
		}
		printf("Case #%d: ", t);
		if(min_==-1) cout<<"Fegla Won"<<endl;
		else cout<<min_<<endl;
	}
}
