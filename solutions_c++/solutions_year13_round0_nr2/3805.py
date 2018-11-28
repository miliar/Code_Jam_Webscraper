#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

struct q{
	int i,j,a;
	q(){}
	q(int _i, int _j, int _a){i = _i; j = _j; a = _a;}
	bool operator < (const q &r) const {
		return a > r.a;
	}
};

int ii[110],jj[110];
int main(){
	freopen("B-large.in","r", stdin);
	freopen("B-large.out","w", stdout);
	int tc;
	scanf("%d", &tc);
	for(int ti = 1; ti <= tc; ti++){
		int n,m;
		scanf("%d%d", &n, &m);
		vector<q> v;

		for(int i = 0; i < n; i++)ii[i] = 0;
		for(int j = 0; j < m; j++)jj[j] = 0;

		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++){
				int a;
				scanf("%d", &a);
				v.push_back(q(i,j,a));
			}
		sort(v.begin(), v.end());
		int pass = 1;
		for(int i = 0; i < v.size(); i++){
			if(ii[v[i].i]>v[i].a && jj[v[i].j]>v[i].a){
				pass = 0;
				break;
			}
			else {
				if(ii[v[i].i]<v[i].a)ii[v[i].i]=v[i].a;
				if(jj[v[i].j]<v[i].a)jj[v[i].j]=v[i].a;
			}
		}
		printf("Case #%d: ", ti);
		if(pass)printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}