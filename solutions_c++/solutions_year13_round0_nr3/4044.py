#include<cstdio>
#include<cmath>

int main()
{
    long long int t, A, B, i, count, j;
    long long int arr[39] = {  1ll, 4ll, 9ll,
                    121ll, 484ll,

                    10201ll, 12321ll, 14641ll,
                    40804ll, 44944ll,

                    1002001ll, 1234321ll,
                    4008004ll,

                    100020001ll, 102030201ll, 104060401ll,
                    121242121ll, 123454321ll, 125686521ll,

                    400080004ll, 404090404ll,

                    10000200001ll, 10221412201ll,
                    12102420121ll, 12345654321ll,

                    40000800004ll,

                    1000002000001ll, 1002003002001ll,
                    1004006004001ll, 1020304030201ll,
                    1022325232201ll, 1024348434201ll,
                    1210024200121ll, 1212225222121ll,
                    1214428244121ll, 1232346432321ll,
                    1234567654321ll,

                    4000008000004ll, 4004009004004ll,
                   };
    
    scanf("%d",&t);
    
    for(j=1;j<=t;j++)
    {
        count=0;
        scanf("%lld%lld",&A,&B);
        for(i=0;i<39;i++)
        {
            if(arr[i]>=A&&arr[i]<=B)
            {
                count++;
            }
        }
        printf("Case #%lld: %lld\n",j,count);
    }
}
