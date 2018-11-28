#include <stdio.h>
#include <vector>

using namespace std;

int n;

int main() {
	scanf("%d",&n);
	
	for(int i = 0; i < n;i++) {
		int n1;
		int n2;
		int t1[5][5];
		int t2[5][5];
		int numbers1[5];
		int numbers2[5];
		
		scanf("%d",&n1);
		for(int j = 0;j < 4;j++) {
			for(int k = 0; k < 4;k++) {
				scanf("%d",&t1[j][k]);
				if(j+1 == n1) numbers1[k] = t1[j][k];
			}
		}
		
		scanf("%d",&n2);
		for(int j = 0;j < 4;j++) {
			for(int k = 0; k < 4;k++) {
				scanf("%d",&t2[j][k]);
				if(j+1 == n2) numbers2[k] = t2[j][k];
			}
		}
		vector<int> v;
		
		for(int j = 0; j < 4;j++) {
			for(int k = 0;k<4;k++) {
				if(numbers1[j] == numbers2[k]) {
					v.push_back(numbers1[j]);
				}
			}
		}
		
		printf("Case #%d: ",i+1);
		
		if(v.size() == 1) {
			printf("%d",v[0]);
		}
		 
		if(v.size() == 0) {
			printf("Volunteer cheated!");
		}
		
		if(v.size() > 1) {
			printf("Bad magician!");
		}
		
		printf("\n");
	}

	return 0;
}
