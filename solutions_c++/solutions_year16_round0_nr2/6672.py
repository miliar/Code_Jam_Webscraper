#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ifstream in;
	ofstream out;
	in.open("B-large.in");
	out.open("outl.txt");
	int j=1, t;
	in>>t;
	while(j<=t){
		string s;
		in>>s;
		bool flag=0;
		int count=0;
		if(s[0]=='+') flag=1;
		for(int i=1;i<s.length();i++){
			if(flag==0 && s[i]=='+') count++, flag=1;
			else if(flag==1 && s[i]=='-') count++, flag=0;
		}
		if(s[s.length()-1]=='-') count++;
		out<<"Case #"<<j<<": "<<count<<endl;
		j++;
	}
	in.close();
	out.close();
	return 0;
}
