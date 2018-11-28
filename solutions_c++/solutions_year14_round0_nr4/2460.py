#include <iostream>
#include <cstdio>
#include <algorithm>

#define ll long long int

using namespace std;

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    
    
    ll t;
    ll p, i, j, n;
    
    double a[1010], b[1010], c[1010];
    
    scanf("%lld", &t);
    
    for (p = 1 ; p <= t; p++) 
	{
        scanf("%lld", &n);
        for (i = 0 ; i < n ; i++)
		 {
            scanf("%lf", &a[i]);
        }
        for (i = 0 ; i < n ; i++)
		 {
            scanf("%lf", &b[i]);
            c[i] = b[i];
        }
        
        sort(a,a+n);
        sort(b,b+n);
        sort(c,c+n);
        
        ll d = 0;
        
        for (i = 0 ; i < n ; i++)
		 {
            for (j = 0 ; j < n ; j++) 
			{
                if (a[i] < b[j] && b[j] != -1) 
				{
                    d++;
                    b[j] = -1;
                    break;
                }
            }
        }
        
        d = n-d;
        ll e = 0;
        
        for (i = 1 ; i < n  ;i++) 
		{
           for (j = 0 ; j < n ; j++)
		    {
               if (a[j] > c[i] && a[j] != -1 && c[i] != -1)
			    {
                    e++;
                    c[i] = -1;
                    a[j] = -1;
                    break;
               }
           }
        }

        for (i = 0 ; i < n ; i++)
		 {
            if(a[i] != -1 && a[i] > c[0]) {
                e++;
                break;
            }
        }
        printf("Case #%lld: %lld %lld\n",p,e,d);
    }
    return 0;
}
