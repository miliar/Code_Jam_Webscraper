#include<iostream>
#include<fstream>
#include<string>
#include<math.h>
using namespace std;
	
	
class fairnSquare{
public:
long int tCases,a,b,x,count;
string strng;

void read(ifstream& in,ofstream& out)
{
	in>>tCases;
	
	for(long int i=1;i<=tCases;i++)
	{
		count =0;
		this->isFairnSquare(in);
		out<<"Case #"<<i<<": "<<count<<endl;
	}
}

void isFairnSquare(ifstream& in)
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
	fairnSquare a;
	in.open("input.in",ios::binary);
	out.open("output.in",ios::out);
	a.read(in,out);
 return 0;
}