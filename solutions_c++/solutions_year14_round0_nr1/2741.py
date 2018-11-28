//prob A magic trick
#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int main() {
	int n;
	scanf("%d",&n);
	for (int k=1; k<=n; k++) {
		int arr[4][4];
		int brr[4][4];
		int answer1;
		int answer2;
		vector<int> solution;
		
		scanf("%d",&answer1);
		for (int i=0; i<4; i++) {
			for (int j=0; j<4; j++) {
				scanf("%d",&arr[i][j]);
			}
		}
		
		scanf("%d",&answer2);
		for (int i=0; i<4; i++) {
			for (int j=0; j<4; j++) {
				scanf("%d",&brr[i][j]);
			}
		}
		
		answer1--; answer2--;
		for (int j=0; j<4; j++) {
			for (int i=0; i<4; i++) {
				if (arr[answer1][j]==brr[answer2][i]) {
					solution.push_back(arr[answer1][j]);
				}
			}
		}
		printf("Case #%d: ",k);
		if (solution.size()==0) {
			printf("Volunteer cheated!\n");
		}
		else if (solution.size()>1) {
			printf("Bad magician!\n");
		}
		else printf("%d\n",solution[0]);
	}
	return 0;
}
