#include <bits/stdc++.h>
using namespace std;

#define md 1000000007

int main()
{   
    ios::sync_with_stdio(false);
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);	
    int t, d, i, ans;
    cin >> t;
    for (int tcase = 1 ; tcase <= t ; tcase++)
    {
    	cin >> d;
    	int p[d], max_p = -1;
    	for (i = 0 ; i < d ; i++)
    	{
			cin >> p[i];
			max_p = max(max_p, p[i]);    		
    	}

    	ans = 10000; 

    	for (i = 1 ; i <= max_p ; i++)
    	{
    		int arrange_time = 0;
    		for(int j = 0 ; j < d ; j++)
    		{
    			if(p[j] > i)
    			{
    				arrange_time += (ceil((float)p[j]/(float)i) - 1);
    			}
    		}
    		ans = min(ans,arrange_time + i);
    	}
    	cout << "Case #" << tcase << ": " << ans << endl;
    }
    return 0;
}


