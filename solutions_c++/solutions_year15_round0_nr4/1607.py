#include<cstdio>
#include<vector>
#include<cstring>
#include<algorithm>

using namespace std;

int main()
{
	int T;
	scanf("%d",&T);
	for(int ix=0;ix<T;ix++)
	{
		int ans;  //0 is richard 1 is gaby
		int x,r,c;
		scanf("%d %d %d",&x,&r,&c);
		if(r*c%x!=0)
			ans = 0;
		else if(x == 1)
			ans = 1;
		else if (x==2)
			ans = 1;
		else if(x==3)
		{
			if(r*c==3)
				ans = 0;
			else
				ans = 1;
		}
		else if(x==4)
		{
			if(r*c<=8)
				ans = 0;
			else
				ans = 1;
		}
		printf("Case #%d: ",ix+1);
		if(ans == 0)
			printf("RICHARD\n");
		else
			printf("GABRIEL\n");
	}
}