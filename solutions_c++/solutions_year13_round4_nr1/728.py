#include<cstdio>
#include<algorithm>
using namespace std;
struct node
{
       long long x,num;
       int kind;
}a[2001];
int n,m,top;
long long old,ans,stk1[1001],stk2[1001];
__inline bool cmp1(node a,node b)
{
         return a.x<b.x||a.x==b.x&&a.kind<b.kind;
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,test,tt;
    scanf("%d",&test);
    for(tt=1;tt<=test;tt++)
    {
    scanf("%d%d",&n,&m);
    printf("Case #%d: ",tt);
    ans=0;
    old=0;
    for(i=1;i<=m;i++)
    {
      long long st,en,num;
      scanf("%I64d%I64d%I64d",&st,&en,&num);
      a[(i<<1)-1].x=st;
      a[(i<<1)-1].num=num;
      a[(i<<1)-1].kind=0;
      a[i<<1].x=en;
      a[i<<1].num=num;
      a[i<<1].kind=1;
      old+=(en-st)*(en-st-1)/2%1000002013*num%1000002013;
    }
    sort(&a[1],&a[m<<1]+1,cmp1);
    for(i=1;i<=m<<1;i++)
    {
      long long st,en,num;
      if(a[i].kind==0)
      {
        stk1[++top]=a[i].x;
        stk2[top]=a[i].num;
      }
      else
      {
        while(a[i].num>stk2[top])
        {
          st=stk1[top];
          en=a[i].x;
          num=stk2[top];
          ans+=(en-st)*(en-st-1)/2%1000002013*num%1000002013;
          a[i].num-=stk2[top];
          top--;
        }
        st=stk1[top];
        en=a[i].x;
        num=a[i].num;
        ans+=(en-st)*(en-st-1)/2%1000002013*num%1000002013;
        stk2[top]-=a[i].num;
        if(stk2[top]==0)top--;
      }
    }
      /*if(a[i].num>b[j].num)
      {
        st=a[i].x;
        en=b[j].x;
        num=a[i].num-b[j].num;
        ans+=(en-st)*(en-st-1)/2%1000002013*num%1000002013;
        a[i].num-=b[j].num;
        j++;
      }
      else if(a[i].num<b[j].num)
      {
        st=a[i].x;
        en=b[j].x;
        num=b[j].num-a[i].num;
        ans+=(en-st)*(en-st-1)/2%1000002013*num%1000002013;
        b[j].num-=a[i].num;
        i++;
      }
      else
      {
        st=a[i].x;
        en=b[j].x;
        num=a[i].num;
        ans+=(en-st)*(en-st-1)/2%1000002013*num%1000002013;
        i++;
        j++;
      }*/
    ans-=old;
    if(ans<0)ans+=1000002013;
    ans%=1000002013;
    printf("%I64d\n",ans);
    }
    return 0;
}
