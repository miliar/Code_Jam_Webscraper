#include <cstdio>
#include <vector>
using namespace std;

int main(){
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;i++){
		int a,b,c[16],d[16];
		scanf("%d",&a);
		for (int x=0;x<16;x++)
			scanf("%d",&c[x]);
		scanf("%d",&b);
		for (int x=0;x<16;x++)
			scanf("%d",&d[x]);
		vector<int> ans;
		for (int j=(a-1)*4;j<(a-1)*4+4;j++){
			for (int k=(b-1)*4;k<(b-1)*4+4;k++){
				if (c[j]==d[k])
					ans.push_back(c[j]);
			}
		}
		if (ans.size()==1)
			printf("Case #%d: %d\n",i,ans[0]);
		else if (ans.size()>1)
			printf("Case #%d: Bad magician!\n",i);
		else if (ans.size()==0)
			printf("Case #%d: Volunteer cheated!\n", i);
	}
}