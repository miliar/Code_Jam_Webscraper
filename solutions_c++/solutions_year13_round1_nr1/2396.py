#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;

int ttt;


long long r,t,ans;



int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0_out.txt","w",stdout);
    
    int i,j;
    
    scanf("%d",&ttt);
    for(int tt=1;tt<=ttt;tt++)
    {
        printf("Case #%d: ",tt);
        scanf("%lld %lld",&r,&t);
        long long num=r/2;
        if(r%2==0)
        {
            long long op=-1;
            t+=(num)*(2*num-1);
        }
        else
        {
            long long op=1;
            t+=(num)*(2*num+1);
        }
        
        long long lo=1,mid,hi=1000000000LL;
        
        
        
        while(lo < hi)
        {
            mid = lo + (hi-lo+1)/2;
            //printf("\n%lld %lld %lld %lld\n",lo,mid,hi,t);
            long long temp;
            if(r%2==1)
                temp=(mid*(2*mid+1));
            else
                temp=(mid*(2*mid-1));
            //printf("%lld %lld \n",temp,t);
            if(temp>t)
            {
                hi = mid-1;
                //printf("1111\n");
            }
            else
            {
                lo = mid;
                //printf("2222\n");
            }
        }
        
        ans=lo-num;
        printf("%lld\n",ans);
        
        
        
    }
    
    
    
    //system("pause");
    return 0;
}
