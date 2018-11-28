#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
//string a1[200],a2[200];
//string ans1,ans2;
//int b1[100005],b2[100005],n;
int a[10005],b[10005],ans[10005];

typedef pair<int,int> ii;
ll z;
ll q;
int flag=0;
int check()
{
    int n=z,i;
    for(i=0;i<n;i++)
    ans[i]=a[i];
           /* for(i=0;i<z;i++)
            {
                if(ans[i]==0)
                printf("P");
                if(ans[i]==1)
                printf("S");
                if(ans[i]==2)
                printf("R");
            }
            printf("\n");*/

    while(n!=1){
    for(i=0;i<n;i=i+2)
    {
        if(a[i]==a[i+1])
        return 0;
        if(a[i]>a[i+1])
        {
            if(a[i]==2 && a[i+1]==0)
            {
                b[i/2]=0;
            }
            else
            {
                b[i/2]=a[i];
            }
        }
        else
        {
            if(a[i]==0 && a[i+1]==2)
            {
                b[i/2]=0;
            }
            else
            {
                b[i/2]=a[i+1];
            }
        }
    }
    n=n/2;
    for(i=0;i<n;i++)
    a[i]=b[i];
    }

    return 1;
}
void func(int n,int c,int r,int s,int p)
{
 int i;
     if(flag==1)
        return ;
         //printf("%d %d %d %d %d\n",n,c,r,s,p);
    if(n==z)
    {
        if(flag==1)
        return ;

        flag=check();
        for(i=0;i<z;i++)
    a[i]=ans[i];
        if(flag==1)
        return ;
    }
    if(p>0)
    {
        int q=a[n];
        a[n]=0;
        //if(n==0)
        //printf("yo\n");
        func(n+1,0,r,s,p-1);
        a[n]=q;
    }
    if(r>0)
    {
        int q=a[n];
        a[n]=2;
        func(n+1,2,r-1,s,p);
        a[n]=q;
    }
    if(s>0)
    {
        int q=a[n];
        a[n]=1;
        func(n+1,1,r,s-1,p);
        a[n]=q;
    }

}


int main()
{
    ll t,i,j,c=1,k,n,r,p,s;

    freopen("A-small-attempt3.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%lld",&t);
    while(t--)
    {
        scanf("%lld%lld%lld%lld",&n,&r,&p,&s);
        q=n;
        z=pow(2,n);
        flag=0;

        func(0,-1,r,s,p);
        printf("Case #%lld: ",c++);
        if(flag==1)
        {
            for(i=0;i<z;i++)
            {
                if(ans[i]==0)
                printf("P");
                if(ans[i]==1)
                printf("S");
                if(ans[i]==2)
                printf("R");
            }
        }
        else
        {
            printf("IMPOSSIBLE");
        }


         printf("\n");

            //printf("%lld\n",p);


    }
    return 0;
}
