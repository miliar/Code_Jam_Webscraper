#include<iostream>
#include<string>
using namespace std;
int main()
{int t,d=1;
cin>>t;
do{

string s,s1;
cin>>s;

char arr[2100];
char *w;
for(int i=0;i<2100;i++)
{
arr[i]='*';	
	
}


char *q;
q=&arr[0];
w=&s[0];
int i=1000,j=1000;
 arr[i]=*w;
//converting to ascii
int a=*w;

w++;
while(*w!='\0')
{
	int b=*w;
	
	if(b>=a)
	{i=i-1;
	arr[i]=*w;
	a=b;	
		
	}
	else{
		j=j+1;
		arr[j]=*w;
	}
	
	w++;
}
j=j+1;
arr[j]='\0';
cout<<"Case #"<<d<<": ";	
while(*q!='\0')
{
	if(*q!='*')
	{
		cout<<*q;
	}
	q++;
	}	
	cout<<endl;
d++;}while(d<=t);
	
	return 0;
}
