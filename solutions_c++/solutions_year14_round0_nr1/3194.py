#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int main()
{
	//freopen("in_jam.txt","r",stdin);
	//freopen("out_jam1.txt","w",stdout);
	int T,A[4][4],B[4][4],A1,B1;
	scanf("%d",&T);
	vector<int> ans;
	for (int i = 0; i < T; ++i)
	{
		ans.clear();
		scanf("%d",&A1);
		for(int j = 0;j < 4;j++){
			for(int k = 0;k < 4;k++){
				scanf("%d",&A[j][k]);
			}
		}
		scanf("%d",&B1);
		for(int j = 0;j < 4;j++){
			for(int k = 0;k < 4;k++){
				scanf("%d",&B[j][k]);
			}
		}
		for(int j = 0;j < 4;j++){
			for(int k = 0;k < 4;k++){
				if(A[A1 - 1][j] == B[B1 - 1][k]){
					ans.push_back(A[A1 - 1][j]);
					break;
				}
			}
		}
		if(ans.size() > 1){
			printf("Case #%d: Bad magician!\n",i + 1);
		}
		else if(ans.size() == 0){
			printf("Case #%d: Volunteer cheated!\n",i + 1);
		}
		else {
			printf("Case #%d: %d\n",i + 1,ans[0]);
		}
	}
	return 0;
}
