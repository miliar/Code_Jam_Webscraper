#include"cstdio"
#include"cstdlib"

main ()
{
    FILE *fpr,*fpw;
    fpr = fopen("D-large.in","r+");
    fpw = fopen("D-large.out","w+");
    int TEST;
    fscanf(fpr,"%d",&TEST);
    int n;
    for (n=1;n<=TEST;n++)
    {
        double n1[1001],n2[1001];
        int num;
        int i,j;
        fscanf(fpr," %d",&num);
        for (i=0;i<num;i++) fscanf(fpr," %lf",&n1[i]);
        for (i=0;i<num;i++) fscanf(fpr," %lf",&n2[i]);
        for (i=0;i<num;i++)
        {
            int min=i;
            for (j=i+1;j<num;j++) if (n1[j]<n1[min]) min=j;
            double temp = n1[min];
            n1[min] = n1[i];
            n1[i] = temp;
        }
        for (i=0;i<num;i++)
        {
            int min=i;
            for (j=i+1;j<num;j++) if (n2[j]<n2[min]) min=j;
            double temp = n2[min];
            n2[min] = n2[i];
            n2[i] = temp;
        }
        
        fprintf(fpw,"Case #%d: ",n);
        
        //DECEITFUL WAR!!
        int check[1001]={0};
        int point=0;
        for (i=0;i<num;i++)
        {
            for (j=0;j<num;j++)
            {
                if (n1[i]>n2[j] && check[j]==0) break;
            }
            if (j==num)
            {
                for (j=num-1;j>=0;j--) if (check[j]==0) break;
                check[j]=1;
            }
            else
            {
                ++point;
                check[j]=1;
            }
        }
        printf("%d ",point);
        fprintf(fpw,"%d ",point);
        
        //WAR!!
        
        j=-1;
        for (i=0;i<num;i++)
        {
            for (++j;j<num;j++)
            {
                if (n2[j]>n1[i]) break;
            }
            if (j>=num) break;
        }
        printf("%d\n",num-i);
        fprintf(fpw,"%d ",num-i);
        
        
        
        fprintf(fpw,"\n");
    }
    
    printf("YAY!");
    
    scanf(" ");
}
