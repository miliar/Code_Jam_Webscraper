#include <cstdio>
#include <iostream>

using namespace std;

int A[20], casos, bas, esta, eleg;

int main()
{
    freopen("small.in","r",stdin);
    freopen("answer.txt","w",stdout);
    scanf("%d",&casos);
    for(int v=1; v<=casos; v++){
        scanf("%d",&esta);
        for(int i=1; i<esta; i++){
            for(int e=1; e<=4; e++)
                scanf("%d",&bas);
        }
        for(int i=1; i<=4; i++)
            scanf("%d",&A[i]);
        for(int i=esta+1; i<5; i++){
            for(int e=1; e<=4; e++)
                scanf("%d",&bas);
        }

        scanf("%d",&esta);
        for(int i=1; i<esta; i++){
            for(int e=1; e<=4; e++)
                scanf("%d",&bas);
        }
        for(int i=5; i<=8; i++)
            scanf("%d",&A[i]);
        for(int i=esta+1; i<5; i++){
            for(int e=1; e<=4; e++)
                scanf("%d",&bas);
        }
        eleg=0;
        for(int i=1; i<8; i++){
            for(int e=i+1; e<=8; e++){
                if(A[i]==A[e]){
                    if(eleg==0)
                        eleg=A[i];
                    else
                        eleg=-1;
                }
            }
        }
        printf("Case #%d: ",v);
        if(eleg==0)
            printf("Volunteer cheated!\n");
        else if(eleg>0)
            printf("%d\n",eleg);
        else
            printf("Bad magician!\n");
    }
    return 0;
}
