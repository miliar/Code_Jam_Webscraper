#include <cstdio>
#include <cstring>
int main()
{
	int T,N;
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d",&N);
		printf("Case #%d: ",tt);
		if(N==0) puts("INSOMNIA");
		else{
			bool mark[10];
			int cnt=10;
			memset(mark,0,sizeof mark);
			int j;
			for(j=1;;j++){
				for(long long M=N*j;M;M/=10)
					if(!mark[M%10]) --cnt,mark[M%10]=true;
				if(!cnt)break;
			}
			printf("%d\n",(long long)N*j);
		}
	}
}
