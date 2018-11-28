#include<iostream>
#include<fstream>
#include<stdio.h>
#include<string.h>

using namespace std;

int main()
{
	int t,n,l;
	std::cin>>t;
	string s,temp,left,right;
	char ch;

	for(int k=0;k<t;k++)
	{
		std::cin>>s;
		l=s.size();
		temp.erase();
		left.erase();
		right.erase();

		for(int i=0;i<l;i++)
		{
			left.erase();
			right.erase();
			left=temp;
			right=temp;
			temp.erase();
			ch=s[i];
			left=ch+left;
			right=right+ch;
			if(left.compare(right)>0)
				temp=left;
			else
				temp=right;
		}
		std::cout<<"Case #"<<(k+1)<<": "<<temp<<"\n";
	}
	return 0;
}