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
	char s[1005];
	int l;

	int casecnt=1;
	testcases
	{
		printf("Case #%d: ",casecnt++);
		sfs(s);
		l=strlen(s);

		int cnt=0;

		for(i=l-1;i>=0;i--)
		{
			if(s[i] == '-')
			{
				cnt++;
				for(j=i;j>=0;j--)
				{
					s[j] = (s[j] == '-')?'+':'-';
				}
			}
		}

		printf("%d\n",cnt);
	}
	return 0;
}