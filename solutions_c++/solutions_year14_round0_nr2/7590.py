#include<stdio.h>
#include<conio.h>
#include<fstream.h>
#include<iostream.h>
void main()
{
	double c,f,x,r,r1;
	double s1,s2,pen;
	 clrscr();
	for(int i=1;i<=3;i++)
	{

		cout<<"c=";
		cin>>c;

		cout<<"f";
		cin>>f;

		cout<<"x";
		cin>>x;

		r=2;
		r1=r+f;
		pen=0;
		pen=pen+(c/r);

		s1=x/r;
		s2=(x/r1)+pen;
	  while(1)
	  {
		if(s1<s2)
		{
			cout<<s1;
			break;
		}
		else
		{
			r=r1;
			r1=r1+f;
			pen=pen+(c/r);
			s1=s2;
			s2=(x/r1)+pen;
		}
	   }

	}
		getch();
}