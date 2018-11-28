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

typedef unsigned long ul;

using namespace std;

int main() {
ul p[1000],tt,d,cof,div,maxv,res;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin >> tt;
	
	for (ul i=0;++i<=tt;)
	{
		cin >> d;
		for (ul j=0;j<d;j++) cin >> p[j];
		res = maxv = *max_element(p,p+d);

        for (ul j=1;j<=maxv;j++)
		{
            div = j;
            for (ul k=0;k<d;k++)
			{
				cof = p[k] / j;
                if (cof >= 1)
				{
					div += cof;
                    if (cof*j == p[k]) div--;
                }
            }
            res = min(res,div) ;
		}
		
		cout << "Case #" << i << ": " << res << endl;
	}
	
	return 0;
}
