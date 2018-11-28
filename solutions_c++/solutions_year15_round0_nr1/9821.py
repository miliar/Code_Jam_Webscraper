#include <bits/stdc++.h>
#define ll long long unsigned int
using namespace std;

int main() {
	// your code goes here
    ll t,n,op=1,i,count,ans;
    char a[10001];
    scanf("%llu",&t);
    while(t--)
    {
        scanf("%llu",&n);
        scanf("%s",a);
        count=0;
        ans=0;
        for(i=0;i<=n;i++)
        {
            if(i>count)
            {
               
                ans+=i-count;
                count+=i-count;
                
            }
             count+=a[i]-'0';
             //printf("%llu %llu %llu \n",count,ans,i);
        }
        printf("Case #%llu: %llu\n",op,ans);
        op++;
        
    }
	return 0;
}
