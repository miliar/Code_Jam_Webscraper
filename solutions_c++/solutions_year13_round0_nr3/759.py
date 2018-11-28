#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;

long long int s[1000]={0,1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004LL,404090404LL,10000200001LL,10221412201LL,12102420121LL,12345654321LL,40000800004LL,1000002000001LL,1002003002001LL,1004006004001LL,1020304030201LL,1022325232201LL,1024348434201LL,1210024200121LL,1212225222121LL,1214428244121LL,1232346432321LL,1234567654321LL,4000008000004LL,4004009004004LL,100000020000001LL,100220141022001LL,102012040210201LL,102234363432201LL,121000242000121LL,121242363242121LL,123212464212321LL,123456787654321LL,400000080000004LL};
int main()
{
    freopen("C-large-1.in","r",stdin);
    freopen("out2.txt","w",stdout);
    int amm;
    scanf("%d",&amm);
    for (int count=1;count<=amm;count++)
    {
        long long int a,b;
        scanf("%lld%lld",&a,&b);
        int A=lower_bound(s,s+50,a)-s,B=lower_bound(s,s+50,b)-s;
        if (s[A]>=a)A--;
        if (s[B]>b)B--;
        //printf("   %d  %d\n",A,B);
        printf("Case #%d: %d\n",count,B-A);
    }
    return 0;
}
