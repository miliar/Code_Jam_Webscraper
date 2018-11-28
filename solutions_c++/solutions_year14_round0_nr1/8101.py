#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
	int t,mat1[4][4],mat2[4][4],i,j,ans1,ans2,card,count,tc;
	cin>>t;
	tc = 0;
	while(t--) {
		tc++;
		count = 0;
		cin>>ans1;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++) cin>>mat1[i][j];
		cin>>ans2;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++) cin>>mat2[i][j];

		ans1--,ans2--;
		for(i=0;i<4;i++) {
			for(j=0;j<4;j++) {
				if(mat1[ans1][i] == mat2[ans2][j]) {
					count++;
					card = mat1[ans1][i];
				}
			}
		}
		if(count == 0) printf("Case #%d: Volunteer cheated!\n",tc);
		else if(count == 1) printf("Case #%d: %d\n",tc,card);
		else printf("Case #%d: Bad magician!\n",tc);
	}
	return 0;
}