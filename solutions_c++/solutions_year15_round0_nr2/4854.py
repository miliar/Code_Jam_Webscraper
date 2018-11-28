#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
int arr[1003];

int main()
{    
    int t,d,i,j,mxsec,mnsec,sum,step=0;    
    scanf("%d",&t);    
    while(t--)
	 {
        scanf("%d", &d) ;
        for(i=0;i<d;i++) 
		{
            scanf("%d", &arr[i]) ;
            mxsec = max(mxsec,arr[i]) ;
        }
        
        mnsec = mxsec ;
        
        for(i=1;i<=mxsec;i++) 
		{
            sum=i;
            for(j=0;j<d;j++)
            {
                if( arr[j] > i )
                {
                    if( arr[j]%i == 0 )
                        sum += (arr[j]/i-1) ;
                    else
                        sum += (arr[j]/i) ;
                }
            }
            mnsec = min(mnsec,sum) ;
        }
        printf("Case #%d: %d\n", ++step, mnsec) ;
    }
    return 0 ;
}