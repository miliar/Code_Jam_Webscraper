#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int s[107];
char ss[107];
int main()
{
    freopen("c:/B-small-attempt0.in","r",stdin);
    freopen("c:/b-small.out","w",stdout);
    int t,l;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        int ans=0;
        scanf("%s",ss);
        l=strlen(ss);
        for(int j=l-1;j>=0;j--)
        {
            if(ss[j]=='-')
            {
                ans+=1;
                ss[j]='+';
                for(int k=j-1;k>=0;k--)
                {
                    if(ss[k]=='-')
                        ss[k]='+';
                    else
                        ss[k]='-';
                }
            }
        }
        printf("Case #%d: %d\n",i,ans);
    }
}
