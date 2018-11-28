//A
#include <iostream>
#include <cstdio>
#include <cstring>
#define db(x) cout<<#x<<" "<<(x)<<" "
#define el cout<<endl
using namespace std;
int cas,tcas;

namespace solve{
	int usd[10];
	int N;
	void update(int x)
	{
		for(;x;x/=10)
		{
			usd[x%10]=1;
		}
	}
	void solve(){
		scanf("%d",&N);
		if(N==0)
		{
			puts("INSOMNIA");
			return;
		}
		
		memset(usd,0,sizeof(usd));
		for(int i=1;i<100;i++)
		{
			update(i*N);
			int flag=1;
			for(int k=0;k<10;k++)if(!usd[k])
			{
				flag=0;break;
			}
			if(flag)
			{
				printf("%d\n",i*N);
				return;
			}
		}
		//puts("???");
		puts("INSOMNIA");
	}
}


int main() {
	//freopen("A.in","r",stdin);
	//freopen("A.out","w",stdout);
	scanf("%d",&cas);
	for(tcas=0;tcas<cas;tcas++){
		printf("Case #%d: ",tcas+1);
		solve::solve();
	}
	return 0;
}
