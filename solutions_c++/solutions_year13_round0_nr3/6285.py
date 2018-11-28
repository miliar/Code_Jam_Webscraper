#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;
bool palindrome(int num);
int main()
{
	ifstream infile("C-small-attempt2.in");
	ofstream outfile("out.txt");
	int T;
	int flag;
	int s;
	int a, b;
	infile>>T;
	for(int i = 0; i < T; ++i)
	{
		flag = 0;
		s = 0;
		infile>>a;
		infile>>b;
		for(int k = a; k <= b; ++k)
		{
			if(palindrome(k))
			{
				for(int t = 1; t <= k; ++t)
				{
					if(t * t == k && palindrome(t))
					{
						s++;
						flag = 1;
						break;
					}
				}
			}
		}
		//if(flag)
		//{
			stringstream ss;
			ss<<"Case #"<<i + 1<<": "<<s<<endl;
			outfile<<ss.str().c_str();
		//}
	}
	infile.close();
	outfile.close();
	return 0;
}
bool palindrome(int num)
{
	if(num < 10)
		return true;
	int s = 0;
	int temp = num;
	int denominator = 1;
	while(temp != 0)
	{
		s++;
		temp /= 10;
		denominator *= 10;
	}
	denominator /= 10;
	int g;
	int h;
	
	while(num != 0)
	{
		g = num % 10;
		h = num / denominator;
		if(g != h)
			return false;
		num -= num % 10;
		num /= 10;
		num = num % (denominator / 10);
		if(num < 10)
			return true;
	}
	return true;
}