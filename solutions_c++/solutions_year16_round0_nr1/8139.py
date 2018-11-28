#include<bits/stdc++.h>
using namespace std;
int check(int *a)
{
    int i;
    for(i=0;i<10;i++)
        if(a[i]==0)
            return 1;
    return 0;    
}
int main()
{
//    FILE *fp;
//    FILE *fr;
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,z=1;
    scanf("%d",&t);
    //printf("hi1\n");

    while(z<=t)
    {
        long long n,temp,k=1;
        int x;
        scanf("%lld",&n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",z);
            z++;continue;
        }
        int a[10];
        memset(a,0,sizeof(a));
//        printf("hi1\n");
        
        while(check(a))
        {   
            n=n*k;
            temp=n;
            while(temp!=0)
            {
                x=temp%10;
                a[x]=1;
                temp/=10;
            }    
            n/=k;
            k++;
        }
        printf("Case #%d: %lld\n",z,n*(k-1));
        z++;
    }
//    fclose(fp);
//    fclose(fr);
    return 0;
}