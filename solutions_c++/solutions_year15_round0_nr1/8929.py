#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
	ofstream op;
	ifstream ip ("input.txt");
  	op.open ("output.txt");
  	int t,a,b,x=1,c;
  	string s;
  	ip>>t;
  	while(t--)
  	{
  		b=0,a=0; ip>>c;
  		ip>>s; //cout<<s<<endl;
  		a=a+s[0]-'0'; //cout<<a<<" ";
  		for(int i=1;i<s.length();i++)
  		{
  			if(a<i) { b=b+i-a; a=i;   }
  			a=a+s[i]-'0';
		  } op<<"Case #"<<x<<": "<<b<<endl;  x++; //cout<<b<<" ";
	}
	
	return 0;
}
