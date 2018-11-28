#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
map<string,set<int> > mp[10];
int n,x,y,ma;
int nn[1000000];
double c[2010][2010];
double m2[2010];
int main()
{
	m2[0]=1;
	for (int i=0;i<=2000;++i)
	{
		if (i>0)
		{
			m2[i]=m2[i-1]/2;
		}
		for (int j=0;j<=i;++j)
		{
			if (j==0)
			{
				c[i][j]=1;
			}
			else
			{
				c[i][j]=c[i-1][j-1]+c[i-1][j];
			}
		}
	}
	nn[0]=1;
	for (int i=2;i<100000;i+=2)
	{
		nn[i]=nn[i-2]+i*2+1;
		if (nn[i]>2000000)
		{
			ma=i;
			break;
		}
	}	


	freopen("E:\\gcj\\input.in","r",stdin);
	freopen("E:\\gcj\\ouput.txt","w",stdout);
	//freopen("E:\\gcj\\5-5\\ged.txt","r",stdin);
	int T;	
	cin >> T;
	for (int kk=1;kk<=T;++kk)
	{
		cin >> n >> x >> y;
		int ss=abs(x)+y;

		if (ss>=ma)
		{
			printf("Case #%d: %.9lf\n",kk,0);
			continue;
		}
		if (ss==0)
		{
			
				printf("Case #%d: %.9lf\n",kk,1.0);
				
			continue;
		}
		y++;
		if (n<nn[ss-2]+y)
		{
			printf("Case #%d: %.9lf\n",kk,0);
			continue;
		}
		if (n>=nn[ss-2]+ss+y || n>=nn[ss])
		{
			printf("Case #%d: %.9lf\n",kk,1.0);
			continue;
		}
		if (y==ss+1)
		{
			if (n==nn[ss])
			{
				printf("Case #%d: %.9lf\n",kk,1.0);
			}
			else
			{
				printf("Case #%d: %.9lf\n",kk,0.0);

			}
			continue;
		}	
		double p=0;
		int r=n-nn[ss-2];
		for (int j=y;j<=r;++j)
		{
			p+=m2[r]*c[r][j];
		}
		printf("Case #%d: %.9lf\n",kk,p);

		//printf("Case #%d: %lld\n",kk,ans);
	}
	return 0;
}