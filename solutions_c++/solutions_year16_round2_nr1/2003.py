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
#define INF 1000000000
#define pb push_back
#define mp make_pair
#define fr first 
#define sc second
#define testcases scanf("%d",&t);while(t--)
#define ffor(a,b,c) for(a=b;a<c;a++)
#define rfor(a,b,c) for(a=b;a>=c;a--)

ll power(ll base, ll exp)
{
	if(exp == 0)
	return 1;
	ll r = power(base, exp/2);
	r=(r*r)%mod;
	if(exp&1)
		r=(r*base)%mod;
	return r;
}

/**********************************************/

int hashh[26]={0};
int l;
vector< int > ans;

void add(int no, int times)
{
	int i;
	for(i=0;i<times;i++)
		ans.pb(no);
}

void sub(string str,int times)
{
	int i;
	for(i=0;i<str.length();i++)
		hashh[str[i] - 'A']-=times;
}

void doit()
{
	int no;
	no= hashh['Z'-'A'];
	add(0, no);
	sub("ZERO", no);

	no= hashh['G'-'A'];
	add(8, no);
	sub("EIGHT", no);

	no= hashh['X'-'A'];
	add(6, no);
	sub("SIX", no);

	no= hashh['U'-'A'];
	add(4, no);
	sub("FOUR", no);

	no= hashh['W'-'A'];
	add(2, no);
	sub("TWO", no);

	no= hashh['R'-'A'];
	add(3, no);
	sub("THREE", no);

	no= hashh['F'-'A'];
	add(5, no);
	sub("FIVE", no);

	no= hashh['V'-'A'];
	add(7, no);
	sub("SEVEN", no);

	no= hashh['O'-'A'];
	add(1, no);
	sub("ONE", no);

	no= hashh['I'-'A'];
	add(9, no);
	sub("NINE", no);
}	

int main()
{
	int i,j,t;
	int casecnt=1;
	char s[2005];

	testcases
	{
		ans.clear();
		memset(hashh, 0 , sizeof(hashh));
		printf("Case #%d: ",casecnt++);

		sfs(s);
		l = strlen(s);

		for(i=0;i<l;i++)
			hashh[s[i] - 'A']++;

		doit();

		sort(ans.begin(), ans.end());
		for(i=0;i<ans.size();i++)
			printf("%d",ans[i]);
		printf("\n");
	}
	return 0;
}