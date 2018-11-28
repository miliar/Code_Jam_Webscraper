#include<bits/stdc++.h>
using namespace std;
void floff(char s[],int size)
{
	reverse(s,s+size);
		for(int i=0;i<size;i++)
			if(s[i]=='-')
				s[i]='+';
			else s[i]='-';
		reverse(s,s+size);	
}
int main()
{
	ifstream f1("B-large.in");
	ofstream f2("B-large-ans.in");
	int t,x=1;
	f1>>t;
	char s[103];
	while(t--)
	{
	f1>>s;
	int flip=0;
	f2<<"Case #"<<x++<<": ";
	for(int i=strlen(s)-1;i>=0;i--)
	{
		if(s[i]=='-')
		{
			flip++;
			floff(s,i+1);
		}
	}
	f2<<flip<<'\n';
	}
	f1.close();
	f2.close();
	return 0;
}
