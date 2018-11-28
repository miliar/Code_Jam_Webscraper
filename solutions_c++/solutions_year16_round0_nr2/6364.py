#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);

    int T,t=1;
    scanf("%d",&T);
    while(T--)
    {
        string s1,s2,s3,temp;
        int i,j,k,len1=0,len2=0,cnt1=0,cnt2=0;
        cin>>s1;
         len1=s1.size();
         temp=s1[0];
         for (i=1;i<len1;i++)
         {
            if(s1[i]!=s1[i-1])
            {
                temp=s1[i];
                cnt1++;
            }

         }
         if (s1[len1-1]=='+')
         {
             printf("Case #%d: %d\n",t,cnt1);
             t++;

         }
         else if (s1[len1-1]=='-')
         {
             printf("Case #%d: %d\n",t,cnt1+1);
             t++;
         }





    }
    return 0;
}
