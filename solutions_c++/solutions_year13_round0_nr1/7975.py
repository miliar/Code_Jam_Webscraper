#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<climits>
#include<sstream>

#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<utility>
#include<stack>
#include<queue>
#include<deque>
#include<list>
#include<bitset>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef vector<string> vs; 
typedef pair<int,int> ii;
typedef long long int LLI;
typedef unsigned long long int ULLI;

#define sz(a)                        int((a).size()) 
#define pb                           push_back 
#define mp                           make_pair
#define F                            first
#define S                            second
#define present(c,x)                 ((c).find(x) != (c).end()) 
#define cpresent(c,x)                (find(all(c),x) != (c).end())
#define tr(c,i)                      for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define all(c)                       (c).begin(),(c).end()
#define si(n)                        scanf("%d",&n)
#define sl(n)                        scanf("%lld",&n)
#define sf(n)                        scanf("%f",&n)
#define sd(n)                        scanf("%lf",&n)
#define ss(n)                        scanf("%s",n)

#define abs(x)                       ((x)<0?-(x):(x))
#define fill(a,v)                    memset((a),(v),sizeof (a))
#define INF                          INT_MAX
#define LINF                         (long long)1e18
#define EPS                          1e-9
#define MAX

bool check(char b[][8], char bt[][8], char symb)
{
	char temp[8], dia1[8], dia2[8];

	for(int i=0; i<4; ++i)
	{
		temp[i] = symb;
		dia1[i] = b[i][i];
		dia2[i] = b[i][3-i];
	}
	temp[4] = dia1[4] = dia2[4] = '\0';

	for(int i=0; i<4; ++i)
		if(!strcmp(b[i], temp) || !strcmp(bt[i], temp))
			return true;
	return (!strcmp(dia1, temp) || !strcmp(dia2, temp));
}

int main()
{
	int t;
	char b[8][8], bt[8][8], *p, *pt;
	
	si(t);
	for(int cases=1; cases<=t; ++cases)
	{
		printf("Case #%d: ",cases);
		for(int i=0; i<4; ++i)
			ss(b[i]);

		bool isleft = false;
		for(int i=0; i<4; ++i)
		{
			for(int j=0; j<4; ++j)
			{
				bt[i][j] = b[j][i];
				if(b[j][i] == 'T')
					p = &b[j][i], pt = &bt[i][j];
				isleft |= (b[i][j] == '.');
			}
			bt[i][4] = '\0';
		}

		*p = *pt = 'X';
		if(check(b, bt, 'X'))
		{
			printf("X won\n");
			continue;
		}

		*p = *pt = 'O';
		if(check(b, bt, 'O'))
		{
			printf("O won\n");
			continue;
		}

		if(!isleft)
			printf("Draw\n");
		else
			printf("Game has not completed\n");
	}
	return 0;
}
