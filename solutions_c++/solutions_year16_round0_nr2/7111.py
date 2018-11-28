#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T,cnt;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        string s;
        cin>>s;
        if(s[0]=='-') cnt=1;
        else cnt=0;
        for(int i=0;i<s.size()-1;i++)
        {
            if(s[i]=='+'&&s[i+1]=='-') cnt+=2;
        }
        printf("Case #%d: %d",t,cnt);
        if(t!=T) printf("\n");
    }
    return 0;
}
