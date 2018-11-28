#include <iostream>

using namespace std;
int main()
{
	int T,t;
	int i, smax;
	char input[1005];
	
	cin >> T;
	for(t=1; t<=T; t++)
	{	cin >> smax >> input;
		
		int ans = 0;
		if(smax == 0)
		{	ans = 0;	}
		else
		{
			int a;
			int no_gotup=0, no_req = 0; 
			for(i=0; i<=smax; i++)
			{	a = (int)input[i] - 48;
				
				if(i==0)
				{	no_gotup = a;	}
				else
				{	if(no_gotup >= i)
					{	no_gotup += a;	}
					else 
					{	if(a!=0)
						{	no_req += i - no_gotup;
							no_gotup += a + no_req;
						}
					}
				}
			}
			ans = no_req;
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}