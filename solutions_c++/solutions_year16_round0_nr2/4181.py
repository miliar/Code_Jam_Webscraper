#include<bits/stdc++.h>
using namespace std;
int allplus(string str,int l)
{
	int done=1;
	for(int i=0;i<l;i++) if(str[i]=='-') {done=0;break;}
	return done;
}
void flip(string &str,int s,int e)
{
	for(int i=s;i<=e;i++) 
	{
		if(str[i]=='+') str[i]='-';
		else str[i]='+';
	}
}
int main()
{
	ifstream file1("B-large.in");
	ofstream file2("file22.txt");
	int t;
	file1>>t;
	for(int j=0;j<t;j++)
	{
		int count=0;
		string str;
		file1>>str;
		int l=str.length();
		file2<<"Case #"<<j+1<<": ";
		while(!allplus(str,l))
		{
			int i;
			for(i=l-1;i>=0;i--) if(str[i]=='-') break;
			flip(str,0,i);
			count++;
		}
		file2<<count<<endl;		
	}
}
