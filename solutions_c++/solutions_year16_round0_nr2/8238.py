#include<iostream>
#include<string>
using namespace std;

int main()
{
	int T,index,count=0;
	cin>> T;
	string stack;
	for(int i=1;i<=T;i++)
	{
		cin >> stack;
		count = 0;
		index = stack.find_last_of('-');
		while(index!=string::npos)
		{
			count++;			
			for(int j=0;j<=index;j++)
			{
				if(stack[j] == '+')
					stack[j] = '-';
				else if(stack[j] == '-')
					stack[j] = '+';
			}
			index = stack.find_last_of('-');
		}
		cout << "Case #" << i << ": " << count << endl;
	}
}