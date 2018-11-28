#include <iostream>
#include <cstring>

using namespace std;

int present[10];

bool all_nums_present()
{
	for (int i = 0; i < 10; ++i)
	{
		if(present[i] == 0)
			return false;
	}
	return true;
}

void update_present(int num)
{
	int temp;
	while(num > 0)
	{
		temp = num%10;
		present[temp] = 1;
		num /= 10;
	}
}

int main()
{
	int T;
	cin>>T;

	for (int i = 0; i < T; ++i)
	{
		int N;
		cin>>N;
		memset(present, 0, 10*sizeof(int));
		if(N == 0)
			cout<<"Case #"<<(i+1)<<": "<<"INSOMNIA"<<endl;
		else
		{
			for(int j = 1; 1; j++)
			{
				update_present(j*N);
				if( all_nums_present() )
				{
					cout<<"Case #"<<(i+1)<<": "<<(j*N)<<endl;
					break;
				}
			}
		}
	}

	return 0;
}