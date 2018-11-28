#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream fin;
	ofstream fout;
	fin.open("B-large.in");
	fout.open("B-large.out");
	int t,i,g,j,l;
	string s;
	fin>>t;
	for(i=1;i<=t;i++)
	{
        fin>>s;
        l=s.length();
        g=1;
        for(j=1;j<l;j++)
        {
            if(s[j]!=s[j-1])
            g++;
        }
        if(s[0]=='+' && s[l-1]=='-')
        fout<<"Case #"<<i<<": "<<g<<endl;
        else if(s[0]=='+' && s[l-1]=='+')
        fout<<"Case #"<<i<<": "<<g-1<<endl;
        else if(s[0]=='-' && s[l-1]=='+')
        fout<<"Case #"<<i<<": "<<g-1<<endl;
        else
        fout<<"Case #"<<i<<": "<<g<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}
