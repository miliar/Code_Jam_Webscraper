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
#include <memory.h>

using namespace std;

int mod=1000002013;
int a[1001],b[1001],p[1001];

struct item {
	int l,r,cnt;
};

bool operator < (const item & a,const item & b) {
	return a.l<b.l||a.l==b.l&&a.r<b.r;
}

int get(int n,int d) {
	return 1LL*(n-d+1+n)*d/2%mod;
}

int getX(vector <int> & x,int val) {
	return lower_bound(x.begin(),x.end(),val)-x.begin();
}

void doTest() {
	int n,m;
	scanf("%d%d",&n,&m);
	int total=0;
	for(int i=0;i<m;++i) {
		scanf("%d%d%d",&a[i],&b[i],&p[i]);
//		--a[i]; --b[i];
		total=(total+1LL*p[i]*get(n,b[i]-a[i]))%mod;
	}
/*	vector <int> x;
	for(int i=0;i<m;++i) {
		x.push_back(a[i]);
		x.push_back(b[i]);
	}
	sort(x.begin(),x.end());
	x.resize(unique(x.begin(),x.end())-x.begin());
*/	vector <item> v;
	set <item> f;
	for(int i=0;i<m;++i) {
//		item it={getX(x,a[i]),getX(x,b[i]),p[i]};
		item it={a[i],b[i],p[i]};
		v.push_back(it);
		f.insert(it);
	}
//	sort(v.begin(),v.end());
	int cur=0;
	/*set <item>::iterator it,it1;
	while(!f.empty()) {
		item top=*f.begin();
		f.erase(f.begin());
		bool was=false;
		for(it=f.begin();top.cnt&&it!=f.end();++it) {
			if (it->cnt==0) continue;
			if (it->l!=top.l&&it->l<=top.r&&it->r>top.r) {
				was=true;
				int go=min(top.cnt,it->cnt);
				top.cnt-=go;
				item tmp={it->l,it->r,it->cnt-go};
				f.erase(it);
				f.insert(tmp); it=f.find(tmp);
				item it1={top.l,it->r,go},it2={it->l,top.r,go};
				f.insert(it1);
				f.insert(it2);
			}
		}
		if (!was) {
			cur=(cur+1LL*get(n,top.r-top.l)*top.cnt)%mod;
		} else if (top.cnt) f.insert(top);
	}*/
	while(true) {
		bool was=false;
		for(int i=0;i<v.size();++i)
			if (v[i].cnt)
			for(int j=0;j<v.size();++j) {
				if (i!=j&&v[i].cnt&&v[j].cnt) {
					if (v[j].l>v[i].l&&v[j].l<=v[i].r&&v[j].r>v[i].r) {
						int go=min(v[i].cnt,v[j].cnt);
						v[i].cnt-=go;
						v[j].cnt-=go;
						item it1={v[i].l,v[j].r,go},it2={v[j].l,v[i].r,go};
						v.push_back(it1);
						v.push_back(it2);
						was=true;
					}
				}
			}
		if (!was) break;
	}
	for(int i=0;i<v.size();++i)
		cur=(cur+1LL*v[i].cnt*get(n,v[i].r-v[i].l))%mod;
	cout << (total-cur+mod)%mod;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;++test) {
		printf("Case #%d: ",test);
		doTest();
		printf("\n");
	}
	return 0;
}
