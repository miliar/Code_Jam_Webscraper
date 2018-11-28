#include<iostream>
#include<string.h>
using namespace std;
int main()
{
freopen("B-Large.in","r",stdin);
freopen("output-b-large.out","w",stdout);
int t;     //no. of test cases
char s[100];     //for input of string
int l;   //for length of string,flag value
int v;   //variations in the string array
int x=1;
cin>>t;
 while(t--)
 {
 	cin>>s;
 	l=strlen(s);
 	v=0;
 	 for(int i=0;i<l;i++)
 	 {
 		if(s[i]!=s[i+1])
 		v++;
	 }	
	 if(s[l-1]=='+')
	 v--;
	cout<<"Case #"<<x<<": "<<v<<endl;
	x++;
 }
return 0;	
}
