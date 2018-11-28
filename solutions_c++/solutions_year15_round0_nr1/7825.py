#include <vector>
#include <list>
#include <map>
#include <set>
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

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq=1;qq<=tt;qq++) {
    printf("Case #%d: ", qq);
     int smax,x=0,ans=0;
     cin>>smax;
     char ip[smax+1];
     cin>>ip;
    	x=ip[0]-'0';
		for(int j=1;j<=smax;j++)
		{
			if(j<=x)
			  x=x+ip[j]-'0';
			else
			{
			  ans=ans+j-x;
			  x=x+ip[j]-'0'+j-x;
		}
		}
		printf("%d\n", ans);
  
  }
  return 0;
}

