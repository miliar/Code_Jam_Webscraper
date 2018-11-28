#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>
#define toDigit(c) (c-'0')
using namespace std;

int main () {
	int count;
  	int result;
  	
	ifstream input;
	ofstream output;
  	
	//input.open("B-sample.in", std::ios_base::in);
  	//output.open("B-sample.out", std::ios_base::out);
	
  	//input.open("B-small.in", std::ios_base::in);
  	//output.open("B-small.out", std::ios_base::out);
  	
	input.open("B-large.in", std::ios_base::in);
  	output.open("B-large.out", std::ios_base::out);
	    	
  	input >> count;

  	for(int j=1; j<=count; j++)
  	{
  		char t;
  		string s;
  		
  		input>>s;

  		result = 0;
  		
  		while(1)
  		{		  
	  		int len = s.size();
	  		if(s[0] == '+')
	  		{
				for(int i=1;i<s.size();i++)
				{
					if(s[i] == '-') 
					{
					 	len = i;	
					 	break;
					} 
				}  
				
				if(len == s.size())
				{
					output<<"Case #"<<j<<": "<<result<<endl;
					break;
				}
				else
				{
					result += 1;
					for(int i=0;i<len;i++) s[i] = '-';
				}
			}
			else
			{
				for(int i=0;i<s.size();i++)
				{
					if(s[i] == '-') len = i;
				}
				result += 1;
				for(int i=0;i<=len/2;i++)
				{
					t = s[i];
					s[i] = (s[len-i] == '+') ? '-' : '+';
					s[len-i] = (t == '+') ? '-' : '+';
				}
			}
		}
	}  	
  
  	input.close();
  	output.close();
  	
  	return 0;
}
