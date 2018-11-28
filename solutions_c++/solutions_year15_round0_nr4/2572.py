#include <cstdio>
using namespace std;

int main() {
	int TC, x, r, c, ans = 0;
	scanf("%d", &TC);
	for(int i=1; i<=TC; i++){
                bool richard = false;
                scanf("%d %d %d", &x, &r, &c);
                if(x == 4){
                        richard = r*c%x != 0 || r <= 2 || c <= 2;
                }
                if(x == 3){
                        richard = r*c%x != 0 || r == 1 || c == 1;
                }
                if(x == 2){
                        richard = r*c%x != 0;
                }
                printf("Case #%d: %s\n", i, richard?"RICHARD":"GABRIEL");
	}
}
