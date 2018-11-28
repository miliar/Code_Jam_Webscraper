/*#include <cstdio>
#include <cmath>
#include <vector>
using namespace std;
__int64 a,b;
int T,Ti;
vector <int> ans;
int pal(__int64 d){
	int a[100];
	__int64 md=d;
	memset(a,0,sizeof(a));
	int ni;
	for(ni=0;;ni++) {
		if(md==0) break;
		a[ni]=md%10;
		md/=10;
	}
	int i;
	for(i=0;i<ni/2;i++) {
		if(a[i]!=a[ni-i-1]) return 0;
	}
	return 1;
}
int main() {
	__int64 i;
	freopen("output.txt","wt",stdout);
	for(i=1;i<=10000000;i++) {
		if(pal(i*i) && pal(i)) {
			ans.push_back(i);
		}
	}
	printf("%d\n",ans.size());
	for(i=0;i<ans.size();i++) {
		printf("%d\n",ans[i]);
	}
	return 0;
}
*/
#include <cstdio>
#include <cmath>
int dbb[100];
int dn;
int T,Ti;
int main() {
	FILE *db=fopen("db.txt","rt");
	fscanf(db,"%d",&dn);
	int di;
	for(di=0;di<dn;di++) {
		fscanf(db,"%d",&dbb[di]);
	}
	freopen("input.txt","rt" ,stdin);
	freopen("output.txt","wt",stdout);
	scanf("%d",&T);
	__int64 a,b;
	for(Ti=1;Ti<=T;Ti++) {
		scanf("%I64d%I64d",&a,&b);
		int sp,ep;
		sp=sqrt(a);
		if(a>sp*sp) sp++;
		ep=sqrt(b);
		int i,cnt=0;;
		for(i=0;i<dn;i++) {
			if(sp<=dbb[i] && dbb[i]<=ep) cnt++;
		}
		printf("Case #%d: %d\n",Ti,cnt);
	}
}