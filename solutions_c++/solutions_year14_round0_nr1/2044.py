#include <cstdio>
#include <vector>
using namespace std;

int main() {
	int T,n,y;
	vector<int> pool,ans;
	scanf("%d",&T);
	for(int z=1;z<=T;z++) {
		pool.clear();
		ans.clear();
		scanf("%d",&n);
		for(int a=1;a<=4;a++) {
			for(int b=1;b<=4;b++) {
				scanf("%d",&y);
				if(a==n) pool.push_back(y);
			}
		}
		scanf("%d",&n);
		for(int a=1;a<=4;a++) {
			for(int b=1;b<=4;b++) {
				scanf("%d",&y);
				if(a==n) {
					for(int c=0;c<pool.size();c++) if(y==pool[c]) ans.push_back(y);
				}
			}
		}
		printf("Case #%d: ",z);
		if(ans.size()==0) printf("Volunteer cheated!\n");
		else if(ans.size()>1) printf("Bad magician!\n");
		else printf("%d\n",ans[0]);
	}
	return 0;
}
