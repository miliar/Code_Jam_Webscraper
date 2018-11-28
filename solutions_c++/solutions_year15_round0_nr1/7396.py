#include <iostream>
using namespace std;
int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		int max, min=0, sum = 0;;
		cin >> max;
		string input;
		cin >> input;
		int l = input.length();
		for (int j = 0; j < l; ++j)
		{
			int num = input[j] - '0';
			sum += num;
			if(j!=l-1 && sum<j+1){
				int diff = j+1 - sum;
				sum += diff;				
				min += diff;
			}
		}
		cout << "Case #"<<i+1<<": "<< min << "\n";
	}
}