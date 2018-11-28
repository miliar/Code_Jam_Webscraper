#include<iostream.h>
#include<conio.h>
#include<fstream.h>
#include<stdio.h>


unsigned char ch;
int a[100][100]    ,   d[100][100];
int b = 0   ,   f = 0   ,  greatest = 0  ,  check = 0  ,  g = 0  ,  h = 0  ,  r = 0  ,  c = 0  ,  t = 0  ,  s = 0  ,  i = 0  ,  j = 0  ,  row_d = 0  ,  col_d = 0  ;

ifstream in("rojo.txt");
ofstream out("pat.txt");


int test_case();
void row_col_reader();
void array_initializer();
void display();
void evaluate();
void final();

void main()
{clrscr();
b = test_case();
cout<<b;
while(f!=b)
{ greatest = 0  ,  check = 0  ,  g = 0  ,  h = 0  ,  r = 0  ,  c = 0  ,  t = 0  ,  s = 0  ,  i = 0  ,  j = 0;
row_col_reader();
cout<<"\n"<<r<<" "<<c;
array_initializer();
display();
evaluate();
final();
f=f+1;
}
getch();
}


int test_case()
{
in.seekg(0);
in.get(ch);
h=(int)ch-48;
in.get(ch);
   while(ch!='\n')

     {
       h  =  ( h * 10 ) + ( (int)ch - 48  )  ;
       in.get(ch);
     }
return h;}

void row_col_reader()
{ in.get(ch);
g=(int)ch-48;
in.get(ch);
while(ch!=' ')
{g=(g*10)+((int)ch-48);
in.get(ch);
}
r=g;
in.get(ch);
g=(int)ch-48;
in.get(ch);
while(ch!='\n')
{g=(g*10)+((int)ch-48);
in.get(ch);
}
c=g;

 }

void array_initializer()
{
for(i=0;i<r;i++)
{ for(j=0;j<c;j++)
   {in.get(ch);
    a[i][j]=(int)ch - 48;
    in.get(ch);
    while( (ch!=' ') && (ch!='\n') &&((int)ch!=255) )
    {a[i][j]=(a[i][j]*10) + ( (int)ch -48);
     in.get(ch);
    }
    if(a[i][j] > greatest)
    {greatest=a[i][j];}

   }
}

}



void display()
{ for( i = 0 ; i < r ; i++)
    { cout<<"\n";
      for( j = 0 ; j < c ; j++)
	 {
	   cout<<a[i][j]<<" ";
	 }

    }
i = 0, j = 0;

while( (ch!='\n') && ( (int)ch !=255) )
{in.get(ch);
}
}

void evaluate()
{if((r!=1)&&(c!=1))
{for(i=0;i<r;i++)
{
for(j=0;j<c;j++)
{ row_d=0,col_d=0;
  if(a[i][j]==greatest)
  {d[i][j]=2;}
  if(a[i][j]!=greatest)
  {while(row_d<r)
    {
    if( a[i][j] != a[row_d++][j])
      { d[i][j] = 1;
	break;
      }
    else
     {d[i][j] = 2;
     }
   }
  if(d[i][j]==1)
  {while(col_d<c)
    {
      if( d[i][j]==1)
	{
	 if(a[i][j]!=a[i][col_d++])
	   { d[i][j]=0;
	     break;
	   }
	}
     }
   }

 if(a[i][j]==greatest)
  {d[i][j]=2;}
}
}
}

row_d=0,col_d=0;}
else if((r==1)||(c==1))
{
for(i=0;i<r;i++)
{
for(j=0;j<c;j++)
{d[i][j]=2;
}
}
}
}

void final()
{
for(i=0;i<r;i++)
{cout<<"\n";
for(j=0;j<c;j++)
{
cout<<d[i][j]<<" ";
}
}
i=0,j=0;
for(i=0;i<r;i++)
{
for(j=0;j<c;j++)
{if(d[i][j]==0)
 {out<<"Case #"<<f+1<<": NO\n";
 check=1;
 break;
 }
}
if(check==1)
{break;}
}
if(check!=1)
{out<<"Case #"<<f+1<<": YES\n";}

}