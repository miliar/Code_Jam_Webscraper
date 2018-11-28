#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<algorithm>
using namespace std;
char s[1<<13],t[1<<13];
const char ty[3]={'P','R','S'};
//alpha P<R<S
void work(char *s,int len)
{
    if(len==1)return;
    work(s,len/2);
    work(s+len/2,len/2);
    int cmp=0;
    for(int i=0;i<len/2;i++)
        if(s[i]!=s[i+len/2])
        {
            if(s[i]>s[i+len/2])cmp=1;
            break;
        }
    if(cmp)for(int i=0;i<len/2;i++)
        swap(s[i],s[i+len/2]);
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++)
    {
        int n,cnt[3];//P,R,S
        scanf("%d%d%d%d",&n,&cnt[1],&cnt[0],&cnt[2]);
        bool isok=0;
        for(int _=0;_<3 && !isok;_++)
        {
            memset(s,0,sizeof(s));
            s[0]=_+'0';
            for(int i=0;i<n;i++)
            {
                for(int j=0;j<(1<<i);j++)
                {
                    t[j<<1]=s[j];
                    t[j<<1|1]=(s[j]-'0'+1)%3+'0';
                }
                for(int j=0;j<(1<<i+1);j++)
                    s[j]=t[j];
            }
            int now[3]={0,0,0};
            for(int i=0;i<(1<<n);i++)
                now[s[i]-'0']++;
            bool flag=1;
            for(int i=0;i<3;i++)
                if(now[i]!=cnt[i])flag=0;
            isok|=flag;
        }
        printf("Case #%d: ",ca);
        if(!isok)printf("IMPOSSIBLE\n");
        else
        {
            work(s,1<<n);
            for(int i=0;i<(1<<n);i++)
                printf("%c",ty[s[i]-'0']);
            printf("\n");
        }
    }
    return 0;
}
