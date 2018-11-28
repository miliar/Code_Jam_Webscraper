
#include <sstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <iomanip>
#include <map>
#include <set>
#include <cmath>
#include <list>
#include <cassert>


using namespace std;
#pragma comment(linker, "/STACK:50000000")


string problem_name = "A-large(5)";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
 freopen((problem_name+".out").c_str(),"wt",stdout);
}

int lef = 10;
int u[11];

void check(long long n)
{
	while (n)
	{
		if (!u[n%10]) lef--;
		u[n%10]=1;
		n/=10;
	}
	
}

int main()
{
	init();

	int tst;
	scanf("%d\n",&tst);

	for (int cas = 1; cas<=tst;cas++)
	{
		int n;
		scanf("%d",&n);
		if (n==0) 
		{
			printf("Case #%d: INSOMNIA\n",cas);
				continue;
		}
		lef=10;
		memset(u,0,sizeof(u));
		for (int i=1;;i++)
		{
			
			check(n*(long long)i);
			if (lef==0)
			{
				printf("Case #%d: %d\n",cas,n*(long long)i);
				break;				
			}
		}		
	
	}


	return 0;
}
