#include<iostream>
#include<fstream>
#include<string>
#include<math.h>
using namespace std;

ifstream in("input.txt",ios::in);
ofstream out("output.txt",ios::out);
int numOfFairs;

bool checkP(string str)
{
	int len=str.length();
	int hlen=len/2;
	for(int i=0 ; i<hlen ; i++)
	{
		if(str[i]!=str[len-i-1])
			return false;
	}
	return true;
}

bool checkForPalindrom(float square,int num)
{
	string sq=to_string(num);
	string n=to_string((int)square);
	return checkP(n) && checkP(sq);
}

void solve()
{
	int start,end;
	in>>start>>end;
	for(int i=start ; i<=end ; i++)
	{
		float sq=sqrtf(i);
		int temp=sq;
		if(sq!=temp)
			continue;
		if(checkForPalindrom(sq,i))
			numOfFairs++;
	}
	out<<numOfFairs<<endl;
}

void main()
{
	int num;
	in>>num;
	for(int i=1 ; i<=num ; i++)
	{
		numOfFairs=0;
		out<<"Case #"<<i<<": ";
		solve();
	}
}
