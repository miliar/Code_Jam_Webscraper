#include<bits/stdc++.h>
using namespace std;
int main()
{ifstream in;
    ofstream out;
    in.open("input.txt");
    out.open("output.txt");
    int t;
    in>>t;
     for(int j = 1;j<=t;j++)
{

	string s,s2;
	in>>s;
	s2 = "";

	for(int i = 0;i< s.length() ; i++)
	{
		if(s[i]>=s2[0])
			s2 = s[i] + s2;
		else s2  = s2 + s[i];
		}
		out<<"Case #"<<j<<": "<<s2<<endl;

}
	return 0;
}
