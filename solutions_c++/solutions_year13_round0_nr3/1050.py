using namespace std;

#include <iostream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>

typedef long long unsigned int LLU;

LLU reverse(LLU num)
{
     LLU rem=0,d;
     while(num>0)
     {
               d=num%10;
               rem=rem*10+d;
               num=num/10;
     }
     return rem;
}
bool ispalin(LLU num)
{
     LLU num_rev=reverse(num);
     if(num==num_rev)
        return 1;
     return 0;
}
int main()
{
    //freopen("C-large-1.in","r",stdin);
    //freopen("out-large1.txt","w",stdout);
    int t=0,k=0,i=0,count,count1,count2;
    LLU j,a,b,arr[100];
    for(LLU i=1;i<100000001;i++)
     {
             if(ispalin(i))
             {
                                j=i*i;
                                if(ispalin(j))
                                {
                                    arr[k++]=j;
                                }
             }
     }

    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%llu %llu",&a,&b);
        count=0,count1=0,count2=0;
        if(a>arr[k-1])
            {
                printf("0\n");
                continue;
            }
        if(b>arr[k-1])
               b=arr[k-1];
        for(int l=0;l<k;l++)
               {
                       if(arr[l]>=a)
                        {
                            count1=l;
                            break;
                        }
               }
               for(int l=0;l<k;l++)
               {
                       if(arr[l]<=b)
                       count2=l;
               }
        count=count2-count1+1;
        cout<<"Case #"<<i<<": "<<count<<endl;
    }
    return 0;
}
