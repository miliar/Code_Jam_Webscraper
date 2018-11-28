#include <iostream>
#include <string>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int T;
    cin >> T;
    string case_str = "Case #";
    string colon = ": ";
    int count = 1;
    const string success_str = "GABRIEL";
    const string fail_str = "RICHARD";
    while(T--)
    {
    	int x, r, c;	
    	cin >> x >> r >> c;
    	bool flag;
    	if(x == 1)
    	{
    		flag = true;
    	}
    	else if(r*c < x)
    	{
    		flag = false;
    	}
    	else if(r*c % x != 0)
    	{
    		flag = false;
    	}
    	else if(x == 2)			// x == 2 && r*c >= x && r*c%x == 0
    	{
    		flag = true;
    	}
    	// x >= 3 from now on
    	else if(r < sqrt(x) || c < sqrt(x))
    	{
    		flag = false;
    	}
    	else			// x | r*c, r*c>x, x >= 3
    	{
    		if(x==4 && (r == 2 || c == 2))
    		{
    			flag = false;
    		}
    		else
    		{
    			flag = true;
    		}
    	}


    	if(flag)
    	{
    		cout << case_str << count++ << colon << success_str << endl;
    	}
    	else
    	{
    		cout << case_str << count++ << colon << fail_str << endl;
    	}
    }
    return 0;
}