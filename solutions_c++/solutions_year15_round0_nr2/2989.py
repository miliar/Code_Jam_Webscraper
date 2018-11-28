#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <algorithm>
#include <deque>
#include <vector>
#include <map>
#include <cmath>
#include <cstdlib>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <cstring>
#include <climits>
#include <ctype.h>
#include <utility>
using namespace std;

#define ft first
#define sd second
#define pb push_back
#define endl '\n'
#define cpy(a,e) memcpy(a,e,sizeof(e))
#define clr(a,e) memset(a,e,sizeof(a))
#define rep(i,n) for (int (i)=0;(i)<(n);i++)
#define repd(i,n) for (int (i)=(n)-1;(i)>=0;i--)
#define reps(i,s,e) for (int (i)=(s);(i)<=(e);i++)
#define repds(i,s,e) for (int (i)=(s);(i)>=(e);i--)

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	ifstream fin;
	fin.open("in.txt");
	ofstream fout;
	fout.open("out.txt");
	int t;
	fin >> t;
	rep(k,t) {
		int n,x,p[1055],ans=INT_MAX,u=0;
		fin >> n;
		rep(i,n) fin >> p[i],u=max(u,p[i]);
		reps(i,1,u) {
			int m=0;
			rep(j,n) {
				if (p[j]-i<=0) continue;
				int left=p[j]-i;
				m+=(left+i-1)/i;
			}
			m+=i;
			ans=min(ans,m);
		}
		fout << "Case #" << k+1 << ": " << ans << endl;
	}
	return 0;
}

