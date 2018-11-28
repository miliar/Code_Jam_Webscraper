#include <cstdio>
#include <vector>
using namespace std;

int main(){
	int t;
	scanf("%d",&t);
	for(int testcase = 1; testcase <= t; testcase++){
		int n,q,m,ans=0;
		scanf("%d",&n); n--;
		vector<int> first;
		for (int i = 0; i < 4; ++i){
			for (int j = 0; j < 4; ++j){
				scanf("%d",&q);
				if(i==n){
					first.push_back(q);
				}
			}
		}
		scanf("%d",&m); m--;
		for (int i = 0; i < 4; ++i){
			for (int j = 0; j < 4; ++j){
				scanf("%d",&q);
				if(i==m){
					for (int k = 0; k < 4; ++k){
						if(q==first[k]){
							if(ans){
								ans = -1;
							}else{
								ans = q;
							}
						}
					}
				}
			}
		}
		if(ans==-1) printf("Case #%d: Bad magician!\n", testcase);
		else if(!ans) printf("Case #%d: Volunteer cheated!\n", testcase);
		else printf("Case #%d: %d\n", testcase, ans);
	}
	return 0;
}
