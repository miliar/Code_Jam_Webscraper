#include<iostream>
#include <fstream> 
#include<list>
using namespace std;


bool testNum(list<int> a)
{
	int temp1, temp2;
	if (a.empty())
		return false;
	else if(a.size() == 1 && a.front() == 0)
		return false;
	while(a.size()>1)
	{
		temp1 = a.front();
		temp2 = a.back();
		if(temp1 != temp2)
			return false;
		a.pop_front();
		a.pop_back();
	}
	return true;
}

int main()
{
	ofstream fout("result.rtf");
	int T;
	cin >> T;
	for(int n=0; n<T; n++)
	{
	long long start;
	long long end;

	cin >> start >> end;

	long long count = 0;
	for(int i = start; i <= end; i++)
	{
		list<int> number1;
		list<int> number2;

		long double input = i;
		long double root;
		int digit;

		long double temp = sqrt((double)input);
		if(temp == (long long)temp)
			root = temp;
		else 
			root = 0;


		while(input >= 1)
		{
			 digit = (long long)input%10;
			number1.push_front(digit);
			input /= 10;
		}
		

		while(root >= 1)
		{
			 digit = (long long)root%10;
			number2.push_front(digit);
			root /= 10;
		}

		bool result1 = testNum(number1);
		bool result2 = testNum(number2);
		if(result1 && result2)
			count++;
	}

	
	cout << "Case #" << n+1 << ": " << count << '\n';
	}

}
