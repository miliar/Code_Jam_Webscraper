#include<bits/stdc++.h>
using namespace std;
int main()
{
int t;
scanf("%d",&t);
int p=1;
while(t--)
{
int n;
scanf("%d",&n);
if(n==0)
{
cout<<"Case #"<<p<<": ";
cout<<"INSOMNIA\n";
p++;
continue;
}
int a[11];
for(int i=0;i<=9;i++)
                a[i]=-1;
                int ans=0;
for(int i=1;;i++)
{
    int x=n*i,y=0;
    while(x>0)
    {
       a[x%10]=x%10;
       x=x/10;
    }
    for(int j=0;j<=9;j++)
    {
                    if(a[j]==j)
                                y++;
    }
    if(y==10)
    {
                    ans=i*n;
                    break;
    }
}
cout<<"Case #"<<p<<": ";
cout<<ans<<endl;
p++;
}
return 0;
}
