#include <iostream>

using namespace std;
long long array[] = {1,4,9,121,484,10201,12321,14641,40804,44944,1234321,4008004,102030201,104060401,121242121,123454321,125686521,404090404,10221412201ll,12102420121ll,12345654321ll,1020304030201ll,1022325232201ll,1024348434201ll,1212225222121ll,1214428244121ll,1232346432321ll,1234567654321ll,4004009004004ll};
int main()
{
    int n,rr=1;
    scanf("%d",&n);
    while(n--)
    {
        long long a,b;
        scanf("%I64d %I64d",&a,&b);
        int cnt=0;
        for (int i=0;i<sizeof(array)/sizeof(long long);i++)
        {
            if (array[i]>=a && array[i]<=b) cnt++;
        }

        printf("Case #%d: %d\n",rr++,cnt);
    }

    return 0;
}
