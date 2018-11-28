#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int main()
{
    int T,cas=0;
    scanf("%d",&T);
    while(T--)
    {
        string s;
        cin>>s;
        int len=(int)s.size(),ans=(s[len-1]=='-');
        for(int i=1;i<len;++i)
            if(s[i]!=s[i-1])ans++;
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
