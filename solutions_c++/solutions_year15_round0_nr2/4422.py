#include <stdio.h>
#include <algorithm>
using namespace std;
int tt[10]={0};
int find(int d)
{
    int Min=d;
    if(d==0)
    {
        return 0;
    }
    if(tt[d]!=0)
    {
        for(int i=d-1;i>=1;i--)
        {
            tt[i]+=tt[d];
            tt[d-i]+=tt[d];
            Min = min(Min,find(d-1)+tt[d]);
            tt[i]-=tt[d];
            tt[d-i]-=tt[d];
        }
    }
    else return find(d-1);
    //printf("%d %d\n",d,Min);
    return Min;
}
int main()
{
    int t;
    FILE *in = fopen("input.in","r");
    FILE *out = fopen("output.txt","w");
    fscanf(in,"%d",&t);
    for(int o=0;o<t;o++)
    {
        for(int i=0;i<10;i++)
            tt[i]=0;
        int a;
        int temp[10];

        fscanf(in,"%d",&a);
        for(int j=0;j<a;j++){
            fscanf(in,"%d",&temp[j]);
            tt[temp[j]]++;
        }
        fprintf(out,"Case #%d: %d\n",o+1,find(9));
    }
}
