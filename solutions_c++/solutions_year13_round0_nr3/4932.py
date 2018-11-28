

#include<iostream>
#include<cmath>
#include<math.h>
#include<string>
#include<sstream>
#include<fstream>

using namespace std;

bool palindrome(string a)
{
	return(a==string(a.rbegin(),a.rend()));

 }



int main()
{
	string a;
	int num=0;
	int x=0,y=1,t,aa=1;
	stringstream c,d;

	ifstream in("C-small-attempt0.in");
	ofstream out("out.txt");

	in>>t;




	while(t--)
	{
		in>>x>>y;
		for(;x<=y;x++)
		{
			
			c<<x;
			d<<sqrt((double)x);
			if(palindrome(c.str())&&palindrome(d.str()))
				num++;
			c.str("");
			d.str("");
		}
		out<<"Case #"<<aa++<<": "<<num<<"\n";
		num=0;
	}

	return 0;
		
}
