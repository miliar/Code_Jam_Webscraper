#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

long long tab[40]={1LL,4LL,9LL,121LL,484LL,10201LL,12321LL,14641LL,40804LL,44944LL,1002001LL,1234321LL,4008004LL,100020001LL,
102030201LL,104060401LL,121242121LL,123454321LL,125686521LL,400080004LL,404090404LL,10000200001LL,10221412201LL,12102420121LL,
12345654321LL,40000800004LL,1000002000001LL,1002003002001LL,1004006004001LL,1020304030201LL,1022325232201LL,1024348434201LL,
1210024200121LL,1212225222121LL,1214428244121LL,1232346432321LL,1234567654321LL,4000008000004LL,4004009004004LL,100000000000014LL};

/*bool palindrome(const long long k)
{
  long long rev=0LL,temp=k;
  while(temp)
  {
    rev*=10LL;rev+=temp%10LL;
    temp/=10LL;
  }
  return rev==k;
}
void init()
{
  for(long long k=1LL;k*k<M;k++)
  {
    //if(k%1000LL==0)printf("%lld\n",k);
    if(palindrome(k)&& palindrome(k*k))V.push_back(k*k);
  }
   printf("koncze\n");
} */
int solve()
{
  long long a,b;
  scanf("%lld%lld",&a,&b);
  return upper_bound(tab,tab+40,b)-upper_bound(tab,tab+40,a-1);
}
int main()
{
    //init();
    //for(int i=0;i<V.size();i++)printf("%lld,",V[i]);
    //for(int i=0;i<100;i++)printf("%d %d\n",i,upper_bound(V.begin(),V.end(),i)-V.begin());
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++)printf("Case #%d: %d\n",i+1,solve());
    return 0;
}
