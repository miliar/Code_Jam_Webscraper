#include<iostream>

using namespace std;

int main()
{
	int c;
	int i = 1;
	int a = 10;
	
	cin >> c;
	while(c--)
	{
		int num, tmp, sum;
		
		int k = 1 ;
		int result[10] = {};
		cin >> num;
		
		if(num > 0)
		{
			while(1)
			{
				int count = 0;
				sum = num*k;
				tmp = sum;
				while(tmp != 0)
				{
						int tmp2;
						tmp2 = tmp%10;
						result[tmp2]++;
						tmp /= 10;
				}				
				
				for(int j = 0 ; j < 10 ; j++)
					if(result[j] > 0)
						count++;
				if(count == 10)
					break;
				k++;
			}
			cout << "Case #" << i << ": " << sum << endl;
		}
		else
		{
			cout << "Case #" << i << ": INSOMNIA" << endl;
		}
		i++;
	}
	
	
	
	return 0;
}
