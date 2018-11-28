#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int main()
{
	//freopen("alarge.out","w",stdout);
	int t; scanf("%d", &t);
	for(int tc=1;tc<=t;tc++)
	{
		int n; scanf("%d", &n);
		printf("Case #%d: ", tc);
		if(n==0) { printf("INSOMNIA\n"); continue; }
		bool udh[15]; memset(udh,false,sizeof(udh));
		int cnt=0, kali=0;
		while(cnt<10)
		{
			kali++;
			int cur=kali*n;
			while(cur>0)
			{
				int dig=cur%10;
				if(!udh[dig]) cnt++;
				udh[dig]=true;
				cur/=10;
			}
		}
		printf("%d\n", kali*n);
	}
	return 0;
}
