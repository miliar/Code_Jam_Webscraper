#include<iostream>
#include<string.h>
#include<fstream>
using namespace std;

int cmp(char a, char b);

int main()
{
	int i,t,tt;
	string s,f;
	ofstream myfile;
	myfile.open("Output.txt");;
	cin>>t;
	for(tt=1;tt<=t;tt++)
	{
	cin>>s;
	f=s[0];
	for(i=1;i<s.length();i++)
	{
		if(cmp(f[0],s[i])<0)
		f=f+s[i];
		else
		f=s[i]+f;
	}
	myfile<<"Case #"<<tt<<": ";
	myfile<<f<<endl;
}
myfile.close();
}

int cmp(char a, char b)
{
	if((int)a>(int)b)
    return -1;
    return 1;
}
