#include <stdio.h>
#include <string.h>

bool card [17];

int main ()
{
    int t,kase=0,i,row,x,j;

    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);

    scanf ("%d",&t);

    while (t--){
        scanf ("%d",&row);

        int x;
        memset (card,false,sizeof (card));

        for (i=0;i<4;i++){
            for (j=0;j<4;j++){
                 scanf ("%d",&x);
                 if (i==row-1) card[x]=true;
            }
        }

        int tot=0,res;

        scanf ("%d",&row);

        for (i=0;i<4;i++){
            for (j=0;j<4;j++){
                 scanf ("%d",&x);
                 if (i==row-1 && card[x]==true){
                    tot+=1;
                    res=x;
                 }
            }
        }

        printf ("Case #%d: ",++kase);
        if (tot==0) printf ("Volunteer cheated!\n");
        else if (tot==1) printf ("%d\n",res);
        else printf ("Bad magician!\n");
    }
    return 0;
}
