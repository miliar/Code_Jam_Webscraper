#include<iostream>
#include<string>
using namespace std;

int x[10];

void reset()
{
	for(int i=0;i<=9;i++)
		x[i]=i;
}

bool check()
{
	int i;
	for(i=0;i<=9;i++)
		if(x[i]!=-1)
			break;
	if(i!=10)
		return 0;
	
	return 1;
}

long int last_number(long int);



int main()
{
	int t,i;
	long int n[101];
	cin>>t;
	for(i=1;i<=t;i++)
		cin>>n[i];
	for(i=1;i<=t;i++)
	{
		if(n[i]==0)
			cout<<"Case #"<<i<<": INSOMNIA\n";
		else
			cout<<"Case #"<<i<<": "<<last_number(n[i])<<endl;
	}
	
	return 0;
}

long int last_number(long int a)
{
	int p=a;
	reset();
	
	for(int j=1;;j++)
	{
		a=p*j;
		string s= to_string(a);
		
		for(int i=0;s[i]!='\0';i++)
		{
			int m=-48+int(s[i]);		//s[i] is char type
			x[m]=-1;
		}
		
		if(check())
			return a;
	}
}
