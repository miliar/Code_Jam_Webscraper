#include<fstream.h>
#include<conio.h>
#include<math.h>

ifstream fin("C1.in");
ofstream f("cjout3.txt");

int palin( int i )
{
 int s=0, n;
 n=i;

  while( i!=0 )
  {
     s=s*10+(i%10);
     i=i/10;
  }

  if( s==n )
  return 1;
  else
  return 0;
}

void main()
{
clrscr();

int a[100], b[100], t, p[100], q[100], x, y, s=0;

fin>>t;

for( x=0; x<t; x++ )
{
fin>>a[x]>>b[x];
}

fin.close();

for( x=0; x<t; x++ )
{
p[x]=sqrt(a[x]);
q[x]=sqrt(b[x]);
}

for( y=0; y<t; y++ )
{s=0;
for( x=p[y]; x<=q[y]; x++ )
{
    if( palin(x) )
    {
       if( x*x>=a[y] && x*x<=b[y] && palin(x*x) )
       s++;
    }
}

f<<"Case #"<<y+1<<": "<<s<<endl;
}

f.close();
getch();
}