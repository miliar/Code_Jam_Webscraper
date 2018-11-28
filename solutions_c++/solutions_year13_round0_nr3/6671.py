#include<cstdio>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<cmath>
using namespace std;
int x[1005];
int ans[1005];
int func(int num)
{
        char a[13],b[13];
        int j,k,size;

        itoa(num,a,10);
        for(j=0;a[j];j++);
        size=j;
        j--;
        for( k=0;k<=size-1;k++)
        {
            b[k]=a[j];
            j--;


        }
        b[k]=0;
        int tmp=atoi(b);

        if(tmp==num) return 1;
        return 0;

}
void make()
{
    for(int i=1;i<=31;i++) {if(func(i*i)) x[i*i]=1;}

    for(int i=1;i<1005;i++)
    {
        if(x[i]==1)
        {
            int c=sqrt(i*1.);
            if( func(c)) {x[i]=1;}
            else x[i]=0;
        }
    }

    ans[0]=0;
    for(int i=1;i<1005;i++)
    {
        if(x[i]==1) ans[i]=ans[i-1]+1;
        else ans[i]=ans[i-1];
    }
}


int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("b.txt","w",stdout);
    make();
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        int a,b;
        scanf("%d %d",&a,&b);
        printf("Case #%d: %d\n",i,ans[b]-ans[a-1]);

    }
    return 0;
}
