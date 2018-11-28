#include<cstdio>
#include<map>
using namespace std;
int main(){
	freopen("0.in","r", stdin);
	freopen("0.out","w",stdout);
	int t;
	scanf("%d", &t);
	for(int ca = 1; ca <= t; ca ++){
        int x, r, c;
        scanf("%d %d %d", &x, &r, &c);
        if (r > c){
            swap(r, c);
        }
        if (x == 1){
            printf("Case #%d: GABRIEL\n", ca);
        }
        else if (x == 2){
            if (r == 2 || c == 2 || c == 4){
				printf("Case #%d: GABRIEL\n", ca);
            }
            else{
				printf("Case #%d: RICHARD\n", ca);
            }
        }
        else if (x == 3){
            if((r==3 && c!=1)||(c==3 && r!=1)){
                printf("Case #%d: GABRIEL\n", ca);
            }
            else{
				printf("Case #%d: RICHARD\n", ca);
            }
        }
        else if (x == 4){
			if((r == 4 || r == 3) && c == 4){
				printf("Case #%d: GABRIEL\n", ca);
			}else{
				printf("Case #%d: RICHARD\n", ca);
			}
        }
	}
	return 0;
}
