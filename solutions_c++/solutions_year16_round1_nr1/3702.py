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

char s[1005];
int l;
int final[3005];
int start=1500;
int end=1500;

int main()
{
	int i,j,t;

	int casecnt=1;
	testcases
	{
		start=1500;
		end=1500;
		printf("Case #%d: ",casecnt++);
		sfs(s);
		l= strlen(s);
		final[end++]=s[0];
		for(i=1;i<l;i++)
		{
			if(s[i] >= final[start])
				final[--start]=s[i];
			else
				final[end++]=s[i];
		}
		for(i=start;i<end;i++)
			printf("%c",final[i]);
		printf("\n");
	}
	return 0;
}