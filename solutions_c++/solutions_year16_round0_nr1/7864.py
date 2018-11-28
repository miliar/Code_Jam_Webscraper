#include <iostream>
#include <string>
using namespace std;

int main() 
{
	int T, n; 
	cin >> T; 
	
	for(int i = 1; i <= T; i++)
	{
		int result;
		bool digits[10] { false };
		cin >> n;
		
		if(n == 0) 
		{ 
			cout << "Case #" << i << ": INSOMNIA" << endl;
		} 
		else 
		{ 
			int count = 0; 
			
			for(int i = 1; count < 10; i++)
			{
				int tmp = i * n; 
				while(tmp)
				{
					int r = tmp % 10; 
					
					if(!digits[r])
					{
						digits[r] = true; 
						count++;
						if(count == 10)
						{
							result = i * n;
							break;
						}
					}
					
					tmp /= 10;
				}
			}
			
			cout << "Case #" << i << ": " << result << endl;
		}
	}
	
	return 0;
}