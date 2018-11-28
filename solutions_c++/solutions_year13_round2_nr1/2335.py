#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<limits.h>
#define fori(a) for(i=0;i<a;i++)
#define forj(a) for(j=0;j<a;j++)
#define fork(a,b) for(k=a;k<b;k++)
int readint()
{
    int t=0;
    char c;
    c=getchar();
    while(c<'0' || c>'9')
        c=getchar();
    while(c>='0' && c<='9')
    {
        t=(t<<3)+(t<<1)+c-'0';
        c=getchar();
    }
    return t;
}
int compare(const void *a,const void *b)
{
    return *(int*)a-*(int*)b;
}
int main()
{
    int i,j,k,t,n,p,count,m,d;
    freopen("A-small-attempt1.in","r",stdin);
    freopen("outputone.txt","w",stdout);
    t=readint();
    fori(t)
    {
        m=readint();
        n=readint();
        int arr[n];
        forj(n) arr[j]=readint();
        p=0;
        int sum=0,count1,count2,count;
        count=0;
        sum=m;
        k=n;
        if (m==1) printf("Case #%d: %d\n",i+1,n);
        else{
        while(n>0)
        {
            qsort(&arr[p],n,sizeof(int),compare);
            //forj(n) printf("%d ",arr[j]);
            //printf("%d %d\n",sum,arr[p]);
            if (sum>arr[p])
            {
                //printf("Inside %d %d\n",p,arr[p]);
                sum+=arr[p];
                p++;
                n--;
            }
            else //(sum<=arr[p])
            {
                //puts("No");
                d=sum-1;
                count1=0;
                count2=0;
                while(sum<=arr[p]&&d!=0)
                {
                    sum+=d;
                    d=sum-1;
                    count1++;
                }
                count2=n;
                if (count1<count2)
                {
                    sum+=arr[p];p++;count+=count1;n--;
                }
                else
                {
                    p+=n;count+=count2;
                    n-=count2;
                }
            }
        }
        printf("Case #%d: %d\n",i+1,count);
        }
    }

    return 0;
}
