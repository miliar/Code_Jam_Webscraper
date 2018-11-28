//
//  Created by  CQU_CST_WuErli
//  Copyright (c) 2016 CQU_CST_WuErli. All rights reserved.
//
#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <algorithm>
#include <sstream>
#include <cassert>
#define CLR(x) memset(x,0,sizeof(x))
#define OFF(x) memset(x,-1,sizeof(x))
#define MEM(x,a) memset((x),(a),sizeof(x))
#define BUG cout << "I am here" << endl
#define lookln(x) cout << #x << "=" << x << endl
#define SI(a) scanf("%d",&a)
#define SII(a,b) scanf("%d%d",&a,&b)
#define SIII(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define rep(flag,start,end) for(int flag=start;flag<=end;flag++)
#define Rep(flag,start,end) for(int flag=start;flag>=end;flag--)
const int INF_INT=0x3f3f3f3f;
const long long INF_LL=0x7f7f7f7f;
const int MOD=1e9+7;
const double eps=1e-10;
const double pi=acos(-1);
typedef long long  ll;
using namespace std;

struct P
{
	int n;
	int a[60];
	bool operator < (const P& rhs) const {
		int flag=1;
		for (int i=1;i<=n;i++) if (a[i]>=rhs.a[i]) {
			flag=0;break;
		}
		return flag;
	}
	bool operator == (const P& rhs) const {
		for (int i=1;i<=n;i++) if (a[i]!=rhs.a[i]) return false;
		return true;
	}
};
P rec[120];

int flag;
int vis[120];
set<P>::iterator it;
set<P> st;
int n;
P ans;
int t[120][120];
P col[120];

void dfs(int cnt) {
	if (flag) return;
	if (cnt>n) return;
	if (cnt==n) {
		int aa=1;
		for (it=st.begin();it!=st.end();it++) {
			for (int j=1;j<=n;j++)
				t[aa][j]=it->a[j];
			aa++;
		}
		// for (int i=1;i<=n;i++) {
		// 	for (int j=1;j<=n;j++) cout << t[i][j] << ' ';
		// 	cout << endl;
		// }
		// cout << "-------------" << endl;
		P tmp; tmp.n=n;
		aa=1;
		for (int i=1;i<=n;i++) {
			for (int j=1;j<=n;j++) tmp.a[j]=t[j][i];
			col[aa++]=tmp;
		}
		// for (int i=1;i<aa;i++) {
		// 	for (int j=1;j<=n;j++) cout << col[i].a[j] << ' ' ;
		// 	cout << endl;
		// }
		// cout << "+++++++++" << endl;
		int ok=n-1;
		int cc[n+1];
		CLR(cc);
		for (int i=1;i<=2*n-1;i++) if (!vis[i]) {
			for (int j=1;j<aa;j++) if (!cc[j]) {
				if (rec[i]==col[j]) {
					cc[j]=1;
					ok--;
					break;
				}
			}
		}
		if (ok==0) {
			for (int i=1;i<aa;i++) if (!cc[i]) {
				for (int j=1;j<=n;j++) ans.a[j]=col[i].a[j];
				flag=1;
				return;
			}
		}
		return;
	}
	// lookln(cnt);
	for (int i=1;i<=2*n-1;i++) if (!vis[i]) {
		if (!st.size()) {
			vis[i]=1;
			st.insert(rec[i]);
			int sss=st.size();
			dfs(cnt+1);
			st.erase(rec[i]);
			int ttt=st.size();
			vis[i]=0;
		}
		else {
			it=--st.end();
			if (*it<rec[i]) {
				vis[i]=1;
				st.insert(rec[i]);
				dfs(cnt+1);
				vis[i]=0;
				st.erase(rec[i]);
			}
		}
	}
}

int main(int argc, char const *argv[]) {
#ifdef LOCAL
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
#endif
    for (int T_T,kase=SI(T_T);kase<=T_T;kase++) {
    	SI(n);
    	for (int i=1;i<=2*n-1;i++) {
    		rec[i].n=n;
    		for (int j=1;j<=n;j++) SI(rec[i].a[j]);
    	}
    	flag=0;
    	CLR(vis);
    	st.clear();
    	dfs(0);
    	printf("Case #%d: ", kase);
    	for (int i=1;i<=n;i++) {
    		printf("%d", ans.a[i]);
    		if (i<n) printf(" ");
    		else printf("\n");
    	}
    }
	return 0;
}