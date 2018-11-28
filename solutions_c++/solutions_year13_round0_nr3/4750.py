#include<iostream>
#include<fstream>
#include<string>
#include<cmath>

using namespace std;


string convertToString (int ss)
{
	string number="";
	while (ss!=0)
	{
		string temp="";
		temp+=(char)(ss%10+48);
		number=temp+number;
		ss/=10;
	}
	return number;
}
bool checkPalindrome (string test)
{
	int limit=(test.length()/2)-1;
	for (int ab=0;ab<=limit;ab++)
	{
		if (test[ab]!=test[test.length()-1-ab])
		{
			return false;
		}
	}

	return true;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testCases;
	scanf("%d", &testCases);
	int counter;
	for (int a=0; a<testCases; a++)
	{
		int lower,upper;
		counter=0;
		scanf("%d %d", &lower, &upper);
		
		for (int a=lower;a<=upper; a++)
		{
			double number=a;
			if (sqrt(number)==floor(sqrt(number)))
			{
				string square=convertToString(number);
				string root=convertToString ((int)(sqrt(number)));
				if (checkPalindrome(square)&&(checkPalindrome(root)))
					counter++;
			}

		}
		printf("Case #%d: %d\n", a+1, counter);
	}


}