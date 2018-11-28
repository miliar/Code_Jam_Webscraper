#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main(){
	ifstream input("input.txt");
	ofstream output("output.txt");
int t;
input>>t;
string s[1000];
string s1;
for(int i=0;i<t;i++)
{
input>>s[i];
}
for(int i=0;i<t;i++)
{s1=s[i][0];
	for(int k=1;k<s[i].size();k++)
	{
	if(s[i][k]>=s1[0])
		s1.insert(0,1,s[i][k]);
	else
		s1.push_back(s[i][k]);
	}
	output<<"case #"<<i+1<<": "<<s1<<endl;
}
}