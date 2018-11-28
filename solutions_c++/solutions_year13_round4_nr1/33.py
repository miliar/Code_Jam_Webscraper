#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
typedef pair <int, int> pii;
const int md=1000002013;
int t,tt,n,m,x,i,top,a,b,c,r;
vector <pii> all;
pii s[2020];
long long sum(long long n) {
   return (n*(n-1LL))/2;
}
long long res(long long d) {
  return (sum(n)-sum(n-d))%md;
}
int main() {
  freopen("Al.in","r",stdin);
  freopen("Al.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d%d",&n,&m);
	all.clear();
	for (r=i=0; i<m; i++) {
	  scanf("%d%d%d",&a,&b,&c);
	  all.push_back(make_pair(a,-c));
	  all.push_back(make_pair(b,c));
	  r=(r+c*res(b-a))%md;
	}
	sort(all.begin(),all.end());
	for (top=i=0; i<all.size(); i++) if (all[i].second>0) {
	  while (all[i].second>0) {
	    x=min(s[top].second,all[i].second);
		all[i].second-=x;
		s[top].second-=x;
		r=(r-((x*res(all[i].first-s[top].first))%md)+md)%md;
		if (s[top].second==0) top--;
	  }
	} else s[++top]=make_pair(all[i].first,-all[i].second);
    printf("Case #%d: %d\n",t,r);
  }
  return 0;
}
