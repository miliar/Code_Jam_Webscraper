#include <iostream>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int j=0;j<t;j++)
    {
		string s;
		cin>>s;
		int num=0;
		for(int i=0;i<s.length();i++)
		{
			if(((s[i]=='+')&&(s[i+1]=='-'))||((s[i]=='-')&&(s[i+1]=='+'))) num++;
		}
		if(s[s.length()-1]=='-') num++;
		cout<<"Case #"<<j+1<<": "<<num<<endl;
    }
    return 0;
}
