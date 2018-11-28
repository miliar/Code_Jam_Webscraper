#include<bits/stdc++.h>
#define cin fin
#define cout fout
using namespace std;
const int N=1e5+5;

int main()
{
	ifstream fin;
	fin.open("11.in",ios::in);
	ofstream fout;
	fout.open("11.out",ios::out);
	int t;
	cin >> t;
	for(int i=1;i<=t;i++)
	{
		string s;
		cin >> s;
		cout<<"Case #"<<i<<": ";
		int z=0;
		s=s+"!";
		for(int i=0;i<s.size()-1;i++)
		{
			if(s[i]=='-' && s[i+1]!='-')
				z++;
			if(s[i]=='+' && s[i+1]=='-')
				z++;
		}
		cout<<z<<endl;
	}
	return 0;
}


