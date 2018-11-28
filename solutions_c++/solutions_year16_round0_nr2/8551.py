#include<iostream>
#include<fstream>
#include<string>
#include<string.h>
using namespace std;
int main()
{
	long long t1,n;
	ifstream inp("input.txt");
	ofstream out("output.txt");
	string line;
	inp>>t1;
	//cout<<t1<<endl;
	for(long long it=1;it<=t1;it++)
	{
		char pr,curr,str[1000];
		//getline (inp,line);
		inp>>str;
		//cout<<str<<endl;
		int count=0,l=strlen(str);
		pr=str[0];
		int i;
		for(i=0;str[i]!='\0';i++)
		{
			curr=str[i];
			if(curr!=pr)
				count++;
			pr=curr;	
		}
		if(str[i-1]=='-')
			count++;
		out<<"Case #"<<it<<": "<<count<<endl;	
	}
	inp.close();
	out.close();
}
