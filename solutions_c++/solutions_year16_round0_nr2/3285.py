#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    char s[200];
    int cou=0;
    for (int i=1;i<=t;i++)
    {
        scanf("%s",s);
        int len=strlen(s);
        int p=0;
        int ans=0;
        bool first=false;
        if (s[p]=='-') first=true;
        while (p<len)
        {
            bool ismin=false;
            while (p<len && s[p]=='-') {p++;ismin=true;}
            if ((p<len && s[p]=='+') || (p==len))
            {
                //cout<<"cou:"<<cou<<"p:"<<p<<":"<<s[p]<<"first:"<<first<<"ans:"<<ans<<endl;
                while (p<len && s[p]=='+') p++;
                if (ismin)
                 if (first) {ans=ans+1;first=false;}
                    else ans+=2;
                //p++;
            }
            //p++;
        }
        printf("Case #%d: %d\n",++cou,ans);
    }
    return 0;
}
