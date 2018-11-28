#include<iostream>
#include<string>
#include<vector>
#include<math.h>
#include<algorithm>
#include<stdio.h>
using namespace std;
int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int t;
	cin>>t;
	int n;
	for(int i=0; i<t; i++)
	{
		cin>>n;
		vector <string> data(n,"");
		string s;
		vector<vector<int> > letters(n);
		int jami=0;
		for(int j=0; j<n; j++)
		{
			jami=1;
			cin>>s;
			data[j]+=s[0];
			for(int k=0; k<s.size()-1; k++)
			{
				if(s[k]==s[k+1])
					jami++;
				else
				{
					letters[j].push_back(jami);
					jami=1;
					data[j]+=s[k+1];
				}
			}
			letters[j].push_back(jami);
		}
		bool ch=false;
		for(int j=0; j<n-1;j++)
		{
			if(data[j]!=data[j+1])
			{
				cout<<"Case #"<<i+1<<": ";
				cout<<"Fegla Won"<<endl;
				ch=true;
				break;
			}
		}
		if(ch) continue;
		int sachiro;
		int sachiro1;
		int mini=0;
		int naklebi, meti;
		int jami1, jami2;
		for(int j=0; j<letters[0].size();j++)
		{
			jami=0;
			naklebi=0; meti=0;
			for(int k=0; k<n; k++)
			{
				jami+=letters[k][j];
			}
			sachiro=jami/n;
			sachiro1=sachiro+1;
			jami1=0; jami2=0;
			for(int k=0; k<n; k++)
			{
				jami1+=abs(letters[k][j]-sachiro);
				jami2+=abs(letters[k][j]-sachiro1);
			}
			mini+=min(jami1, jami2);
		}
		cout<<"Case #"<<i+1<<": ";
		cout<<mini<<endl;
	}
	return 0;
}