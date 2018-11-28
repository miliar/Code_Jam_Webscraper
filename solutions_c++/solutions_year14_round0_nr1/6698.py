#include<cstdio>
#include<vector>
using namespace std;

int main(){
	int t, r1, r2, x;
	scanf("%d", &t);
	for(int i = 0; i < t; ++i){
		vector<int> v1, v2;
		scanf("%d", &r1);
		for(int j = 0; j < 4; ++j){
			if(j == r1 - 1){
				for(int k = 0; k < 4; ++k){
					scanf("%d", &x);
					v1.push_back(x);
				}
			} else {
				for(int k = 0; k < 4; ++k){
					scanf("%d", &x);
				}
			}
		}
		scanf("%d", &r2);
		for(int j = 0; j < 4; ++j){
			if(j == r2 - 1){
				for(int k = 0; k < 4; ++k){
					scanf("%d", &x);
					v2.push_back(x);
				}
			} else {
				for(int k = 0; k < 4; ++k){
					scanf("%d", &x);
				}
			}
		}
		int p = 0;
		for(int j = 0; j < 4; ++j){
			for(int k = 0; k < 4; ++k){
				if(v1[j] == v2[k]){
					p++;
					x = v1[j];
				}
			}
		}
		printf("Case #%d: ", i + 1);
		if(p == 0){
			printf("Volunteer cheated!\n");
		} else {
			if(p == 1){
				printf("%d\n", x);
			} else {
				printf("Bad magician!\n");
			}
		}
	}
	return 0;
}
