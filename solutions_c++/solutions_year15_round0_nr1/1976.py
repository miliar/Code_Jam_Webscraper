#include <iostream>
#include <cstring>
#include <cstdio>
#include <queue>
#include <stack>
#include <string>
using namespace std;
string a;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    int n,s,ans,num;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        scanf("%d",&n);
        cin>>a;
        s=a[0]-'0';
        ans=0;
        for(int j=1;j<=n;j++)
        {
            num=a[j]-'0';
            if(s<j)
            {
                ans+=j-s;
                s=j;
            }
            s+=num;
        }
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
