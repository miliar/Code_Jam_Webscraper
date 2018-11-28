#include<stdio.h>
#include<stdlib.h>
#include<string.h>
typedef struct ad
{
        int smax;
        char* s;
}ad;
int main()
{
    FILE* fp;
    fp=fopen("in.in","r");
    int t,i,j,tpr,n;
    fscanf(fp,"%d",&t);
    ad* a=(ad*)malloc(sizeof(ad)*t);
    for(i=0;i<t;i++)
    {
                    fscanf(fp,"%d",&a[i].smax);
                    a[i].s=(char*)malloc(sizeof(char)*(a[i].smax+1));
                    fscanf(fp,"%s",a[i].s);
    }
    fclose(fp);
    int p;
    int* op=(int*)malloc(sizeof(int)*t);
    for(i=0;i<t;i++)
    {
                    tpr=0;
                    p=(int)a[i].s[0];
                    p=p-48;
                    for(j=1;j<=a[i].smax;j++)
                    {
                               if(j>p)
                               {
                                     tpr++;
                                     p++;
                               }
                               p+=((int)a[i].s[j])-48;
                               if(p>=a[i].smax)
                                    break;
                    }
                    op[i]=tpr;
    }
    FILE* fp1;
    fp1=fopen("out.out","w");
    for(i=0;i<t;i++)
    {
                   fprintf(fp1,"Case #%d: %d\n",(i+1),op[i]);
    }
    fclose(fp1);
    scanf("%d",&t);
}
