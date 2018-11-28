#include <iostream>

using namespace std;

char flipChecker(char in)	{
	if(in=='+')		return '-';
	else		return '+';
}
int main()	{
	long long t,j,index,flips;
	bool checkingBegins=false;
	string str;
	char checker;
	cin>>t;
	j = 0;
	while(t--)	{
		j++;
		cin>>str;
		index = str.length() - 1;
		checkingBegins = false;
		flips = 0;
		while(index>=0 && !checkingBegins)	{
			if(str[index]=='+')	index--;
			else	{
				checkingBegins = true;
				index--;
				flips++;
			}
		}
		checker = '+';
		while(index>=0 && checkingBegins)	{
			if(str[index]!=checker)	index--;
			else	{
				checker = flipChecker(checker);
				index--;
				flips++;
			}
		}
		cout<<"Case #"<<j<<": "<<flips<<endl;
	}
	return 0;
}