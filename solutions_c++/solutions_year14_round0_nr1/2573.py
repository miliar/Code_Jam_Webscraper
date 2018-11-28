#include "iostream"
#include "cstring"
#include "cstdio"
using namespace std;
int a[10][10];
int b[20];
int main(void)
{
	int T, l1, l2;
	freopen("A-small-attempt0.in","r", stdin);
	freopen("A.out","w", stdout);
	int g = 0;
	scanf("%d", &T);
	while(T --){
		printf("Case #%d: ",++ g);
		scanf("%d", &l1);
		memset(b, 0, sizeof(b));
		for(int i = 0; i < 4; ++ i){
			for(int j = 0; j < 4; ++ j){
				scanf("%d", &a[i][j]);
				if(i == l1 - 1){
					b[a[i][j]] ++;
				}
			}
		}
		scanf("%d", &l1);
		for(int i = 0; i < 4; ++ i){
			for(int j = 0; j < 4; ++ j){
				scanf("%d", &a[i][j]);
				if(i == l1 - 1){
					b[a[i][j]] ++;
				}
			}
		}
		int sum = 0, mk = -1;
		for(int i = 1; i <= 16; ++ i){
			if(b[i] == 2){
				mk = i;
				sum ++;
			}
		}
		if(sum == 1){
			printf("%d\n", mk);
		}else if(sum == 0){
			puts("Volunteer cheated!");
		}else{
			puts("Bad magician!");
		}
	}
	return 0;
}
