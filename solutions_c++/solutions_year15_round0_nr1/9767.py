#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	int i,j,t;
	ifstream data("input");
	data>>t;
	
	for(i=0;i<t;i++)
	{
		int len,x=0,y=0;
		char str[10];
		data>>len>>str;
		x=str[0]-48;
		for(j=1;j<=len;j++)
		{
			if((x+y)>=j)
				x=x+(str[j]-48);
			else
			{
				y=j-x;
				x=x+(str[j]-48);
			}
		}
		fstream result;
		result.open("output",ios::app|ios::out);
		result<<"Case #"<<(i+1)<<": "<<y<<"\n";
	}
	
}
