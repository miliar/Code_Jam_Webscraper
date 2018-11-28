#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main(void){
	freopen("A.in", "rt", stdin);
	freopen("A.out", "wt", stdout);
	int ct; cin >> ct;
	for(int caset=1;caset<=ct;caset++){
		int i, j;
		int n1; cin >> n1; n1--;
		int arr1[4][4];
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin >> arr1[i][j];
		int n2; cin >> n2; n2--;
		int arr2[4][4];
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin >> arr2[i][j];
		int tr=0; int num=0;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				if(arr1[n1][i]==arr2[n2][j]){
					tr++;
					num=arr1[n1][i];
				}
		switch(tr){
			case 0:
				printf("Case #%d: Volunteer cheated!\n",caset);
				break;
			case 1:
				printf("Case #%d: %d\n", caset, num);
				break;
			default:
				printf("Case #%d: Bad magician!\n",caset);
		}
				
	}
	return 0;
}

