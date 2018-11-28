#include<cstdio>
//#include<conio.h>
int main()
{
    freopen("C:\\Users\\dell\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\dell\\Desktop\\output.txt","w",stdout);
    long long n[39]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001ll,10221412201ll,12102420121ll,12345654321ll,40000800004ll,1000002000001ll,1002003002001ll,1004006004001ll,1020304030201ll,1022325232201ll,1024348434201ll,1210024200121ll,1212225222121ll,1214428244121ll,1232346432321ll,1234567654321ll,4000008000004ll,4004009004004ll},t,x=1,a,b,no,i;
    scanf("%lld",&t);
    while(t--)
    {
    scanf("%lld %lld",&a,&b);
    no=0;
    for(i=0;i<39;i++)
    {
        if(n[i]>=a && n[i]<=b)
        no++;  
    }
    printf("Case #%lld: %lld\n",x,no);
    x++;
    }
    //getch();
    return 0;
    
}
          
