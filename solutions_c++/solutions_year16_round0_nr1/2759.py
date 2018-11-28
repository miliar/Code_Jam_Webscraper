#include <iostream>
#include <cmath>

using namespace std;

typedef long long ll;

int main()
{
	ll casses = 0;
	cin >> casses;
	bool data[10];
	
	for(int caseNum = 0; caseNum < casses; caseNum++)
	{
		int num;
		cin >> num;
		for(int i = 0; i < 10; i++)
			data[i] = false;
		if(num == 0)
		{
			cout << "Case #" << caseNum + 1 << ": INSOMNIA" << endl;
		}
		else
		{
			int temp = num;
			while(true)
			{
				int temp2 = temp;
				while(temp2 > 0)
				{
					data[temp2 % 10] = true;
					temp2 /= 10;
				}
				
				bool good = true;
				for(int i = 0; i < 10; i++)
				{
					if(!data[i])
					{
						good = false;
						break;
					}
				}
				if(good)
				{
					cout << "Case #" << caseNum + 1 << ": " << temp << endl;
					break; 
				}
				
				temp += num;
			}
		}
	}
	return 0;
}
