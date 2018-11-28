#include<cstdio>
#include<cstring>
#include<set>
#include<vector>

using namespace std;

vector<int> list;
set<int> st;
int T,n,m;
int a[111][111];
bool chk[111][111];

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	scanf("%d",&T);
	for(int cs=1;cs<=T;++cs) {
		memset(chk,0,sizeof(chk));
		scanf("%d%d",&n,&m),st.clear(),list.clear();
		for(int i=0;i<n;++i)
			for(int j=0;j<m;++j)
				scanf("%d",&a[i][j]),st.insert(a[i][j]);
		list.assign(st.begin(),st.end());

		bool can = true;
		for(int x=0;x<list.size();++x) {
			int num = list[x];

			for(int i=0;i<m;++i) {
				if(a[0][i] <= num ) {
					bool go = true;
					for(int j=0;j<n;++j)
						go &= (a[j][i] <= num);
					if(go) for(int j=0;j<n;++j)
						if(a[j][i] == num)
							chk[j][i] = 1;
				}
			}
			for(int i=0;i<n;++i) {
				if(a[i][0] <= num) {
					bool go = true;
					for(int j=0;j<m;++j)
						go &= (a[i][j] <= num);
					if(go) for(int j=0;j<m;++j)
						if(a[i][j] == num)
							chk[i][j] = 1;
				}
			}
			for(int i=0;i<n;++i)
				for(int j=0;j<m;++j)
					if(a[i][j] == num)
						can &= chk[i][j];
		}

		for(int i=0;i<n;++i)
			for(int j=0;j<m;++j)
				can &= chk[i][j];

		if(can) printf("Case #%d: YES\n",cs);
		else printf("Case #%d: NO\n",cs);
	}

	return 0;
}