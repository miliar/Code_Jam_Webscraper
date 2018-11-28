#include<iostream.h>
#include<fstream.h>
#include<conio.h>
#include<math.h>

int palindrome(int n)
{
	int r=0,temp;
	temp=n;
	while(temp)
	{
		r=r*10;
		r=r+temp%10;
		temp=temp/10;
	}
	if(n==r)
		return 1;
	else
		return 0;
}

void main()
{
	int T,A,B,a,b,s=0,t=1;
	ifstream r;
	r.open("C.in",ios::in);
	ofstream w;
	w.open("Out.txt",ios::out);
	clrscr();

	r>>T;

	while(T--)
	{
		r>>A>>B; s=0;
		a=sqrt(A);
		b=sqrt(B);
		while(a<=b)
		{
			if(palindrome(a))
				if(((a*a)<=B)&&((a*a)>=A)&&palindrome(a*a))
					s++;
			a++;
		}
		w<<"Case #"<<t++<<": "<<s<<endl;
	}
	r.close();
	w.close();
	getch();
}