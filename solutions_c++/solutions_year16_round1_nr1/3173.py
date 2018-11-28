#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstring>

using namespace std;

int t;
string s;
string ss;

int main()
{
	int i,j,k;
	int tcase=1;
	int counter=0;
	freopen("in1+","r",stdin);
	freopen("out1+","w",stdout);

	cin>>t;
	for(i=1;i<=t;i++)
	{
		counter=0;
		cin>>s;
		ss=s[0];
		int len=s.length();
		for(j=1;j<=len-1;j++)
		{
			if((s[j]+ss>ss+s[j]))
			{
				ss=s[j]+ss;
			}
			else
			{
				ss=ss+s[j];
			}
		}
		if(s[len-1]=='-')
			cout<<"Case #"<<tcase++<<": "<<ss<<endl;
		else
			cout<<"Case #"<<tcase++<<": "<<ss<<endl;
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
