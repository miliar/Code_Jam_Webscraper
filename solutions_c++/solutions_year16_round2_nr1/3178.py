#include <vector>
#include <valarray>
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
	int t;
	int i,j,a[30],ans[11];
	char s[2009];
	scanf("%d",&t);
	for(j=1;j<=t;j++)
	{
		scanf("%s",s);
		printf("Case #%d: ",j);
		for(i=0;i<29;i++)
		a[i]=0;
		for(i=0;i<11;i++)
		ans[i]=0;
		for(i=0;s[i]!='\0';i++)
		{
			a[s[i]-'A']++;
		}
		while(a['Z'-'A']!=0)
		{
			ans[0]++;
			a['Z'-'A']--;
			a['E'-'A']--;
			a['R'-'A']--;
			a['O'-'A']--;
		}
		
		while(a['W'-'A']!=0)
		{
			ans[2]++;
			a['T'-'A']--;
			a['W'-'A']--;
			a['O'-'A']--;
		}
		
		while(a['U'-'A']!=0)
		{
			ans[4]++;
			a['F'-'A']--;
			a['O'-'A']--;
			a['U'-'A']--;
			a['R'-'A']--;
		}
		
		while(a['X'-'A']!=0)
		{
			ans[6]++;
			a['S'-'A']--;
			a['I'-'A']--;
			a['X'-'A']--;
		}
		
		while(a['G'-'A']!=0)
		{
			ans[8]++;
			a['E'-'A']--;
			a['I'-'A']--;
			a['G'-'A']--;
			a['H'-'A']--;
			a['T'-'A']--;
		}
		
		while(a['O'-'A']!=0)
		{
			ans[1]++;
			a['O'-'A']--;
			a['N'-'A']--;
			a['E'-'A']--;
		}
		
		while(a['T'-'A']!=0)
		{
			ans[3]++;
			a['T'-'A']--;
			a['H'-'A']--;
			a['R'-'A']--;
			a['E'-'A']-=2;
		}
		
		while(a['F'-'A']!=0)
		{
			ans[5]++;
			a['F'-'A']--;
			a['I'-'A']--;
			a['V'-'A']--;
			a['E'-'A']--;
		}
		
		while(a['V'-'A']!=0)
		{
			ans[7]++;
			a['S'-'A']--;
			a['E'-'A']-=2;
			a['V'-'A']--;
			a['N'-'A']--;
		}
		
		while(a['I'-'A']!=0)
		{
			ans[9]++;
			a['N'-'A']-=2;
			a['I'-'A']--;
			a['E'-'A']--;
		}
		for(i=0;i<10;i++)
		{
			while(ans[i]!=0)
			{
				printf("%d",i);
				ans[i]--;
			}
		}
		printf("\n");
	}
	return 0;
}
