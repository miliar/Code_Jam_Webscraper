#include <stdio.h>
#include <algorithm>
using namespace std;
int a[1000005];
int main()
{
    int totalcase,cur,total;
    FILE *in=fopen("A-small-attempt4.in","r");
    FILE *out=fopen("output.txt","w");
    fscanf(in,"%d",&totalcase);
    for(int o=0;o<totalcase;o++)
    {
        fscanf(in,"%d %d",&cur,&total);
        for(int i=0;i<total;i++)
        {
            fscanf(in,"%d",&a[i]);
        }
        sort(a,&a[total]);
        int count2=0;
        int m=10000000;
        for(int i=0;i<total;i++)
        {
            if(cur<=a[i])
            {
                //printf("w1 %d->%d\n",a[i],cur);
                m=min(m,total-i+count2);
                if(cur<=1)
                {
                    m=total-i+count2;
                    break;
                }
                while(cur<=a[i])
                {
                    cur+=cur-1;
                    count2++;
                }
                cur+=a[i];
                m=min(m,total-i-1+count2);
                //printf("w2 %d->%d\n",a[i],cur);
            }
            else
            {
                cur+=a[i];
                /*printf("w3 %d->%d\n",a[i],cur);
                printf("%d %d+%d\n",i,total-i-1,count2);*/
                m=min(m,total-i-1+count2);
            }
        }
        fprintf(out,"Case #%d: %d\n",o+1,m);
    }
    return 0;
}
/*
1
10 7
5 15 20 100 105 110 150
*/
