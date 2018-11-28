#include<iostream>
#include<stdio.h>
#include<cstring>
using namespace std;
const int maxn=50005;
char s[maxn];
int a[maxn];
int ne_po=1;
int calc(int x1,int x2)
{
    if (x1==-100) return x2;
    if (x2==-100) return x1;

    if (x1==x2)
    {
        ne_po*=-1;
        return -100;
    }
    if ((x1+1)%3==x2) return (x1+2)%3; else
    {
        ne_po*=-1;
        return (x1+1)%3;
    }
}
void work()
{
    int x,l,len1=-1,len2=-1;
    scanf("%d%d",&l,&x);
    scanf("%s",s+1);
    for (int i=1;i<=l;i++)
        a[i]=s[i]-'i';
    for (int i=l+1;i<=l*4;i++)
        a[i]=a[i-l];

    int now=-100;
    ne_po=1;
    for (int i=1;i<=l*4;i++)
    {
        now=calc(now,a[i]);
        if (now==0 && ne_po==1)
        {
            len1=i;
            break;
        }
    }

    now=-100;
    ne_po=1;
    for (int i=l*4;i>=1;i--)
    {
        now=calc(a[i],now);
        if (now==2 && ne_po==1)
        {
            len2=l*4-i+1;
            break;
        }
    }

    now=-100;
    ne_po=1;
      for (int i=l;i>=1;i--)
        now=calc(a[i],now);

    bool ok=false;
    if (now!=-100)
    {
        if (x%2==0 && x%4!=0) ok=true;
    } else
    {
        if (ne_po==-1 && x%2==1) ok=true;
    }


//    cout<<len1<<' '<<len2<<' '<<ok<<endl;

    if (ok && len1!=-1 && len2!=-1 && len1+len2<=1LL*l*x)
        printf("YES\n"); else printf("NO\n");

}
int main()
{
   // freopen("small.in","r",stdin);
   // freopen("samll.out","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while (T--)
    {
        cas++;
        printf("Case #%d: ",cas);
        work();
    }
}
