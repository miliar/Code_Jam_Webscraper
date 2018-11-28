#include<stdio.h>
#define s(i) scanf("%d",&i)
#define p(i) printf("%d",&i)
#define f(n,i) for(int i=0;i<n;i++)
int max(int a,int b)
{
if(a>b)return a;
return b;
}
int main()
{int t;
s(t);
f(t,k)
{

int n,m;
s(n);s(m);
int r[n],c[m];
f(n,i)r[i]=0;
f(m,i)c[i]=0;
int a[n][m];
f(n,i)
f(m,j)
{s(a[i][j]);//p(i); p(j);
r[i]=max(r[i],a[i][j]);
c[j]=max(c[j],a[i][j]);

}
int flag=0;
f(n,i)
f(m,j)
{//p(a[i][j]);
      if(a[i][j]<r[i]&&a[i][j]<c[j]){//p(r[i]);p(c[j]);
      flag=1;break;}
      if(flag==1)break;}
printf("Case #%d: ",k+1);
if(flag==0)printf("YES\n");
else printf("NO\n");
}
}
