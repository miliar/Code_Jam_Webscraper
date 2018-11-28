#include <iostream>
#include <sstream>

using namespace std;

int main()
{
	int t, encontrados;
	long long num,n, original;
	scanf("%d",&t);
	bool digits[10];

	for(int tt = 1; tt <= t; tt++)
	{
		encontrados = 0;
		memset(digits, false, sizeof(digits));
		scanf("%lld",&num);
		original = num;
		
		if(num == 0)
			printf("Case #%d: INSOMNIA\n",tt);
		else
		{
			bool compute = true;
			while(compute)
			{ 
				string str;
				stringstream mystream;
				mystream << num;
				str = mystream.str();
				
				for(int i = 0; i < str.size(); i++)
				{	
					if(!digits[str[i] - '0'])
					{
						digits[str[i] - '0'] = true;
						if(++encontrados == 10)
						{
							compute = false;
							break;
						}
					}
				}
				

				if(compute)
				{
					num += original;
				}
			}
			printf("Case #%d: %lld\n",tt,num);
		}
	}
	return 0;
}