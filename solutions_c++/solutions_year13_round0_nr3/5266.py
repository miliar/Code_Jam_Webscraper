#include <iostream>
#include <fstream>
#include <stack>
#include <math.h>

using namespace std;

int expon(int b, int p)
{
	int result = 1;
	for(int i = 0; i < p; i++)
		result *= b;
	return result;
}

bool isPalindrome(int num)
{
	stack<int> s;
	int temp = num;
	while(temp != 0)
	{
		s.push(temp % 10);
		temp /= 10;
	}
	for(int i = 0; !s.empty(); i++)
	{
		temp += s.top() * expon(10, i);
		s.pop();
	}
	if(num == temp)
		return true;
	return false;
}

int main()
{
	int a = 0;
	int b = 0;
	int tests = 0;

	ifstream input;
	ofstream output;

	input.open("input.txt", ios::in);
	output.open("output.txt", ios::out);

	input >> tests;

	for(int i = 0; i < tests; i++)
	{
		int count = 0;
		input >> a >> b;
		for(int j = a; j <= b; j++)
		{
			double fsqrt = sqrt(double(j));
			int isqrt = fsqrt;
			if(isqrt == fsqrt && isPalindrome(j) && isPalindrome(isqrt))
			{
				count++;
			}
		}
		output << "Case #" << i + 1 << ": " << count << endl;
		
	}

	input.close();
	output.close();
	
	return 0;
}