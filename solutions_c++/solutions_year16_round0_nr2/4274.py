#include<iostream>
#include<string>
#include<cstdio>
#include<limits>
#include<cmath>
#include<vector>
#include<set>
#include<stack>
#include<queue>
#include<cstring>
#include<algorithm>
using namespace std;

//#define SMALL
#define LARGE

void flip(char s[101])
{
    if(s[0] == '-')
    {
        for(int i = 0; s[i] != '\0'; i++)
        {
            if(s[i] == '-')
                s[i] = '+';
            else
                s[i] = '-';
        }
    }
    else
    {
        for(int i = 0; s[i] != '\0' && s[i] != '-'; i++)
            s[i] = '-';
    }
}

int main()
{

	#ifdef SMALL
		freopen("B-small-attempt0.in", "rt", stdin);
		freopen("B-small-attempt0.out", "wt", stdout);
	#endif

	#ifdef LARGE
		freopen("B-large.in", "rt", stdin);
		freopen("B-large.out", "wt", stdout);
	#endif

	int t;
	cin >> t;
	
	for(int i = 1; i <= t; i++)
	{
		int ans = 0;
		char s[101];
		cin >> s;
		
		int index = strlen(s) - 1;
		
		while(index > -1)
		{
		    if(s[index] == '+')
		    {
		        s[index] = '\0';
		        index--;
		    }
		    else
		    {
		        flip(s);
		        ans++;
		    }
		}
		
		cout << "Case #" << i << ": " << ans << endl;		
	}
	
	return 0;
}
