#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <ctime>
#include <map>
#define fi first
#define se second
#define PA pair<int,int>
#define VI vector<int>
#define VP vector<PA >
#define mk(x,y) make_pair(x,y)
#define N 10010
#define For(i,x,y) for (i=x;i<=y;i++)
using namespace std;
int i,j,k,n,m,te,T,t,nn,an;
char p[N];
map<string,int> a;
VI b[N];
int main() {
	//freopen("bil.in","r",stdin);
	//freopen("bil.out","w",stdout);
	scanf("%d",&T);
	For(te,1,T) {
		scanf("%d",&n); gets(p);
		a.clear(); t=0;
		For(j,1,n) {
			gets(p+1);
			m=strlen(p+1);
			for (i=1;i<=m;) {
				for (;i<=m&&p[i]==' ';i++);
				if (i>m) break;
				string s;
				for (;i<=m&&p[i]!=' ';i++) s+=p[i];
				if (!a.count(s)) a[s]=++t;
				b[a[s]].push_back(j);
			}
		}
		nn=(1<<n)-1; an=N;
		For(i,1,nn) if ((i&3)==1) {
			int s=0;
			For(j,1,t) {
				int F=0;
				for (k=0;k<b[j].size();k++) {
					int A=b[j][k];
					F|=(i>>A-1)&1?1:2;
					if (F==3) break;
				}
				s+=F==3;
				if (s>an) break;
			}
			an=min(an,s);
		}
		printf("Case #%d: %d\n",te,an);
		For(i,1,t) b[i].clear();
		cerr<<te<<endl;
	}
	return 0;
}
