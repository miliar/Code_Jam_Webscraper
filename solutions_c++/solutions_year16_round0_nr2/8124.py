#include<iostream>
#include<string>
using namespace std;


size_t position = 0;
int count = 0;

string reverseString(string str, int pos, char ch)
{
count++;
for(int j=0; j<=pos; j++)
	str[j] = ch;
return str;
}

void calculateNumber(string str)
{
	if(str[0] == '+')
	{
		position = str.find('-');
		if (position!=string::npos)
			str = reverseString(str,position-1,'-');
		else
			return;
	}
	else if(str[0] == '-')
	{
		position = str.find('+');
		if (position!=string::npos)
			str = reverseString(str,position-1,'+');
		else
			str = reverseString(str,str.length()-1,'+');
	}
	calculateNumber(str);
}

int main()
{
int T;
string N;
cin>>T;
for(int i1 = 0;i1<T;i1++)
{
cin>>N;
count = 0;
calculateNumber(N);
cout<<"Case #"<<i1+1<<": "<<count<<"\n";
}
return 0;
}

