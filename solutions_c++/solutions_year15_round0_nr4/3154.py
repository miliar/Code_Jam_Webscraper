#include <iostream>
#include <cstdio>

using namespace std;

int abs(int a){
    if(a>=0) return a;
    else return (-1)*a;
}

int main()
{

    //freopen("D-small-attempt0.in","r",stdin);
    //freopen("test.txt","r",stdin);
    //freopen("D-small-attempt0.out","w",stdout);
    int i,T,X,C,R,winner;
    scanf("%d",&T);
    for(i=1;i<=T;i++){
        winner = 0;
        scanf("%d%d%d",&X,&R,&C);
        if(X==1)
            winner = 1;
        else if(X ==2){
            if(R%2==0)
                winner = 1;
            else{
                if(C%2==0)
                    winner = 1;
                else winner = 2;
            }
        }
        else if(X == 3){
                if(R==3||C==3)
                    if(R>1 && C>1)
                        winner=1;
                    else winner = 2;
                else winner = 2;

        }
        else{
                if(R == 4 || C == 4){
                    if(abs(R-C)<2)
                        winner = 1;
                    else winner = 2;
                }

                else
                    winner = 2;

        }
        if(winner == 1)
            printf("Case #%d: GABRIEL\n",i);
        else if(winner == 2)
            printf("Case #%d: RICHARD\n",i);
    }
    return 0;
}
