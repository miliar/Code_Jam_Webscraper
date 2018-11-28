#include<iostream.h>
#include<conio.h>
#include<fstream.h>
void main()
{clrscr();
int a[100],b,t,n=1,r=0,p=0;
char ch;
ifstream in;
in.open("input.txt");
while(!in.eof())
{fl1>>t;
do{     r=0;p=0;
	cin>>b;
	fl1>>ch;
	for(i=0;i<=b;i++)
	{fl1>>ch;
	a[i]=ch-48;
	}
	p=a[0];
	for(i=1;i<=b;i++)
	{if(i>p)
	r+=i-p;
	p+=r+a[i];}
	cout<<"Case #"<<n<<": "<<r;
	n++;}

getch();
}

