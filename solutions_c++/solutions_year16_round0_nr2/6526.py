#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

int test,  result;

int check(string & str);
void flipping(string & str);
int main()
{
cin >> test;
int i, j;
string str;
for ( i =1; i<= test; i++)
{
	cin >> str ;
	
	result = 0;

	while(check(str))
	{
		flipping(str);
		result++;
	}
	cout << "Case #" << i << ": " << result << endl;

}
return 0;
}

int check(string & str)
{
	int index = str.length();
	int length = index;
	while ( str[index-1] == '+')
	{
		index--;
	}
	
	// remove from index to end
	str.erase(index, length - index );
	length = str.length();
	return length;
}

void flipping(string & str)
{

	int index = 0;
	while (str[index] == '+')
	{
		str[index++] = '-';
	}
	if (index == 0)
	{
		reverse(str.begin(), str.end());
		int i;
		int len = str.length();
		for (i = 0; i < len; i++)
		{
			if (str[i] == '-')
			{
				str[i] = '+';
			}
			else
			{
				str[i] = '-';
			}
		}
	}
}





























