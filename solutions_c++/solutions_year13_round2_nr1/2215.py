#include<cstdio>
//#include<conio.h>
#include<algorithm>
using namespace std;
int a[20],s,i,ans,n;
int fun(int s,int i,int ans)
{
    //printf("%d %d %d\n",s,i,ans);
    if(i==n)
    return ans;
    if(a[i]<s)
    return fun(s+a[i],i+1,ans);
    
    else
    {
        return min(fun(s+s-1,i,ans+1), fun(s,i+1,ans+1));
    }
    return ans;
}
int main()
{
    freopen("C:\\Users\\dell\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\dell\\Desktop\\output.txt","w",stdout);
    int t,x=1;
    scanf("%d",&t);
    while(t--)
    {
    scanf("%d %d",&s,&n);
    for(i=0;i<n;i++)
    scanf("%d",&a[i]);
    sort(a,a+n);
    if(s==1)
    printf("Case #%d: %d\n",x,n);
    else
    printf("Case #%d: %d\n",x,fun(s,0,0));
    x++;
    }
    //getch();
    return 0;
}
               
    
    
