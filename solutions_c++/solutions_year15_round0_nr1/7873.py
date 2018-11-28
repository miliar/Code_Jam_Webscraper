#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;

const int MAXN=1110;
int n;
char s[MAXN];
int main()
{
//        freopen("E:\\Code_Fantasy\\C\\A-small-attempt0.txt","r",stdin);
//        freopen("E:\\Code_Fantasy\\C\\A-small-attempt1.txt","w",stdout);
        int t;
        scanf("%d",&t);
        for(int Cas=1;Cas<=t;++Cas)
        {
                scanf("%d",&n);
                scanf("%s",s);
                int ans=0;
                int shy=s[0]-'0';
                for(int i=1;i<=n;++i)
                {
                        if(s[i]-'0'!=0)
                        {
                                if(shy>=i)
                                {
                                        shy+=(s[i]-'0');
                                }
                                else
                                {
                                        ans+=(i-shy);
                                        shy=i+(s[i]-'0');
                                }
                        }
                }
                printf("Case #%d: %d",Cas,ans);
                if(Cas!=t) puts("");
        }
        return 0;
}
