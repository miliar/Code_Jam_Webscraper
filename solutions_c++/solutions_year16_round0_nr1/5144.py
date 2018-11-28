
#include <string>
#include <iostream>
using namespace std;

int main()
{
	int cases, N;
	bool hit[10];
	bool finished = false;
	string number;
	cin >> cases;                    
	for (int c = 1; c <= cases; c++)     
	{
		cin >> N;   

			int i = 0;
			while (i < 10)
			{
				hit[i] = false;
				i++;
			}
			
		if (N)
		{
			int j = 1;
			finished = false;
			while (!finished)
			{
				int i = 0;
				while (i < 10)
				{
					if (!hit[i])
						break;
					if (i == 9)
					{
						cout << "Case #" << c << ": " << (j - 1)*N << endl;
						finished = true;
					}
					i++;
				}

				number = to_string((j*N));
				int k = 0;
				while (k < number.length())
				{
					int index = number[k] - '0';
					hit[index] = true;
					k++;
				}

				j++;
			}
			
		}
		else
		{
			cout << "Case #" << c << ": " << "INSOMNIA" << endl;
		}
	}
	return 0;                       
}

