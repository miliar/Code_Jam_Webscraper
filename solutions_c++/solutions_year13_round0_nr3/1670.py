#include<stdio.h>
#include<vector>
#include<algorithm>

std::vector<long long> su;

bool isPalin(long long x)
{
	long long tmp=x,mul=1,su=0;
	while(x>mul*10)mul*=10;
	while(x>0){
		su+=mul*(x%10);
		x/=10; mul/=10;
	}
	if(tmp==su)return true;
	return false;
}

void setting()
{
	long long i;
	for(i=1;i<=10000000;i++){
		if(isPalin(i)&&isPalin(i*i))su.push_back(i*i);
	}
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,T;
	long long a,b;
	setting();
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		printf("Case #%d: ",t);
		scanf("%lld%lld",&a,&b);
		printf("%d\n",std::upper_bound(su.begin(),su.end(),b)-std::upper_bound(su.begin(),su.end(),a-1));
	}
}