#include<cstdio>
#include<cstring>
#include<algorithm>
#include<map>
const int mod = 1000000007;
using namespace std;
int flag[1010];

bool judge(int num)
{
	int dig[20],tot=0;
	for(;num;num/=10) dig[tot++]=num%10;
	for(int i=0;i<=tot/2;i++) if(dig[i]!=dig[tot-1-i])return false;
	return true;
}
int main()
{
	for(int i=1;i*i<=1000;i++) flag[i*i]=i;
	int t,ca=1,a,b;
	freopen("C-small-attempt4.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&a,&b);
		int ans = 0;
		for(int i=a;i<=b;i++)
		{
			if(flag[i]&&judge(i)&&judge(flag[i])){
			//	printf("i=%d\n",i);
				ans++;
			}
		}
		printf("Case #%d: %d\n",ca++,ans);
	}
	return 0;
}