/*
    Author:-Sarthak Taneja
    CSE 2nd year,MNNIT Allahabad
*/
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair< int,int > ii;
typedef vector< ii > vii;

#define sfd(x) scanf("%d",&x)
#define sfs(x) scanf("%s",x)
#define sff(x) scanf("%lf",&x)
#define mod 1000000007
#define MAX 1000000
#define pb push_back
#define mp make_pair
#define fr first 
#define sc second
#define testcases scanf("%d",&t);while(t--)
#define ffor(a,b,c) for(a=b;a<c;a++)
#define rfor(a,b,c) for(a=b;a>=c;a--)

int main()
{
	int i,j,t;
	int n;

	int casecnt=1;
	testcases
	{
		printf("Case #%d: ",casecnt++);
		int digit[10]={0};
		int cnt=0;
		sfd(n);

		if(n == 0)
		{
			printf("INSOMNIA\n");
		}
		else
		{
			int x=0;
			while(cnt < 10)
			{
				x+=n;
				int y=x;
				while(y)
				{
					if(digit[y%10] == 0)
					{
						digit[y%10]=1;
						cnt++;
					}
					y/=10;
				}
			}

			printf("%d\n",x);
		}
	}
	return 0;
}