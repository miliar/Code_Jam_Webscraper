#include <iostream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <vector>
#include <fstream>
using namespace std;

bool checkString(string mystring);
void flip(string &mystring, int end);
int flipNumber(string mystring);


int main()
{
	ifstream c("B-large.in");
	ofstream d("output.txt");
	
	if (c.fail())
		cout<<"Input failed"<<endl;
	
	int T;
	c>>T;
	
	string mystring[T];
	
	
	for (int i=0;i<T;i++)
		c>>mystring[i];
	
	c.close();
	
	for (int i=0;i<T;i++)
	{
		d<<"Case #"<<i+1<<": ";
		
		int number=flipNumber(mystring[i]);
	
		d<<number<<endl;
	}
}

bool checkString(string mystring)
{
	int size = mystring.size();
	
	for (int i=0;i<size;i++)
	{
		if ( mystring[i] == '-')
			return false;	
	}	
	
	return true;
}

void flip(string &mystring,int end)
{
/*	string s = mystring.substr(0,end);
	int ssize = s.size();
	cout<<s<<endl;
	cout<<ssize<<endl;
	
	string temp = s;
	
	for (int i=ssize-1;i>=0;i--)
	{
		char kk = s[i];
		
		temp[ssize-i-1] = s[i];
	}
	cout<<temp<<endl;
*/	
	for (int i=0;i<end;i++)
	{
		if (mystring[i] == '+')
			mystring[i] = '-';
		else
			mystring[i] = '+';
	}
/*	
	cout<<temp<<endl;
	for (int i=0;i<ssize;i++)
	{
		mystring[i] = temp[i];
	}
*/	
	
}

int flipNumber(string mystring)
{
	int flips = 0;
	int size = mystring.size();
	
	while (checkString(mystring) != true)
	{
		//cout<<"debug1"<<endl;
		
		int start;
		int end;
		int checkt = 0;
		
		for (int i=0;i<size;i++)
		{
			if (mystring[i] == '-' && checkt == 0)
			{
				start = i;
				checkt = 1;
				end = i;
				continue;
			} 
			if (mystring[i] == '-' &&checkt == 1)
				end++;
			if (mystring[i] == '+' &&checkt == 1)
				break;
				
		}		
		
		if (start != end && start == 0)
		{
			//cout<<"debug2"<<endl;
			flip(mystring,end+1);
			flips = flips+1;
		}
		
		if (start != end && start != 0)
		{
			//cout<<"debug2"<<endl;
			flip(mystring,start);
			flip(mystring,end+1);
			flips = flips+2;
		}
		if (start == end)
		{
			//cout<<"debug3"<<endl;
			flip(mystring,end+1);
			flips = flips+1;
			//cout<<"flips: "<<flips<<endl;
		}
		
	}
	//cout<<"ffflips"<<endl;
	return flips;
}






