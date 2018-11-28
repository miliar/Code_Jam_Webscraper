#include<stdio.h>
#include<stdlib.h>
#include<math.h>
long long int a[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,
1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004};

int main()
{
        //freopen("C:\\Users\\lovelotus\\Desktop\\input.txt","r",stdin);
        //freopen("C:\\Users\\lovelotus\\Desktop\\output.txt","w",stdout);
    long long int i,j,x,y,n,cnt,l;
    int k=39,t,k1;
    j=0;
    scanf("%d",&t);
    k1=1;
    while(t--)
    {
        scanf("%lld %lld",&x,&y);
        cnt=0;
        for(i=0;i<k;i++)
        {
            if(a[i]>=x && a[i]<=y) cnt++;
        }
        printf("Case #%d: %lld\n",k1++,cnt);
    }
    return 0;
}
