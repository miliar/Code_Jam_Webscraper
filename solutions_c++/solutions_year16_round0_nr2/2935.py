#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <complex>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <climits>
#include <ctime>

#include<unordered_map>
#include<unordered_set>
using namespace std;


/*
patten :
+- << must do 2 , group this pattern, e.g. +-------- also = 2
-+ << must do 1 , e.g. --------+ , can ignore +

*/
int main(int a, char **ag)
{	
	int Case, cases = 0;
	scanf("%d" , &Case);
	while (Case--)	
	{
		string in;
		cin >> in;

		int ans = 0;
		char prev = in.back();
		for (int i = in.size()-1; i--;)
		{
			if (prev != in[i])
			{
				if (prev == '-')
					ans += 2;
			}
			prev = in[i];
		}
		if ( prev == '-')
			ans++;
		
		printf("Case #%d: " , ++cases );

		printf("%d\n" , ans);

	}

	return 0;
}

