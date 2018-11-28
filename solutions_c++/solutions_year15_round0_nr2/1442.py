#include <iostream>
#include <cstdio>  
#include <cstring>  
 
using namespace std;

int Buf[1200]; 

int main()
{  

//	freopen("..\\B-small-attempt2.in","r",stdin);
//	freopen("..\\B-small-attempt2.out","w",stdout);

	freopen("..\\B-large.in","r",stdin);
	freopen("..\\B-large.out","w",stdout);

	int cas = 1;
    int t;   
    int d;
	int maxv = 0;
	int minv;
	int sum;  
  
    scanf("%d", &t) ;

    while(t--)
	{  
        scanf("%d", &d) ;  
        for(int i = 0 ; i < d ; i++)
		{  
            scanf("%d", &Buf[i]);  
            maxv = max(maxv,Buf[i]);  
        }

        minv = maxv ;

        for(int i = 1 ; i <= maxv ; i++)
		{  
            sum = i ;  
            for(int j = 0 ; j < d ; j++)
			{  
                if( Buf[j] > i )
				{  
                    if( Buf[j]%i == 0 )  
                        sum += (Buf[j]/i-1) ;  
                    else  
                        sum += (Buf[j]/i) ;  
                }  
            }  
            minv = min(minv,sum);  
        }

        printf("Case #%d: %d\n", cas++, minv);  
    }  
    return 0;  
}  