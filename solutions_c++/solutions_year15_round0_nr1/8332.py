#include <iostream>

using namespace std;

int main()
{
	int Smax=0;
	char list[1010];
	int no_of_case;
	cin>>no_of_case;
	for (int i=0;i<no_of_case;i++)
	{
		int add=0;
		int sum=0;
		cin>>Smax>>list;
		for (int j=0;j<=Smax;j++)
		{
			sum+=list[j]-'0';
			if (sum<j+1)
			{
				add++;
				sum++;
			}				
		}
		cout<<"Case #"<<i+1<<": "<<add<<endl;
	}
	return 0;
}