#include<stdio.h>
#include<stdlib.h>
int ma[1000],mb[1000];
int cmp(const void *a ,const void *b)
{
    return *(int *)b - *(int *)a;
}

int main()
{
    //freopen("d.in","r",stdin);
   //freopen("d.txt","w",stdout);
    int T,n,t,i,y,z,j;
    double rw;
    scanf("%d",&T);
    t=1;
    while(T--)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++) {scanf("%lf",&rw);ma[i]=rw*1000000;}
        for(i=0;i<n;i++) {scanf("%lf",&rw);mb[i]=rw*1000000;}
        qsort(ma,n,sizeof(int),cmp);
        qsort(mb,n,sizeof(int),cmp);
        //show(n);
        y=0;z=0;
        for(i=0,y=0,j=0;i<n;i++)
        {
            if(ma[j]>mb[i]) {j++;y++;}
        }
        for(i=0,z=0,j=0;i<n;i++)
        {
            if(mb[j]>ma[i]) j++;
            else z++;
        }
        printf("Case #%d: %d %d\n",t++,y,z);
    }

    return 0;
}
