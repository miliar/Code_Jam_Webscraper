#include <iostream>    

using namespace std;
typedef unsigned int uint;
int main ()
{
	uint test_cases = 0;
  	cin >> test_cases;
	uint a,b,k,c,andd;
  	for (uint i=1;i<=test_cases;i++) 
  	{	
		c = 0;
		cin >> a >> b >> k;
		//cout << "A : " << a << endl;
		//cout << "B : " << b << endl;
		//cout << "K : " << k << endl;
		for(int l = 0; l < a; l++)
		{
			for(int m = 0; m < b; m++)
			{
				for(int t = 0; t < k; t++)
				{
					andd = l & m;
					if(andd == t)
					{
						c++;
						//cout << "In if case , L&M = " << andd <<"\n";
					} 
				}
			}
		}

		cout << "Case #" << i << ": " << c << endl;
  	}
return 0;
}
