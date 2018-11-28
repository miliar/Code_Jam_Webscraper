#include <iostream>
#include <string>
using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		string pancakes;
		int count=0;
		char flag;
		cin>>pancakes;

		flag=pancakes[0];
		for(int j=1;j<pancakes.length();j++)
		{
			if(pancakes[j]==flag)
				continue;
			if(flag ==  '-')
			{
				flag ='+';
				count++;
			}
			else
			{
				count+=2;
				while(j<pancakes.length() && pancakes[j] == '-')
					j++;
				j--;
				flag='+';
			}
		}
		if(flag=='-')	count++;
		cout<<"Case #"<<i<<": "<<count<<endl;
	}
	return 0;
}
