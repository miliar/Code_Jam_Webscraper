#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <sstream>
using namespace std;
bool palindrome(string temp)
{
	bool check;
	string reverse="";

	for(int i=0;i<temp.length();i++)
	reverse = temp[i] + reverse;

	if(reverse==temp)
	check = true;
	else
	check = false;

	return check;	
}
int squareFair(int A,int B)
{
	int count=0;
	string input;
	string squareRoot;

	stringstream convert("");
	for(int i=A;i<=B;i++)
	{
		

		string input;			//string which will contain the result
		string squareRoot;		//String for storing squareRoot of input
		stringstream convert; 		// stringstream used for the conversion
		convert << i;			//add the value of Number to the characters in the stream
		input = convert.str();

		convert.str("");		//Empty the stream
		convert<<sqrt(i);

		squareRoot = convert.str();
		if(palindrome(input) && palindrome(squareRoot))
		count++;
	}

	return count;
}

int main(int argc,char *argv[])
{
	ifstream in(argv[1]);
	ofstream out("fair.out");

	int testCases=0;
	int caseCount=0;
	int A,B;
	if(in)
	{
		int sfCount=0;
		in>>testCases;
		while(testCases > 0)
		{
			caseCount++;
			in>>A;
			in>>B;
			sfCount = squareFair(A,B);
			out<<"Case #"<<caseCount<<": "<<sfCount<<endl;
			testCases--;
		}
	}
}	
