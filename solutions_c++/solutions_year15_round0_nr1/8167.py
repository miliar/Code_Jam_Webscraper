#include <stdio.h>
#define M 1111
int main()
{
	
	freopen("A-large.in", "r", stdin);
	freopen("output_large.txt", "w", stdout);
	
    int tc, cs = 1;
    scanf("%d",&tc);
    while(tc--)    
    {
       int sm, i, j;
       char x[M];
       int y[M];
       scanf("%d %s", &sm, x);
       for(i = 0; i <= sm; ++i)
       {
        y[i] = x[i] - '0';
       }
       int ans = 0;
       for(i = 0; i <= sm; ++i){
        int tmp = 0;
           for(j = 0; j < i; ++j)
       {
        tmp += y[j];
       }
            if(tmp < i)
         {
          ans += (i - tmp);
          y[0] += (i - tmp);
         }
       }
       printf("Case #%d: %d\n", cs++, ans);
    }
    return 0;
}
