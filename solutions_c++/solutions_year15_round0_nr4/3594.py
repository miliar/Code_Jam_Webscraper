#include <bits/stdc++.h>
#define ll long long unsigned int
using namespace std;


int main() {
	// your code goes here
    ll t,n,op=1,a,i,sum,me,mi,atmost,r,c;
    scanf("%llu",&t);
    while(t--)
    {
        scanf("%llu%llu%llu",&n,&r,&c);
        if(n==1)
        {
             printf("Case #%llu: GABRIEL\n",op);
            
        }
        else if(n==2)
        {
            if(r%2==1&&c%2==1)
            printf("Case #%llu: RICHARD\n",op);
            else
            printf("Case #%llu: GABRIEL\n",op);
            
        }
        else if(n==3)
        {
            if(r==1||c==1)
            printf("Case #%llu: RICHARD\n",op);
            else if((r==2&&c==3)||(r==3&&c==2)||(r==4&&c==3)||(r==3&&c==4)||(r==3&&c==3))
            printf("Case #%llu: GABRIEL\n",op);
            else
            printf("Case #%llu: RICHARD\n",op);
            
            
            
        }
        else if(n==4)
        {
            if((r==4&&c==3)||(r==3&&c==4)||(r==4&&c==4))
            printf("Case #%llu: GABRIEL\n",op);
             else
         printf("Case #%llu: RICHARD\n",op);

            
        }
      

        op++;
    }
	return 0;
}
