#include <stdio.h>
#include <string.h>
#define MAX 20

using namespace std;

int magic[MAX][MAX];
int aux[MAX];

int main()
{
    FILE *out;
    out=fopen("out.txt","w");
    int t,n,cont;
    scanf("%d",&t);
    for(int u=1;u<=t;u++){
        if(u!=1)
            memset(aux,0,sizeof aux);
        scanf("%d",&n);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                scanf("%d",&magic[i][j]);
        for(int i=1;i<=4;i++)
            aux[magic[n][i]]=1;
        scanf("%d",&n);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                scanf("%d",&magic[i][j]);
        for(int i=1;i<=4;i++)
            aux[magic[n][i]]++;
        cont=0;
        int l;
        for(int i=1;i<=16;i++)
            if(aux[i]>1){
                l=i;
                cont++;
            }
        fprintf (out,"Case #%d: ",u);
        //printf("Case #%d: ",u);
        if(cont==1)
            fprintf (out,"%d\n",l);
            //printf("%d\n",l);
        else if(cont>1)
            fprintf (out,"Bad magician!\n");
            //printf("Bad magician!\n");
        else
            fprintf (out,"Volunteer cheated!\n");
            //printf("Volunteer cheated!\n");
    }
    return 0;
}
