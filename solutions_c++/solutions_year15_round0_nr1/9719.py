#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<stack>
#include<deque>
#include<queue>
#include<vector>
#include<list>
#include<set>
#include<map>
#include<cmath>
#include<climits>

using namespace std;

int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int t, counter;

	scanf("%d", &t);

	for(counter=1; counter<=t; counter++)
	{
	    int n, i, curr=0, req=0;
	    string s;

	    scanf("%d", &n);
	    cin>>s;

	    for(i=0; i<=n; i++)
        {
            if(curr >= i)
                curr += s[i] - '0';
            else if(s[i] != '0')
            {
                req += i - curr;
                curr += req;
                curr += s[i] - '0';
            }
        }

		printf("Case #%d: %d\n", counter, req);
	}

	return 0;
}
