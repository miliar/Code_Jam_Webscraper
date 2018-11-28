#include <iostream>
#include <string>

using namespace std;

int number_of_flips = 0;
string input;

void flip_cakes(int pos)
{
	if(pos == 0)
	{
		input[pos] = (input[pos] == '-')?'+':'-';
	}
	else
	{
		for (int i = 0; i <= pos/2; ++i)
		{
			char temp = input[pos-i];
			input[pos-i] = (input[i] == '-')?'+':'-';
			input[i] = (temp == '-')?'+':'-';
		}
	}
}

bool all_cakes_happy()
{
	for (int i = 0; i < input.size(); ++i)
	{
		if(input[i] == '-')
			return false;
	}
	return true;
}

int main()
{
	int T;
	cin>>T;

	for (int i = 0; i < T; ++i)
	{
		number_of_flips = 0;
		cin>>input;
		for (int j = input.size()-1; j >= 0; --j)
		{
			if(input[j] == '-')
			{
				int t = j;
				while(input[0] == '+' && t >= 0)
				{
					t--;
					if(input[t] == '+')
					{
						flip_cakes(t);
						number_of_flips++;
					}
				}	
				flip_cakes(j);
				number_of_flips++;
				if(all_cakes_happy())
					break;
			}
		}
		cout<<"Case #"<<(i+1)<<": "<<number_of_flips<<endl;
	}
	return 0;
}