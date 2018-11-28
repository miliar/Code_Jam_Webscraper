#include <bits/stdc++.h>
using namespace std;

#define md 1000000007

int main()
{   
    ios::sync_with_stdio(false);
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);	

    int t;
	cin >> t;

    for (int tcase = 1; tcase <= t; tcase++)
    {
    	int smax, ans = 0, shy_count = 0;
    	string s;
    	cin >> smax;
    	cin >> s;
    	for(int i = 0 ; i <= smax ; i++)
    	{
    		if(shy_count >= i)
    			shy_count += (s[i] - '0');
    		else
    		{
    			ans += (i-shy_count);
    			shy_count += (s[i] - '0') + (i-shy_count);
    		}
    		// cout << shy_count << endl;
    	}
    	cout << "Case #" << tcase << ": " << ans << endl;
    }
    return 0;
}


