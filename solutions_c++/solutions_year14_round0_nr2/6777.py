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
#include <climits>
#include <memory.h>
#include<cstring>
using namespace std;
 
int main() {
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	int cnt=1;
	while(t-->0)
	{
		float c,f,x;
		cin >> c >> f >> x;
		float f1=2;
		float ans=0;
		float le=x/f1;
		float ri=(c/f1)+(x/(f+f1));
		float ans1=100000000;
		while(le>ri)
		{
			ans=ans+(c/f1);
			f1=f1+f;
			ri=ans+(c/f1)+(x/(f+f1));
		    le=ans+x/f1;
		  ans1=min(le,ri);
		}
	cout << "Case #" << cnt << ": " <<setprecision(30) << min(le,ans1) << endl ;
	cnt++;
	}
}
