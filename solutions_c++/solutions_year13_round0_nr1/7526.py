
// Standard includes
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<limits.h>
#include<string.h>
#include<sstream>

//Data Structures
#include<algorithm>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<utility>
#include<stack>
#include<queue>
using namespace std;

#define FOR(i,a,b)  for(int i= (int )a ; i < (int )b ; ++i)
#define rep(i,n)    FOR(i,0,n)
#define INF     INT_MAX
#define ALL(x)      x.begin(),x.end()
#define LET(x,a)    __typeof(a) x(a)
#define IFOR(i,a,b)     for(LET(i,a);i!=(b);++i)
#define EACH(it,v)  IFOR(it,v.begin(),v.end())
#define pb      push_back
#define sz(x)       int(x.size())
#define mp      make_pair
#define fill(x,v)   memset(x,v,sizeof(x))
#define si(n)       scanf("%d",&n)
#define pi(n)       printf("%d ",n)
#define pil(n)      printf("%d\n",n)
#define sl(n)       scanf("%lld",&n)
#define sd(n)       scanf("%lf",&n)
#define ss(n)       scanf("%s",n)

typedef pair<int,int> PI;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

int main()
{
	int t,i;
	char str[5][5];
	int xwon,twon,count=1;
	int emptyflag=0;
	scanf("%d",&t);
	while(count <= t)
	{
		emptyflag=0;
		xwon=0;
		twon=0;
		for(i=0;i<4;i++)
		{
			scanf("%s",str[i]);
		}
		for(i=0;i<4;i++)
		{
			if((str[i][0] == 'X' || str[i][0] == 'T') && (str[i][1] == 'X' || str[i][1] == 'T') && (str[i][2] == 'X' || str[i][2] == 'T') && (str[i][3] == 'X' || str[i][3] == 'T'))
				xwon=1;

			else if((str[i][0] == 'O' || str[i][0] == 'T') && (str[i][1] == 'O' || str[i][1] == 'T') && (str[i][2] == 'O' || str[i][2] == 'T') && (str[i][3] == 'O' || str[i][3] == 'T'))
				twon=1;
			
			if(str[i][0] == '.' || str[i][1] == '.'  || str[i][2] == '.' || str[i][3] == '.')
				emptyflag=1;
			
		}

		for(i=0;i<4;i++)
		{
			if((str[0][i] == 'X' || str[0][i] == 'T') && (str[1][i] == 'X' || str[1][i] == 'T') && (str[2][i] == 'X' || str[2][i] == 'T') && (str[3][i] == 'X' || str[3][i] == 'T'))
				xwon=1;

			else if((str[0][i] == 'O' || str[0][i] == 'T') && (str[1][i] == 'O' || str[1][i] == 'T') && (str[2][i] == 'O' || str[2][i] == 'T') && (str[3][i] == 'O' || str[3][i] == 'T'))
				twon=1;
		}

		if((str[0][0] == 'X' || str[0][0] == 'T') && (str[1][1] == 'X' || str[1][1] == 'T') && (str[2][2] == 'X' || str[2][2] == 'T') && (str[3][3] == 'X' || str[3][3] == 'T'))
			xwon=1;

		else if((str[0][0] == 'O' || str[0][0] == 'T') && (str[1][1] == 'O' || str[1][1] == 'T') && (str[2][2] == 'O' || str[2][2] == 'T') && (str[3][3] == 'O' || str[3][3] == 'T'))
			twon=1;

		if((str[0][3] == 'X' || str[0][3] == 'T') && (str[1][2] == 'X' || str[1][2] == 'T') && (str[2][1] == 'X' || str[2][1] == 'T') && (str[3][0] == 'X' || str[3][0] == 'T'))
			xwon=1;
		else if((str[0][3] == 'O' || str[0][3] == 'T') && (str[1][2] == 'O' || str[1][2] == 'T') && (str[2][1] == 'O' || str[2][1] == 'T') && (str[3][0] == 'O' || str[3][0] == 'T'))
			twon=1;

		if(xwon == 1)
			cout << "Case #" << count << ": X won" << endl;
		else if(twon == 1)
			cout << "Case #" << count << ": O won" << endl;
		else if(xwon == 0 && twon == 0)
		{
			if(emptyflag == 1)
				cout << "Case #" << count << ": Game has not completed" << endl;
			else 
				cout << "Case #" << count << ": Draw" << endl;
		}
		count++;
	}			

	return 0;
}
