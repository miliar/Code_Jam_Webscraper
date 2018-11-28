#include <cstdlib>
#include <cstdio>
using namespace std;

int main(){
	int cases;
	scanf("%d", &cases);
	for(int z=1; z<=cases; z++){
		int an, bn, t;
		int a[4];
		int b[4];
		
		scanf("%d", &an);
		for(int i=0; i<4; i++){
			if(an == i+1){
				for(int j=0; j<4; j++){
					scanf("%d", &a[j]);
				}
			}else{
				for(int j=0; j<4; j++){
					scanf("%d", &t);
				}
			}
		}
		scanf("%d", &bn);
		for(int i=0; i<4; i++){
			if(bn == i+1){
				for(int j=0; j<4; j++){
					scanf("%d", &b[j]);
				}
			}else{
				for(int j=0; j<4; j++){
					scanf("%d", &t);
				}
			}
		}
		
		int cnt = 0;
		int num = -1;
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				if(a[i] == b[j]){
					num = a[i];
					cnt++;
				}
			}
		}
		
		if(cnt == 0){
			printf("Case #%d: Volunteer cheated!\n", z);
		}else if(cnt == 1){
			printf("Case #%d: %d\n", z, num);
		}else{
			printf("Case #%d: Bad magician!\n", z);
		}
	}

	return 0;
}