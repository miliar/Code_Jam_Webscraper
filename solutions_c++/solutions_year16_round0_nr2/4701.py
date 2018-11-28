#include<bits/stdc++.h>
#define ll long long 
#define pb push_back
#define mp make_pair
#define si(i) scanf("%d",&t)
#define fs first
#define sc second
#define FOR(i,j,k) for(int i=0;i<k;i++)
#define REP(i,k) for(int i=0;i<k;i++)
#define FORR(i,j,k) for(int i=n;i>=k;i--)
#define MOD 1000000007
using namespace std;
int main()
{
	//Let's start
	int t;
	int arr[105];
	int test[105];
	si(t);
	char ch[105];
	int Case=1;
	while(t--)
	{
		scanf("\n%s",ch);
		int l = strlen(ch);
		REP(i,l)
		{
			if(ch[i] == '+')
				arr[i] = 1;
			else
				arr[i] = 0;
		}
		int count =0;
		int x = 0;
		int y = l-1;
		while(x<=y)
		{
			int flag =0;
			while(arr[y] == 1)
			{
				y--;
			}
			for(x=0;x<=y;x++)
			{
				if(arr[x] == 1)
				{
					flag =1;
					continue;
				}
				else
				{
					if(flag == 1)
						count++;
					break;
				}
			}
			for(;x<=y;x++)
			{
				if(arr[x] == 0 && x!=y)
					continue;
				{
					count++;
					break;
				}
			}
			int j = 0;
			for(j=0;j<(y-x+1);j++)
			{
				test[j] = arr[y-j] == 0 ? 1:0;
				//cout << arr[y-j] <<" " << y-j << " " << arr[j]<< endl;
			}
			REP(i,y+1)
			{
				arr[i] = test[i];
			}
			y=j-1;
			x=0;
		}
		printf("Case #%d: %d\n",Case++,count);
	}
	return 0;
}