#include<iostream>
#include<string>
using namespace std;

int arr[101];
int len;

void print()
{
	for(int i = 0; i< len; i++)
	{
		cout << arr[i];
	}
}
void flip(int curr_index)
{
	for(int i = curr_index; i >= 0 ; i--)
	{
		if(arr[i] == 1)
		{
			arr[i] = 0;
		}
		else
			arr[i] = 1;
	}
}
int main()
{
	int tc;
	cin >> tc;
	string line;
	for(int t = 1; t<=tc; t++)
	{
		for(int i =0; i< 100; i++)
		{
			arr[i] = -1;
		}
		cin >> line;
		int count =0;
		len = line.length();
		for(int i = 0; i< len; i++)
		{
			if(line[i] == '+')
				arr[i] = 1;
			else
				arr[i] = 0;
		}
		//print();
		for (int index = len-1; index >= 0; --index)
    	{
    		if(arr[index] == 0)
    		{
    			flip(index);
    			count++;
    		}
    	}
    	cout << "Case #"<< t <<": "<<count<<endl;

	}
	return 0;
}