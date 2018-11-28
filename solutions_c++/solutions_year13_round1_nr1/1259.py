#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<algorithm>
#include<sstream>
#include<iomanip>
#include<cstring>
#include<bitset>
#include<fstream>
#include<cmath>
#include<cassert>
#include <stdio.h>
#include<ctype.h>
using namespace std ;
#define LL long long
int main()
{
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int T;
	cin >> T;
	for(int ti = 1; ti <= T; ++ti)
	{
		LL r, t;
		cin >> r >> t;
		LL cnt = 0;
		while(true)
		{
			LL ext = (r + 1) * (r + 1) - (r * r);
			if(ext > t)
				break;
			t -= ext;
			r += 2;
			++cnt;
		}
		cout << "Case #" << ti << ": " << cnt << endl;
	}

}