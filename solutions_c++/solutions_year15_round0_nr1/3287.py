#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    int T,i,j,k,n,m,cs=0;
    string s;
    cin>>T;
    while(T--)
    {
        scanf("%d",&n);
        cin>>s;
        for(i=0,j=0,k=0;s[i];i++)
        {
            k+=max(i-j,0);
            j+=max(i-j,0);
            j+=s[i]-'0';
        }
        printf("Case #%d: %d\n",++cs,k);
    }
    return 0;
}
