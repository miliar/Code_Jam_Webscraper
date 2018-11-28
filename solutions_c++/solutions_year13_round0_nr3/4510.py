#include <string>
#include <sstream>
#include <iostream>
#include <math.h>
#include <fstream>
#include <vector>
using namespace std;
	

bool isPalindrome(int num)
{
	int res = num / 10;
	if(res == 0)
		return true;
	 ostringstream ss;
     ss << num;
	string s = ss.str();
	for(int i=0; i<s.length()/2; i++)
    {
    	if(s[i] != s[s.length() - i-1])
    		{
    			return false;
	    	}
	}
    return true;
}
int findNumbers(int lowBound, int upBound)
{
	int count = 0;
	if(lowBound == upBound)
		return isPalindrome(lowBound);
	for(int i = lowBound; i <= upBound; i++)
	{
		float square = sqrt(i);
		if(fmodf(square,1.0) != 0.0)
			continue;

		if(isPalindrome(i) && isPalindrome(square))
			{
				count++;
			}
	}
	return count;
}
int main()
{
	string line;
	ifstream myfile("in.txt");
	ofstream outFile;
  	outFile.open ("out.txt");
// get # testcases
  	getline (myfile,line);
	int numCases= atoi(line.c_str());
	cout<<numCases<<endl;
	for(size_t i = 1; i<= numCases;i++)//numCases; i++)
	{
		getline (myfile,line);
		stringstream stream(line);
		int lowBound(-1),upBound(-1);
	   		stream >> lowBound;
	   		if(!stream)
	      		break;
	      	else
	      		stream >> upBound;
	
		int result = 0;
		if(upBound == -1)
			result = isPalindrome(lowBound);
		else
			result = findNumbers(lowBound,upBound);

		outFile<<"Case #"<<i<<": "<<result<<endl;
	}
	outFile.close();
	myfile.close();

	return 0;
}