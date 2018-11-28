#include <iostream>
using namespace std;
int main()
{
	unsigned long long T,i,j,k, count;
	char temp;
	string cake;
	cin>>T;
	for(i=0;i<T;i++)
	{
		count = 0;
		cin>>cake;
		if(cake.length() == 1)
		{
			if (cake[0] == '-')
				count = 1;
		}
		else
		{
			temp = cake[0];
			for(j=0;j<cake.length()-1;j++)
			{
				if(cake[j]!=cake[j+1])
				{
					temp = cake[j+1];
					count++;
					continue;
				}
			}
			if(temp == '-') count++;
		}
		cout << "Case #" << i + 1 <<": " << count << endl;
	}
}