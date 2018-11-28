#include<iostream>
#include<string>
#include<cstdio>
#include<limits>
#include<cmath>
#include<vector>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;

//#define SMALL
#define LARGE

int main()
{

	#ifdef SMALL
		freopen("A-small-attempt0.in", "rt", stdin);
		freopen("A-small-attempt0.out", "wt", stdout);
	#endif

	#ifdef LARGE
		freopen("A-large.in", "rt", stdin);
		freopen("A-large.out", "wt", stdout);
	#endif

	int t;
	cin >> t;
	
	for(int i = 1; i <= t; i++)
	{
		long long multiple, n, j = -1, ans = -1;
		cin >> n;
		
		set<int> digits;
		
		while(digits.size() < 10 && j <= 100)
		{
		    j++;
		    multiple = j * n;
		    while(multiple)
		    {
		        digits.insert(multiple % 10);
		        multiple /= 10;
		    }
		}
		
		ans = j * n;
		
		if(j == 101)
    		cout << "Case #" << i << ": INSOMNIA" << endl;
    	else
    		cout << "Case #" << i << ": " << ans << endl;
	}
	
	return 0;
}
