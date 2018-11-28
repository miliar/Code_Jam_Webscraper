#include <iostream>

using namespace std;


int main()
{
	int cs, t, i, n, num[10], ok, x;
	cin >> t;
	cs = t;
	while(t--)
	{
		ok= 0;
		x = 1;
		
		for(i=0 ; i<10 ; i++)
		{
			num[i]=0;
		}
		
		cin >> n;
		
		if(n==0)
		{
			cout<<"Case #"<<cs-t<<": INSOMNIA" << endl;
		}
		else
		{
			int tmp = n;
			
			while(n<=1000000)
			{
				while(n>0)
				{
					int in = n%10;
 					num[in] = 1;
					
					n/=10;
					ok = num[0] && num[1] && num[2] && num[3] && num[4] && num[5] && num[6] && num[7] && num[8] && num[9];
					
					if(ok)
					{
						break;
					}
				}
				if(ok)
				{
					break;
				}
				x++;
				n = tmp*x;
				
			}
			
			if(ok)
				cout<<"Case #"<<cs-t<<": " << tmp*x << endl;
			else
				cout<<"Case #"<<cs-t<<": INSOMNIA" << endl;
		}
	}
	return 0;
}
