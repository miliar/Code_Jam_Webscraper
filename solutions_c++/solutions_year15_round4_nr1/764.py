#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <fstream>
#include <cstring>

using namespace std;
typedef long long LL;

char a[110][110];
int can[110][110];
int dv[4]={1, 2, 4, 8};
int dx[4]={-1, 0, 1, 0};
int dy[4]={0, 1, 0, -1};

int get(char ch) {
	if (ch=='^') return 1;
	if (ch=='>') return 2;
	if (ch=='v') return 4;
	return 8;
}

int main() {
	freopen("pegman.in","r",stdin);
	freopen("pegman.out","w",stdout);
	int tc, nt=1;
	cin>>tc;
	while (tc--) {
		int n, m;
		cin>>n>>m;
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++) cin>>a[i][j];
		memset(can,-1,sizeof(can));
		int ret=0;
		bool is_im=false;
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++) {
				if (a[i][j]=='.') continue;
				can[i][j]=0;
				int c=0;
				bool is_ok=true;
				for (int k=0;k<4;k++) {
					int x=i, y=j;
					bool is_boundary=true;
					while (true) {
						x+=dx[k];
						y+=dy[k];
						if (x<0 || x>=n || y<0 || y>=m) break;
						if (a[x][y]!='.') is_boundary=false;
					}
					if (is_boundary) {
						c|=dv[k];
						is_ok=false;
					}
				}
				if (is_ok) continue;
				int v=get(a[i][j]);
				if (c==15) is_im=1;
				if ((v&c)>0) ret++;
			}
		cout<<"Case #"<<nt++<<": ";
		if (is_im) cout<<"IMPOSSIBLE"<<endl;
		else cout<<ret<<endl;
	}
}
