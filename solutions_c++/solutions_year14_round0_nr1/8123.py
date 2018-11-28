#include<cstdio>
#include<algorithm>
#include<iostream>
#include<cstdlib>
#include<cassert>
#include<cstring>
#include<vector>
#include<string>
#include<cmath>
#include<ctime>
#include<set>
#include<map>
 
using namespace std;

int T, p, fl;
int a[4][4], u[17], ans;
 
int main()
{
    freopen("in", "r", stdin);
    freopen("out", "w", stdout); 
    cin >> T;
    for (int f = 0; f < T; f++)
    {
    	ans = 0, fl = 0;
    	for (int i = 0; i < 17; i++)
    		u[i] = 0;
    	cin >> p;
    	for (int i = 0; i < 4; i++)
    		for (int j = 0; j < 4; j++)
    			cin >> a[i][j];
    	for (int i = 0; i < 4; i++)
    		u[a[p - 1][i]] = 1;
    	cin >> p;
    	for (int i = 0; i < 4; i++)
    		for (int j = 0; j < 4; j++)
    			cin >> a[i][j];
    	for (int i = 0; i < 4; i++)
    		if (u[a[p - 1][i]] == 1)
    		{
    			if (fl == 0)
    			{
    				fl++;
    				ans = a[p - 1][i];
    	    	}
    	    	else if (fl == 1)
    	    		fl = 2;
    	    }
    	cout << "Case #" << f + 1 << ": ";
    	if (fl == 1)
    		cout << ans;
    	else if (fl == 0)
    		cout << "Volunteer cheated!";
    	else
    		cout << "Bad magician!";
    	
    	cout << endl;
    }

    return 0;
}