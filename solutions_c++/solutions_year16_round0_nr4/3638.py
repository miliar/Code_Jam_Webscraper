#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int t,cs=0,k,c,s;
    scanf("%d", &t);
    while (t--) 
  {
    
        scanf("%d %d %d", &k, &c, &s);
     	++cs;
        if (k == 1) 
            printf("Case #%d: 1\n",cs);
        else if (c == 1) 
	{
            if (s == k) 
		{
		printf("Case #%d: ",cs);
                for (int i = 1; i <= k; i++)
                    printf("%d ", i);
                printf("\n");
            }
            else 
                printf("Case #%d: IMPOSSIBLE\n",cs);
            
        }
        else 
	{
	   printf("Case #%d: ",cs);
            if (s < k-1)
                printf("IMPOSSIBLE\n");
            else 
		{
		        int i = 2, cnt = 0;
		        while (cnt < k-1)
			 {
		            printf("%d ", i++);
		            cnt++;
		         }
		        printf("\n");
            	}
        }
    }
    return 0;
}
