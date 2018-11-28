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


int main(int a, char **ag)
{	
	int Case, cases = 0;
	scanf("%d" , &Case);
	while (Case--)	
	{
		
		printf("Case #%d: " , ++cases );

		int n;
		cin >> n;

		set<char> a;
		int i = 1;
		while (n && a.size() != 10)
		{

			stringstream ss;
			ss << n *i++;
			
			for (int j = 0; j < ss.str().size(); ++j)
			{
				a.insert( ss.str()[j]);
			}

		}
		
		if (n)
		 cout << n*--i << endl;
		else
			puts("INSOMNIA");

	}

	return 0;
}

