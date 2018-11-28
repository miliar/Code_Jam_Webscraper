#include<iostream>
#include<cmath>
#include<fstream>
#include <sstream>
using namespace std;

bool isPalindrome(int num)
{
	std::string s;
	std::stringstream out;
	out << num;
	s = out.str();
	string t = string ( s.rbegin(), s.rend() );
	if(s==t)
		return true;
	else
		return false;
}

int main()
{
	int a,b,c,t;
	ifstream fin("input.in");
	ofstream fout("out.txt");
	fin>>t;
	for(int x=0;x<t;x++)
	{
		fin>>a>>b;
		c=0;
		int art,brt;
		art=(int)sqrt(a);
		brt=(int)sqrt(b);
		if(art*art!=a)
			art++;
		for(int i=art;i<=brt;i++)
			if(isPalindrome(i*i)&&isPalindrome(i))
				c++;
		fout<<"Case #"<<x+1<<": "<<c<<endl;
	}
	return 0;
}