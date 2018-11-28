#include<iostream.h>
#include<math.h>
#include<stdlib.h>
#include<conio.h>
#include<string.h>
#include<fstream.h>
class square
{
	ifstream fin;
	ofstream fout;
	int caseno;
	public:
	square()
	{
		caseno=0;
		fout.open("c:\\turboc3\\bin\\output.txt");
	}
	void calculate(int,int);
	void getdata();
};
void square :: calculate(int a,int b)
{
	caseno++;
	int cnt,pal,sqr,no,pali,n,temp;
	cnt=0;
	for(int i=a;i<=b;i++)
	{
		sqr=0;
		pali=0;
		for(int j=1;j<=i;j++)
		{
			if(j*j==i)
			{
				no=j;
				n=0;
				while(no!=0)
				{
					temp=no%10;
					no=no/10;
					n=(n*10)+temp;
				}
				if(n==j)
				{
					sqr=1;
					break;
				}
			}
		}
		no=i;
		n=0;
		while(no!=0)
		{
			temp=no%10;
			no=no/10;
			n=(n*10)+temp;
		}
		if(n==i)
		{
			pali=1;
		}
		if(sqr==1 && pali==1)
		{
			cnt++;
		}
	}
	fout<<"Case #"<<caseno<<": "<<cnt<<endl;
}
void square :: getdata()
{
	char ch,*a,*b,*str;
	int cnt=0;
	int nline=0;
	fin.close();
	fin.open("c:\\turboc3\\bin\\input.txt");
	while(fin)
	{
		fin.get(ch);
//		cout<<ch;
		if(ch=='\n')
		{
			nline++;
			str[cnt]='\0';
			cnt=0;
			if(nline>1)
			{
				a=strtok(str," ");
				b=strtok(NULL," ");
				int x,y;
				x=atoi(a);
				y=atoi(b);
				cout<<endl<<x<<"\t"<<y;
				//calculate(x,y);
			}
		}
		else
		{
			str[cnt]=ch;
			cnt++;
		}
	}
}
void main()
{
	clrscr();
	square s;
	s.getdata();
	getch();
}