#include<iostream>
#include<cstring>
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

void flip(char s[1001], int k)
{
    int index = strlen(s) - 1;
    for(int i = 0; i < k; i++)
    {
    	if(s[index - i] == '+')
    		s[index - i] = '-';
    	else
    		s[index - i] = '+';
    }
}

int main()
{

	#ifdef SMALL
		freopen("A-small-attempt0.in", "rt", stdin);
		freopen("A-small.out", "wt", stdout);
	#endif

	#ifdef LARGE
		freopen("A-large.in", "rt", stdin);
		freopen("A-large.out", "wt", stdout);
	#endif

	int t;
	cin >> t;
	
	for(int i = 1; i <= t; i++)
	{
		int ans = 0, k;
		char s[1001];
		cin >> s >> k;
		
		int index = strlen(s) - 1;
		
		while(index > -1)
		{
		    if(s[index] == '+')
		    {
		        s[index] = '\0';
		        index--;
		    }
		    else if(index >= k - 1)
		    {
		        flip(s,k);
		        ans++;
		    }
		    else
		    {
		    	ans = -1;
		    	break;
		    }
		}	
		
		if(ans > -1)
			cout << "Case #" << i << ": " << ans << endl;
		else
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
	}
	
	return 0;
}
