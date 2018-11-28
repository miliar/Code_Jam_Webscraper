#include<iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
	int n,i=0,j=0,k,cnt;
	int check[100];
	string s;
	int cal=0,cal2=0,cal3=0,succ;
	ifstream inFile("A-small-attempt0.in");
	ofstream outFile("output.txt");
	cin>>n;
	for(i=1;i<=n;i++)
	{
		cin>>s;
		cnt=0;
		cout<<"Case #"<<i<<": ";
		for(j=1;j<s.length();j++)
		{
			//if(s[0]=='+')check[j]=0;
			//else if(s[0]=='-')check[j]=1;
			if(s[j]!=s[j-1])cnt++;
		}
		if(s[0]=='-'&&cnt%2==1)cout<<cnt;
		else if(s[0]=='-'&&cnt%2==0)cout<<cnt+1;
		else if(s[0]=='+'&&cnt%2==1)cout<<cnt+1;
		else cout<<cnt;
		cout<<endl;
	}
	
	outFile.close();
    inFile.close();

	return 0;
}