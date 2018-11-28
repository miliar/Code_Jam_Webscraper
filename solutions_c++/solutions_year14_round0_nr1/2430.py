#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	freopen("in.txt","rt",stdin);
	freopen("Aout.txt","wt",stdout);

	int TC;
	cin>>TC;
	int x,arr[20],n;
	for(int tc=0;tc<TC;++tc)
	{
		memset(arr,0,sizeof(arr));
		int ans = 0;
		for(int t=0;t<2;t++)
		{
			cin>>x;
			x--;
			for(int i=0;i<4;i++)
				for(int j=0;j<4;j++)
				{
					cin>>n;
					if( i == x )
						arr[n]++;
					if( arr[n] > 1 )
						ans = ans ? -1 : n;
				}
		}
		printf("Case #%d: ",tc+1);
		if( ans == -1 ) printf("Bad magician!");
		else if(ans == 0) printf("Volunteer cheated!");
		else printf("%d",ans);
		printf("\n");
	}
	return 0;
}