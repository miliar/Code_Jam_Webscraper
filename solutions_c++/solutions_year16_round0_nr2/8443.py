#include<iostream>
#include<string>
#include<fstream>
#include<unistd.h>
#include<stdlib.h>
 
using namespace std;
 
int main()
{
	ifstream infile("B-large.in");
	ofstream outfile("result3.txt");
	int t;
	string temp;
	getline(infile,temp);
	t=atoi(temp.c_str());
	int counter=0;
	while(t--)
	{
 			counter++;
			string s;
		//	cin>>s;
		getline(infile,s);
			int count=0;
			for(int i=0;i<s.length()-1;i++)
				{
					if(s[i]!=s[i+1])
						count++;
				}
 
			if(s[s.length()-1]=='-')
				count++;
			//cout<<count;
			outfile<<"Case #"<<counter<<": "<<count<<"\n";
	}
	//close(outfile);
	//close(infile);
	return 0;
}
 
 
				
