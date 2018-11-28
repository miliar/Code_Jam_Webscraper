#include <iostream.h>
#include <fstream>
#include <string>
using namespace std;
main()
{
	ifstream inn("B-large.in");
	ofstream out("q2o.txt");
	string s1;
	long cases;
	inn>>cases;
	long c1=0;
	long c;
	char p;
	
	for(long rrr=1; rrr <= cases ; rrr++)
	{
		
		inn>>s1;
		
		c=0;
		for(long i=0;i<s1.length();i++)
		{
			if (s1[i]=='-' and (i+1)==s1.length())
				c++;
			else if((s1[i]!=s1[i+1])&&(i!=s1.length()-1))
			{
				c++;
			}
			
		}
	/*
		for(long i=0;i<s1.length()-1;i++)
		{
			if(s1[i]!=s1[i+1])
			{
				p=s1[i+1];
				for(long k=0;k<i+1;k++)
				{
					s1[k]=p;
				}
				c++;
			}else if(s1[i]==s1[i+1])
				continue;			

		}
		if(s1[0]='-')
			c++;
			*/	
		out<<"Case #" << rrr << ": " << c<<endl;
	}
	
}
