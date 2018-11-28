#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

#define OUT output

using namespace std;

int flipcount(string &inpstr, int st, bool isforward);

int main()
{
	ifstream input("file.in");
	ofstream output("file.out");

	int tc;

	input>>tc;

	for(int c=1; c<=tc; ++c)
	{
		OUT << "Case #" << c << ": ";
		string str;

		input >> str;
		
		OUT << flipcount(str, 0, true);

		if(c<tc) OUT << endl;
	}
	
	return 0;
}
int flipcount(string &inpstr, int st, bool isforward)
{
	int end;
	int ilen = inpstr.length();

	for(end=ilen; end>0 && inpstr[end-1]=='+'; --end)
		;

	string str = string(inpstr,st, end);
	string inppart =  str;

	int len = str.length();

	int i=0, result = 0;
	
	int tmp=i;
	for(; i < len && (str[i] == '+'); ++i)
		;
	
	if(i == len) 
		return result;
	
	if(!isforward)
	{
		for(int i = len-1, j=0; i >= 0; --i, ++j)
			str[j] = (inppart[i]=='+')? '-' : '+';
	}

	i=0;
	result = 0;
	
	tmp=i;
	for(; i < len && (str[i] == '+'); ++i)
		;
	
	if(i == len) return result;
	
	if(i!=tmp) ++result;

	tmp=i;
	for(; i < len && (str[i] == '-'); ++i)
		;
	
	if(i!=tmp) ++result;

	if(i == len) return result;

	return result + flipcount(str, i, false);
}