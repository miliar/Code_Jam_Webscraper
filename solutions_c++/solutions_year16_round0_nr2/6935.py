#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int numberOfFlips(char *A)
{
	int n=0;
	for(int i=0;A[i]!='\0';i++)
		if( (A[i]=='-' && A[i+1]!='-') || (A[i]=='+' && A[i+1]=='-') )
			n++;
	return n;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	char A[100];
	cin>>T;
	cin.ignore();
	for(int i=1;i<=T;i++)
	{
		gets(A);
		cout<<"Case #"<<i<<": "<<numberOfFlips(A)<<endl;
	}
}
