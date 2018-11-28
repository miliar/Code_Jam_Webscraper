#include <iostream>
#include <vector>
#include <math.h>
#include <fstream>
using namespace std;

bool isPalindrome(int num)
{
	int n = num;
	int rev = 0;
	while (num > 0)
	{
    	int dig = num % 10;
    	rev = rev * 10 + dig;
    	num = num / 10;
	}
	if(n==rev)
		return true;
	else
		return false;

}
bool isSquare(int num)
{
	double square = sqrt(num);
	int isquare = square;
	if (square == isquare) 
		return true;
	else
		return false;
}
int main()
{
	fstream f("C-small-attempt0.in", fstream::in);
	int testcases;
	f >> testcases;
	for(int a = 1;a<=testcases;a++)
	{
	int n,s;
	f >> n;
	f >> s;
	int result;
	
	vector<int> victor;
	for(int i = n; i<=s; i++)
		if(isSquare(i))
			victor.push_back(i);
	if(victor.size() == 0)
		result = 0;
	else
		for(int i = 0; i <victor.size(); i++)
			if(!isPalindrome(victor[i]))
			{
				victor.erase(victor.begin()+i);
				i--;
			}
	if(victor.size() == 0)
		result = 0;
	else
		for(int i=0; i<victor.size(); i++)
			if(!isPalindrome(sqrt(victor[i])))
			{
				victor.erase(victor.begin()+i);
				i--;
			}
	result = victor.size();
	cout << "Case #" << a << ": " << result << endl;
	}
}
