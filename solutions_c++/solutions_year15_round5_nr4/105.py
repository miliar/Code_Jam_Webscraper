#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <set>
#include <vector>
using namespace std;

#define mp(x, y) make_pair((x), (y))

typedef long long ll;

int t;
int p;
vector<int> e, f;
int n;
int s;
map<int,int> ps;
vector<int> ans;

int main()
{
	scanf("%d", &t);

for(int q=1; q<=t; q++) {
	scanf("%d", &p);
	e.clear();
	e.resize(p);
	f.clear();
	f.resize(p);
	for(int i=0; i<p; i++) scanf("%d", &e[i]);
	for(int i=0; i<p; i++) scanf("%d", &f[i]);
	s=0;
	for(int i=0; i<p; i++) s+=f[i];
	n=1;
	while((1<<n)!=s) n++;
	ps.clear();
	for(int i=0; i<p; i++) {
		ps[e[i]]=f[i];
	}
	ans.clear();
	ps[0]--;
	map<int,int>::iterator it=ps.begin();
	while(it!=ps.end()) {
		while(it->second==0) it++;
		int next=it->first;
		for(int m=0; m<(1<<ans.size()); m++) {
			int s=next;
			for(int j=m, k=0; j>0; j>>=1, k++) {
				if(j&1) {
					s+=ans[k];
				}
			}
			ps[s]--;
		}
		ans.push_back(next);
		while(it->second==0) it++;
	}

	printf("Case #%d:", q);
	for(int i=0; i<n; i++) printf(" %d", ans[i]);
	printf("\n");
}

	return 0;
}
