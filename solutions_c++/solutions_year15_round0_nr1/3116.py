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
		int n,a[20055];string s;
		fin >> n >> s;
		clr(a,0);n++;
		rep(i,n) a[i]+=s[i]-'0';
		reps(i,1,n*11) a[i]+=a[i-1];
		n--;
		int v=0,ans=0;
		while(v<n) {
			v=a[v];
			if (v>=n) break;
			if (v==a[v]) {
				ans++;v++;
				reps(j,v,n) a[j]++;
			}
		}
		fout << "Case #" << k+1 << ": " << ans << endl;
	}
	return 0;
}

