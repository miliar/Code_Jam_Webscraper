#include <iostream>
using namespace std;
int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int max;
		string str;
		int min=0;
		int temp = 0;
		cin >> max;
		cin >> str;
		int len = str.length();
		for (int j = 0; j < len; j++)
		{
			int num;
			num = str[j] - '0';
			temp = temp +  num;
			if(j!=len-1)
			{
				if (temp < j + 1)
				{
					int diff;
					diff = j+1 - temp;
					temp = temp + diff;				
					min = min +  diff;
				}
				
			}
		}
		cout << "Case #"<<i+1<<": "<< min << "\n";
	}
}