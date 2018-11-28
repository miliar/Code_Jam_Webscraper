#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;


int main()
{
	freopen("A-small-practice.in","rt",stdin);
	freopen("aout.out","wt",stdout);
	int t,k,ans,i;
	char s[122],c;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		ans=0;
		scanf("%s",s);
		printf("Case #%d: ",k);
		c=s[0];
		for(i=0;s[i]!='\0';i++)
		{
			if(s[i]!=c)
			{
				c=s[i];
				ans++;
			}
		}
		if(c=='-')
		ans++;
		printf("%d\n",ans);
	}
	return 0;
}
