#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <set>
using namespace std;

void countFlip(string input, int * resultPtr)
{
	int newLoc = input.length()-1;
	while( (newLoc >= 0) && (input[newLoc] == '+'))
	{
		newLoc--;
	}
	if(newLoc < 0 )
	{
		return;
	}

	while((newLoc >= 0) && (input[newLoc] == '-'))
	{
		newLoc--;
	}
	(*resultPtr)++;
	string s = input.substr(0,newLoc+1);
	string s1 = s;
	for(int i=0; i< s.length(); i++)
	{
		if(s[i] == '-')
			s1[i] = '+';
		else
			s1[i] = '-';
	}
	countFlip(s1,resultPtr);
}

int main(){
	int t =0;
	freopen( "B-large.in", "r", stdin );
	freopen( "B-large.out", "w", stdout );	
	cin >> t;
	

	for(int i =0; i< t; i++)
	{
		string input;
		int result = 0;
		cin >> input;

		countFlip(input, &result);

		
		cout << "Case #" << i+1 <<": " << result << "\n";		
	}

}
