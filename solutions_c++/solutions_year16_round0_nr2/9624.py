#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;
void change(char a[],int i);
int main()
{
	char a[100];
	int c=0,txt=0;
	int n;
	ifstream in;
    ofstream out;
    in.open("INPUT.in");
    out.open("OUTPUT.txt");
	in>>n;
	while(n>0)
	{   txt++;
		in>>a;
		int l=strlen(a);
		for(int i=l-1;i>=0;i--)
		{  if(a[i]=='-')
		   {
		   change(a,i);
		   	  c++;
			  i++;

		   }
		}
		 out<<"Case #"<<txt<<": "<<c<<endl;	
		n--;  
		c=0;
	}
}
void change(char a[],int i)
{

	for(;i>=0;i--)
	{
		if(a[i]=='+')
		a[i]='-';
		 else if(a[i]=='-')
		a[i]='+';
	}

}
