#include<iostream.h>
#include<fstream.h>
#include<conio.h>

void main()
{
	int t,R,T,c,R1,ctr=0;
//	unsigned long long t;
	ifstream r;
	clrscr();
	r.open("SA.in",ios::in);
	ofstream w;
	w.open("Out.txt",ios::out);
	r>>T;

	while(T--)
	{
		c=0;
		r>>R>>t;
		R1=R+1;
		while(t>=0)
		{
			int k;
			c++;
			k=((R1*R1)-(R*R));
			t-=k;
			R+=2;
			R1+=2;
		}
		c--;
		w<<"Case #"<<++ctr<<"= "<<c<<endl;
	}
	r.close();
	w.close();
	getch();
}