#include <iostream>
#include <cmath>
#include <string>
#include <queue>
using namespace std;

int main()
{
freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    for (int i = 0; i  < t; i++)
    {
    	int ans;
    	cin >> ans;
    	int a[4][4];
    	for (int j = 0; j < 4; j++)
    	{
    		for (int k = 0; k < 4; k++)
    		{
    			cin >> a[j][k];
    		}
    	}
    	int ans2;
    	cin >> ans2;
    	int ra = 0;
    	int it;
    	for (int j = 0; j < 4; j++)
    	{
    		for (int k = 0; k < 4; k++)
    		{
    			int x;
    			cin >> x;
    			if (j == ans2 - 1)
    			{
    				for (int l = 0; l < 4; l++)
    				{
    					if (x == a[ans - 1][l])
						{
							ra++;
							it = x;
							break;
						}
    				}
    			}
    		}
    	}
    	if (ra == 1)
		{
			cout << "Case #" << i + 1 << ": " << it << endl;
			continue;
		}
		if (ra == 0)
		{
			cout << "Case #" << i + 1 << ": " << "Volunteer cheated!" << endl;
			continue;
		}
		cout << "Case #" << i + 1 << ": " << "Bad magician!" << endl;
	}
    return 0;
}
