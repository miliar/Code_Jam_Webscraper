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
const int maxs = 1003;

int main()
{
  freopen("A-small-attempt1.in","r",stdin);
  freopen("A-small-attempt1.out","w",stdout);
  int t;
  int num,row;
  int cnt[17];
  scanf("%d",&t);
  for (int cases=1; cases<=t; ++cases)
  {
	  fill(cnt,cnt+17,0);
	  cin >> row;
	  for (int i=1; i<= 4; ++i)
	  {
	  	for (int j=1; j<=4; ++j)
		{
			cin >> num;
			if (i == row)
				cnt[num] ++;
		}
	  }
	  cin >> row;
	  for (int i=1; i<= 4; ++i)
	  {
	  	for (int j=1; j<=4; ++j)
		{
			cin >> num;
			if (i == row)
				cnt[num] ++;
		}
	  }
	  int res = 0,counts=0;
	  for (int i=1; i<=16; ++i)
	  {
	  	if (cnt[i] == 2)
		{ 
			counts ++ ;res = i;
		}
	  }
	  printf("Case #%d: ",cases);
	  if (counts>=2) 
		  cout << "Bad magician!" << endl;
	  else if(counts == 0)
		  cout << "Volunteer cheated!" << endl;
	  else cout << res << endl;
  }
  return 0;
}
