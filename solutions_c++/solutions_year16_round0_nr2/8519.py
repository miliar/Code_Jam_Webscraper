#include<bits/stdc++.h>
using namespace std;

int main()
{
   // freopen("b.txt","r",stdin);
    //  freopen("output_large_large_b.txt","w",stdout);
    int test,cas,temp,i,j,len,ans;
    string s;
    char flag;
    scanf("%d",&test);
    for(cas=1; cas<=test; cas++)
    {
        cin>> s;
        len=s.length();
        if(s[len-1]=='-')
            ans=1;
        else ans=0;
        flag=s[0];
        for(i=0; i<len; i++)
        {
            for(j=i; j<len; j++)
            {
                if(flag!=s[j])
                {
                    ans++;
                    flag=s[j];
                    i=j-1;
                    break;
                }
            }
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
