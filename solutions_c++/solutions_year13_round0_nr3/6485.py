#include<iostream>
#include<fstream>
#include<string>
#include<math.h>
using namespace std;
	
	
class clas{
public:
long int g,a,b,x,y,count;
string strng;

void read(ifstream& in,ofstream& out)
{
	in>>g;
	
	for(long int i=0;i<g;i++)
	{
		count =0;
		this->chkgame(in,out);
		out<<"Case #"<<i+1<<": "<<count<<endl;
		
	}


}

void chkgame(ifstream& in,ofstream& out)
{

	in>>a>>b;
	for(;a<=b;a++)
	{

		strng= to_string(a);
		
		if ((strng == string(strng.rbegin(), strng.rend()))) 
		{

			x=sqrt(a);
			if(x*x==a)
			{strng=to_string(x);
			if (strng == string(strng.rbegin(), strng.rend())) 
			{
				count++;}
			}
		}

	}

	
}


};

int main()
{
	ifstream in;
	ofstream out;
	clas a;
	in.open("input.in",ios::binary);
	out.open("output.in",ios::out);

	a.read(in,out);
	/*
	string strng;
	for(int i=100;i<=1000;i++)
	{
		long long int x=i*i;
		long long int y=i;
		strng=to_string(x);
		if ((strng == string(strng.rbegin(), strng.rend()))) 
		{
			strng=to_string();
			if (strng == string(strng.rbegin(), strng.rend())) 
			{
				cout << i << " "<<i*i<<" is a palindrome"<<endl;
				}
		}

	}*/
system("pause");
 return 0;
}