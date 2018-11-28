#include <cstdio>



int main(){
freopen ("A-small-attempt0.in","r",stdin);
freopen ("A-small-attempt0.out","w",stdout);
int times,i,j,chk,ans;
int in,choose,bucket[20];



scanf ("%d",&times);
    for (int t=1;t<=times;t++){
        for (i=0;i<20;i++)
            bucket[i] = 0;
        i = j = chk = ans = in = choose = 0;

        scanf ("%d",&choose);
        for (i=1;i<=4;i++)
            for (j=1;j<=4;j++){
                scanf ("%d",&in);
                if (i==choose)
                    bucket[in]++;
            }
        scanf ("%d",&choose);
        for (i=1;i<=4;i++)
            for (j=1;j<=4;j++){
                scanf ("%d",&in);
                if (i==choose&&bucket[in]){
                    ans=in;
                    chk++;
                }


            }
        if (chk==0) printf ("Case #%d: Volunteer cheated!\n",t);
        else if (chk==1) printf ("Case #%d: %d\n",t,ans);
        else printf ("Case #%d: Bad magician!\n",t);




    }

return 0;
}
