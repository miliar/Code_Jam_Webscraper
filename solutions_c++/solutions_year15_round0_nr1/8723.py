#include <cmath>
#include <climits>
#include <queue>
#include <vector>
#include <map>
#include <cstdlib>
#include <fstream>
#include <iomanip>   
#include <iostream>  
#include <sstream>  
#include <stack>
#include <algorithm>
#include <cstring>
#include <cassert>

using namespace std;

int main()
{
	int t, n, k, p = 1, count, ans;
	string inp;
	cin >> t;
	while(t--)
	{
		ans = 0;
		count = 0;
		cin >> n;
		cin >> inp;
		for(int i=0;i<inp.size();i++)
		{
			count += (inp[i] - '0');
			//cout << count << "..." << endl;
			if(count < i+1)
			{
				ans += (i+1-count);
				count += (i+1-count);
			}	
		}
		cout << "Case #"<<p<<": "<<ans<<endl;
		++p;
	}	
	return 0;
}
