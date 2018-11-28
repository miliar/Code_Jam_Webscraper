#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int main()
{
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    int a[100];
    int tmp;
    tmp=0;
    int t1,t2,t3,t4,t5;
    int i;
    for(i=1;i<=100;++i)
    {
        if(i*i>1000)
            break;
        t1=i/10;
        t2=i%10;
        if(t1==t2||t1==0)
        {
            t3=(i*i)/100;
            t4=(i*i-t3*100)/10;
            t5=(i*i)%10;
            if(t3==0)
            {
                if(t4==0||t4==t5)
                {
                    a[tmp]=i;
                    tmp++;
//                    printf("%d\n",i);
                }
            }
            else
            {
                if(t3==t5)
                {
                    a[tmp]=i;
                    tmp++;
//                    printf("%d\n",i);
                }
            }
        }
    }
//    printf("tmp=%d\n",tmp);
    int cases;
    int t;
    int j,k;
    int ans;
    scanf("%d",&cases);
    t=1;
    while(cases--)
    {
        printf("Case #%d: ",t);
        t++;
        ans=0;
        scanf("%d%d",&i,&j);
        for(k=0;a[k]*a[k]<=j;++k)
        {
            if(a[k]*a[k]>=i)
                ans++;
        }
        printf("%d\n",ans);
    }
    return 0;
}
