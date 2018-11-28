#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int main()
{
    int T;
    cin >> T;
    string case_str = "Case #";
    string colon = ": ";
    int count = 1;
    int smax;
    string audience;
    while(T--)
    {
    	cin >> smax >> audience;
    	int stood_num = audience.at(0) - '0';
    	int friends_num = 0;
    	for(int need = 1; need <= smax; need++)
    	{
    		if(need > stood_num)
    		{
    			friends_num += need - stood_num;
    			stood_num += need - stood_num + audience.at(need) - '0';
    		}
    		else
    		{
    			stood_num += audience.at(need) - '0';
    		}
    	}
    	cout << case_str << count++ << colon << friends_num << endl;
    }
    return 0;
}
