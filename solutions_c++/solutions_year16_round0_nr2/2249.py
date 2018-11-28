#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

int Pancacke(vector<char>& v)
{

	bool all_plus=true;
	int plus1=-1,i;
	for(i=0;i<v.size();i++)
		if(v[i]=='-') {all_plus = false; break;}
	if(all_plus==true)
		return 0;
	if(v[0]=='+')
	{
		for(i=1;i<v.size();i++)
		{
			if(v[i]=='-')
				plus1=i;
			if(plus1!=-1 && v[i]=='+')
				break;
		}
		for(i=0;i<plus1+1;i++)
			v[i]='+';
		return 2+Pancacke(v);
	}
	else
	{
		for(i=0;(v[i]!='+')&&(i<v.size());i++)
			v[i]='+';
		return 1+Pancacke(v);
	}
}

int main(int argc, char const *argv[])
{
	ifstream input("B.in");
	ofstream output("B.out");
	string s;
	int i,j=1;
	getline(input,s);
	while(getline(input,s))
	{
		vector<char> v;
		for(i=0;i<s.size();i++)
			v.push_back(s.at(i));
		output<<"Case #"<<j<<": "<<Pancacke(v)<<endl;
		j++;
	}
	input.close();
	output.close();
	return 0;
}