#include<stdio.h>
#include<string.h>
#include<vector>
using namespace std;
bool isPalin(long long x)
{
    char buf[25];
    sprintf(buf,"%lld",x);
    int len=strlen(buf);
    for (int i =0;i<len/2;i++)
	if(buf[i]!=buf[len-i-1]) return false;
    return true;

}
vector<long long> v;
int main()
{
    for (long long i=1;i<=10000000;i++)
	if(isPalin(i) && isPalin(i*i))
	    v.push_back(i*i);
    int zes;scanf("%d",&zes);
    for (int z=0;z<zes;z++)
    {
	long long a,b;
	scanf("%lld %lld",&a,&b);
	int res=0;
	for (int i =0;i<v.size();i++)
	    if(v[i]>=a && v[i]<=b) res++;
	printf("Case #%d: %d\n",z+1,res);

    }
}
