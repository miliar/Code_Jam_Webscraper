using namespace std;
#include<iostream>
#include<cstdio>
int main()
{
ios_base::sync_with_stdio(false);
long long int test,j,a,b,k,count;
freopen("C-large-1.in","r",stdin);
freopen("output_c_large.txt","w",stdout);
scanf("%lld",&test);
long long int palin[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001LL,10221412201LL,12102420121LL,12345654321LL,40000800004LL,1000002000001LL,1002003002001LL,1004006004001LL,1020304030201LL,1022325232201LL,1024348434201LL,1210024200121LL,1212225222121LL,1214428244121LL,1232346432321LL,1234567654321LL,4000008000004LL,4004009004004LL};
j=1;
while(test--)
{
scanf("%lld %lld",&a,&b);
count=0;
for(k=0;k<39;k++)
{
if(palin[k]>=a && palin[k]<=b)
count++;
}
printf("Case #%lld: %lld\n",j,count);
j++;
}
return 0;
}
