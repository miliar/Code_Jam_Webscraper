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
#include <climits>
#include <string>
#include <cstring>
#include <cassert>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for (int T = 1; T <= t; ++T) {
		int x,r,c,ans;
		cin>>x>>r>>c;
		if((r*c)%x==0) {
			if(r<c)
				swap(r,c);
			if(c==1){
				if(x>=3)
					ans=0;
				else
					ans=1;
			}
			else if(c==2){
				if(x>=4)
					ans=0;
				else
					ans=1;
			}
			else {
				if(x>r||x>=7)
					ans=0;
				else 
					ans=1;
			}
		}else
			ans = 0;
		if(ans)
			printf("Case #%d: GABRIEL\n",T);
		else
			printf("Case #%d: RICHARD\n",T);
	}
	return 0;
}