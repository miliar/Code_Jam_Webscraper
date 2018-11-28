#include <cstdio>
#include <cstring>

bool pail(long long x){
	char s[100];
	sprintf(s,"%lld",x);
	int len=strlen(s);
	for (int i=0;i<len/2;i++)
		if (s[i]!=s[len-i-1])
			return false;
	return true;
}
long long A[100];
int num=0;
int main()
{
	int cnt=0;
	for (long long i=1;i*i<=100000000000000LL;i++)
		if (pail(i)&&pail(i*i)){
			A[num++]=i*i;
			//printf("%lld %lld\n",i,i*i);
			cnt++;
		}
	//printf("%d\n",cnt);
	int cases;
	scanf("%d",&cases);
	long long L,R;
	for (int t=1;t<=cases;t++){
		scanf("%lld %lld",&L,&R);
		int ans=0;
		for (int i=0;i<num;i++)
			if (L<=A[i]&&A[i]<=R)
				ans++;
		printf("Case #%d: %d\n",t,ans);
	}
}

