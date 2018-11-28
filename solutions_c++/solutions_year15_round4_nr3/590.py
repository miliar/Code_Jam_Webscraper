#include <cstdio>
#include <cstring>
#include <map>
#include <string>
#include <vector>
#include <iostream>

using namespace std;
#define rep(i,l,r) for (int i=(l);i<=(r);i++)

const int inf=~0u>>1;
const int maxn=100400;
map<string,int > M;
map<string,int > S;
int s[6000],s2[6000];
char str[maxn];
vector<int> V[202];
int ans,n;

int main() {
	freopen("c.in","r",stdin);
	//freopen("c.out","w",stdout);
	int T;scanf("%d\n",&T);
	rep(t,1,T) {
		memset(s2,0,sizeof s2);
		memset(s,0,sizeof s);
		printf("Case #%d: ",t);
		scanf("%d\n",&n);
		M.clear();
		int len;
		char* ptr;
		S.clear();
		int tot=0;
		rep(i,1,2) {
			V[i].clear();
			len=strlen(gets(str));
			for (ptr=strtok(str," ");ptr!=NULL;ptr=strtok(NULL," ")) {
				int tmp=M[string(ptr)];
				if (tmp==0)
					tmp=M[string(ptr)]=++tot;
				V[i].push_back(tmp);
				s[tmp]|=i;
			}
		}
		rep(i,3,n) {
			V[i].clear();
			len=strlen(gets(str));
			for (ptr=strtok(str," ");ptr!=NULL;ptr=strtok(NULL," ")) {
				int tmp=M[string(ptr)];
				if (tmp==0)
					tmp=M[string(ptr)]=++tot;
				V[i].push_back(tmp);
			}
		}
		rep(i,1,tot) s2[i]=s[i];
		if (n==2) {
			ans=0;
			rep(i,1,tot)
				if (s[i]==3)
					ans++;
			printf("%d\n",ans);
			continue;
		}
		ans=inf;
		rep(i,0,(1<<(n-2))-1) {
			rep(k,1,tot)
				s[k]=s2[k];
			rep(j,3,n) {
				int p=(i>>(j-3))&1;
				for (const auto &k : V[j])
					s[k]|=(1<<p);
			}
			int tmp=0;
			rep(k,1,tot)
				if (s[k]==3)
					tmp++;
			if (ans>tmp) ans=tmp;
		}
		printf("%d\n",ans);
	}
	return 0;
}

