#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#define Bint long long int
#define N 10000000
using namespace std;
int d[100000];
bool judge(char ch[])
{
    int n=strlen(ch);
    char c[20];
    for(int i=0;i<=n;i++)
        c[i]=ch[i];
    reverse(c,c+n);
    return strcmp(ch,c)==0;
}
void init(int &k)
{   k=0;
    for(int i=1;i<=N;i++)
    {
        char ch[20];
        sprintf(ch,"%d",i);
        if(judge(ch))
        {   Bint w=i*i;
            sprintf(ch,"%lld",w);
            if(judge(ch)){ d[k++]=i;}
        }
    }
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int t;
    int k;
    init(k);
    while(scanf("%d",&t)!=EOF)
    {
        int ca=0;
        while(t--)
        {ca++;
          Bint a,b;
          scanf("%lld%lld",&a,&b);

          int ans=0;
          for(int i=0;i<k;i++)
          {
              Bint w=d[i]*d[i];
              if(a<=w && b>=w) ans++;
              if(w>b) break;
          }
          printf("Case #%d: %d\n",ca,ans);

        }
    }
    return 0;
}
