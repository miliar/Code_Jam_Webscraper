/*

*/

#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <unistd.h>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <sstream>

using namespace std;

int i,j,k,Test_cases,t,line_no,possible_no[4],num,ans,counter=0;

void solve()
{
	scanf("%d",&Test_cases);
	for(t=1;t<=Test_cases;++t)
	{
		counter=num=ans=0;
		scanf("%d",&line_no);
		line_no--;
		for(i=0;i<4;++i)
			for(j=0;j<4;++j)
			{
				scanf("%d",&num);
				if(i==line_no)
					possible_no[j]=num;
			}
		scanf("%d",&line_no);
		line_no--;
		for(i=0;i<4;++i)
			for(j=0;j<4;++j)
			{
				scanf("%d",&num);
				if(i==line_no)
					for(k=0;k<4;++k)
						if(possible_no[k]==num)
						{
							counter++;
							ans=num;
						}
			}
		if(counter==1)
			printf("Case #%d: %d\n",t,ans);
		else if(!counter)
			printf("Case #%d: Volunteer cheated!\n",t);
		else
			printf("Case #%d: Bad magician!\n",t);
	}
}

int main(int argc,char *argv[])
{
	solve();
    return 0;
}


