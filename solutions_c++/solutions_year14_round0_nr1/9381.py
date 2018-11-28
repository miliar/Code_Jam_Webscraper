#include<stdio.h>
#include<math.h>
int a[4][4];
int b[4][4];
int c[20];
int main()
{
   int t,row1,row2,i,j,flag,pos;
   FILE *fp;
   FILE *fo;
   fp=fopen("A-small-attempt0.in","r");
    fo=fopen("output.txt","w");
    char s[25];
   fscanf(fp,"%d",&t);
   printf("%d\n",t);
   while(t--)
   {
       for(i=0;i<17;i++)
        c[i]=0;
       fscanf(fp,"%d",&row1);
       row1--;
       for(i=0;i<4;i++)
{
        fscanf(fp,"%d %d %d %d",&a[i][0],&a[i][1],&a[i][2],&a[i][3]);
        printf("%d %d %d %d\n",a[i][0],a[i][1],a[i][2],a[i][3]);
        }
         fscanf(fp,"%d",&row2);
         //printf("%d\n",row2);
       row2--;
       for(i=0;i<4;i++)
       {
      int ret=fscanf(fp,"%d %d %d %d",&b[i][0],&b[i][1],&b[i][2],&b[i][3]);
       //printf("%d\n",ret);
       }
    for(i=0;i<4;i++)
        c[a[row1][i]]=1;
        flag=0;
    for(i=0;i<4;i++)
    {
        if(c[b[row2][i]]==1)
        {
            flag++;
            pos=b[row2][i];
        }
    }

    if(flag==1)
    {
        fprintf(fo,"%s%d\n","Case #1: ",pos);
    }
    else if(flag==0)
    {
        fprintf(fo,"%s","Case #3: Volunteer cheated!\n");
    }
    else
    {
        fprintf(fo,"%s","Case #2: Bad magician!\n");
    }
   }
   fclose(fo);
   fclose(fp);
return 0;
}
