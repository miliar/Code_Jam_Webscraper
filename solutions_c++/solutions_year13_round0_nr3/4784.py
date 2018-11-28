#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
#include<cstring>

using namespace std;
int main()
{
    int i,t,cnt,k,a,b;
    scanf("%d",&t);
    int s[]={1,4,9,121,484};
    k=1;
    while(k<=t)
    {
         
         cnt=0;
         cin>>a>>b;
         for(i=0;i<5;i++)
         if(s[i]<=b&&s[i]>=a)
         cnt++;
         //if(flag==1)
         printf("Case #%d: %d\n",k,cnt);
         //else if(flag==0)
         //printf("Case #%d: YES\n",k);
         k++;
    }
    return 0;
}
