#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int m[6][6];

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);

	int i,j,k,x,r,c,t,cases;
	string gb = "GABRIEL",rc = "RICHARD",ans;
	scanf("%d",&cases);
	m[3][2] = m[2][3] = 1;
	m[3][3] = 1;
	m[3][4] = m[4][3] = 2;
	m[1][4] = m[4][1] = 1;
	m[2][4] = m[4][2] = 1;
	m[3][4] = m[4][3] = 2;
	m[4][4] = 2;

	for(t = 1;t<=cases;t++)
	{
		scanf("%d%d%d",&x,&r,&c);
		if(x == 1)
		{
			ans = gb;
		}
		else if(x == 2)
		{

			if((r*c)%2 == 0)
				ans = gb;
			else
				ans = rc;
		}
		else if(x == 3)
		{

			if(min(r,c) >=2 && (r*c)%3 == 0)
				ans = gb;
			else
				ans = rc;
		}
		else
		{
			if(min(r,c) >=2 && max(r,c) >=3)
			{
				if(m[r][c] == 2)
					ans = gb;
				else if(m[r][c] == 1)
					ans = rc;

			}
			else
			{
				ans = rc;
			}
		}

		cout <<"Case #"<<t<<": "<<ans<<endl;

	}

	return 0;
}
