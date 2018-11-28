#include<iostream.h>
#include<conio.h>
#include<fstream.h>
#include<stdio.h>
ifstream in("rojo.txt");
ofstream out("pat.txt");
int a,b,c,d,e,f;
int test_case();
int rad();
int paint();
int evaluate(int a, int b);
void main()
{clrscr();
a = test_case();
cout<<a;
for(int i=0;i<a;i++)
{b=rad();
c=paint();
d=evaluate(b,c);
out<<"Case #"<<i+1<<": "<<d<<"\n";
}
in.close();
out.close();
getch();
}
int test_case()
{in.seekg(0);
int a;
unsigned char ch;
in.get(ch);
a = (int)ch - 48;
in.get(ch);
while( ch != '\n')
{ a = (a * 10) + ( (int)ch - 48);
in.get(ch);
}
return a;
}
int rad()
{int a,b;
unsigned char ch;
in.get(ch);
a= (int)ch - 48;
in.get(ch);
while(ch != ' ')
{a = (a * 10) + ((int)ch -48);
in.get(ch);
if( (int)ch ==255)
{break;}
}
return a;
}
int paint()
{int a,b;
unsigned char ch;
in.get(ch);
a= (int)ch -48;
in.get(ch);
while ( (ch !='\n') && ( (int)ch != 255) )
{a=(a*10) + ((int)ch -48);
in.get(ch);
}
return a;
}
int evaluate(int a, int b)
{unsigned char ch;
int c,d=1,e=1;
c=d* ( (2*d) + (2*a) -1);
while((b/c) !=0)
{d++;
c=d* ( (2*d) + (2*a) -1);
e++;
}
cout<<"\n"<<e-1;
return (e-1);
}