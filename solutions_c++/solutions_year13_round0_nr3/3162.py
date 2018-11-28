#include<cstdio>
#include<cstring>

int a[100];
void judge()
{
    a[0]=1;
    a[1]=4;
    a[2]=9;
    int j=3;
    for(int i=11;i<=31;i++){
	   if(i%10==i/10)
	   {
         int tp=i*i;
         if(tp/100==tp%10)
           a[j++]=tp;
	   }
    }
}
int main()
{
    int t,x,y,i,cas=0;
	freopen("C-small-attempt4.in","r",stdin);
	freopen("C-small-attempt4.out","w",stdout);
    scanf("%d",&t);
    judge();
    while(t--)
    {
        int ans=0;
        scanf("%d%d",&x,&y);
        for(i=0;;i++){
           if(a[i]>=x&&a[i]<=y)
               ans++;
           if(a[i]==484)
              break;
              // printf("%d ",a[i]);
        }
        printf("Case #%d: ",++cas);
        printf("%d\n",ans);
    }
	return 0;
}
