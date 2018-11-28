#include <cstdlib>  
#include <cctype>  
#include <cstring>  
#include <cstdio>  
#include <cmath>  
#include <algorithm>  
#include <vector>  
#include <string>  
#include <iostream>  
#include <sstream>  
#include <map>  
#include <set>  
#include <queue>  
#include <stack>  
#include <fstream>  
#include <numeric>  
#include <iomanip>  
#include <bitset>  
#include <list>  
#include <stdexcept>  
#include <functional>  
#include <utility>  
#include <ctime>  
using namespace std;  

#define PB push_back  
#define MP make_pair  

#define REP(i,n) for(i=0;i<(n);++i)  
#define FOR(i,l,h) for(i=(l);i<=(h);++i)  
#define FORD(i,h,l) for(i=(h);i>=(l);--i)  
#define CLOCK cout << "Clock " << (double)clock()/CLOCKS_PER_SEC << endl
const int maxs = 103;

int main()
{
	freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	int num[maxs][maxs];
	int n,m;
	for(int cases=1;cases<=t;cases++)
	{
		scanf("%d %d",&n,&m);
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++)
				scanf("%d",&num[i][j]);
		bool suc = true;
		for (int i=0;suc && i<n;i++)
		{
			for (int j=0;suc && j<m;j++)
			{
				int tmp = num[i][j];
				bool smaller = false,bigger = false;
				for (int k=0;k<m;k++)
				{
					if (num[i][k]<tmp) smaller=true;
					else if(num[i][k]>tmp) bigger = true;
				}
				if (!smaller && !bigger) ;
				else if(!smaller && bigger)
				{
					for (int k=0;k<n;k++)
					{
						if (num[k][j] > tmp) suc = false;
					}
				}
				else if(smaller && !bigger)
				{
					;
				}
				else if(smaller && bigger)
				{
					for (int k=0;k<n;k++)
					{
						if (num[k][j] > tmp) suc = false;
					}
				}
			}
		}
		printf("Case #%d: ",cases);
		if (suc) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}