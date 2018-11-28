#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
    int T;
    scanf("%d",&T);
    for(int c = 1 ; c <= T ; c++){
        int X,R,C;
        scanf("%d %d %d",&X,&R,&C);
        if(R > C)
            swap(R,C);
        printf("Case #%d: ",c);
        int Y = (X-1)/2+1;
        bool no = false;
        // printf("%d %d %d\n",R,C,Y);
        if(X>6 or (R*C)%X != 0 or X>C or Y>R)
            no = true;
        if(X>=2*R-1){
            for(int d = 0 ; d <= X-R ; d++){
                bool ttt = true;
                for(int e = 0 ; e <= C-1-d-(X-d-R) ; e++){
                    int winner = R*e+R*d-d;
                    if(winner%X == 0 and (R*C-winner-R-d-(X-d-R))%X == 0)
                        ttt = false;
                }
                no |= ttt;
            }
        }
        if(no)
            printf("RICHARD\n");
        else
            printf("GABRIEL\n");
    }
}
