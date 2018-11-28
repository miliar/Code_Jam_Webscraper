#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstring>

using namespace std;

int t;
string s;

int main()
{
	int i,j,k;
	int tcase=1;
	int counter=0;
	freopen("in2","r",stdin);
	freopen("out2","w",stdout);

	cin>>t;
	for(i=1;i<=t;i++)
	{
		counter=0;
		cin>>s;
		int len=s.length();
		for(j=0;j<=len-2;j++)
		{
			if(s[j]!=s[j+1])counter++;
		}
		if(s[len-1]=='-')
			cout<<"Case #"<<tcase++<<": "<<counter+1<<endl;
		else
			cout<<"Case #"<<tcase++<<": "<<counter<<endl;
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
