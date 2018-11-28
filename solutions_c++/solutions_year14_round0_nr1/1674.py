#include"cstdio"
#include"cstdlib"

main ()
{
    
    FILE *fpr,*fpw;
    fpr = fopen("A.in","r+");
    fpw = fopen("A.out","w+");
    int TEST;
    fscanf(fpr,"%d",&TEST);
    int n;
    for (n=1;n<=TEST;n++)
    {
        int check[17]={0};
        int i,j,ans1;
        fscanf(fpr,"%d",&ans1);
        for (i=1;i<=4;i++)
        {
            for (j=0;j<4;j++)
            {
                int temp;
                fscanf(fpr,"%d",&temp);
                if (i==ans1) check[temp]=1;
            }
        }
        int ans2,card;
        fscanf(fpr,"%d",&ans2);
        int count=0;
        for (i=1;i<=4;i++)
        {
            for (j=0;j<4;j++)
            {
                int temp;
                fscanf(fpr,"%d",&temp);
                if (i==ans2) check[temp]++;
                if (check[temp]==2) 
                {
                    ++count; card=temp;
                }
            }
        }
        fprintf(fpw,"Case #%d: ",n);
        if (count==0) fprintf(fpw,"Volunteer cheated!");
        else if (count==1) fprintf(fpw,"%d",card);
        else fprintf(fpw,"Bad magician!");
        fprintf(fpw,"\n");
    }
    
    printf("YAY!");
    scanf(" ");
}
