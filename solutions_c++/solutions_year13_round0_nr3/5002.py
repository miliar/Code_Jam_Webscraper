#include<iostream.h>
#include<conio.h>
#include<stdio.h>
#include<fstream.h>
#include<math.h>

ifstream in("rojo2.txt");
ofstream out("patrick.txt");
int a=0,b=0,c=0,i=0,s=0,l=0,d=0,k=0,r=0;
unsigned char ch;
int test_cases();
void range_reader();
void calc();
void pal_check(int );

void main()
{clrscr();
b=test_cases();
cout<<b;
for(k=0;k<b;k++)
{r=0,s=0,l=0;
range_reader();
calc();
cout<<"\n"<<r;
out<<"Case #"<<k+1<<": "<<r<<"\n";
}
in.close();
out.close();
getch();
}

int test_cases()
{in.seekg(0);
in.get(ch);
a = (int)ch - 48;
in.get(ch);
while(ch!='\n')
{a = ( a * 10 ) + ( (int)ch -48);
 in.get(ch);
}
return  a;
}

void range_reader()
{in.get(ch);
c = (int)ch - 48;
in.get(ch);
while( ch!=' ' )
 {
  c = (c*10) + ( (int)ch -48);
  in.get(ch);
 }
if( (sqrt(c)-((int)sqrt(c)))!=0)
{s=(int)sqrt(c)+1;}
else{s=(int)sqrt(c);}
cout<<"\n"<<s<<" ";
in.get(ch);
c=(int)ch -48;
in.get(ch);
while( (ch!='\n')&&((int)ch!=255))
{c=(c*10)+((int)ch-48);
in.get(ch);
}
l=(int)sqrt(c);
cout<<l;
}


void calc()
{
for(i=s;i<=l;i++)
{ pal_check(i);
}
}

void pal_check(int p)
{if ( p/10== 0)
  {
    if( (p*p)<10)
      {
	r++;
      }
  }
 else if( ((p/10)>0) && ((p/10)<10))
  {
    if( (p%10)==(p/10))
      {
	r++;
      }
  }
 else if( ((p/10)>9) && ((p/10)<100))
  {
    if( (p%10)==(p/100))
      {
	r++;
      }
  }
 else if( ((p/10)>99) && ((p/10)<1000))
  {
    if( (p%100)==(p/100))
      {
	r++;
      }
  }
}