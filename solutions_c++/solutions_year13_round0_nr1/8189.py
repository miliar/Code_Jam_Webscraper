#include<fstream.h>
#include<conio.h>
#include<process.h>

ifstream fin("cjq1.in");
ofstream f("cjout1.txt");

void main()
{
clrscr();

char a[10][4][4], s;
int t, x, y, z;
int w=0, d=0 ;


fin>>t;

for( z=0; z<t; z++ )
for( x=0; x<4; x++ )
for( y=0; y<4; y++ )
fin>>a[z][x][y];

fin.close();

for( z=0; z<t; z++ )
{
   w=0, d=0 ;


   for( x=0; x<4; x++ )
   {
      if( a[z][x][0]=='O' )
	 {
	   if( (a[z][x][1]=='O' || a[z][x][1]=='T')&&(a[z][x][2]=='O' || a[z][x][2]=='T')&&(a[z][x][3]=='O' || a[z][x][3]=='T') )
	   { w=1; s='O'; break;}
	 }

      else if ( a[z][x][0]=='X' )
	 {
	   if( (a[z][x][1]=='X' || a[z][x][1]=='T')&&(a[z][x][2]=='X' || a[z][x][2]=='T')&&(a[z][x][3]=='X' || a[z][x][3]=='T') )
	   { w=1; s='X'; break;}
	 }


      else if( a[z][x][0]=='T' )
	 {
	   if( a[z][x][1] =='O' && a[z][x][2] =='O' &&a[z][x][3] =='O')
	   { w=1; s='O'; break; }


	   else if( a[z][x][1] =='X' && a[z][x][2] =='X' &&a[z][x][3] =='X')
	   { w=1; s='X'; break; }

	 }
   }

 if( w==0 )
  {
   for( y=0; y<4; y++ )
   {
       if( a[z][0][y]=='O' )
	 {
	   if( (a[z][1][y]=='O' || a[z][1][y]=='T')&&(a[z][2][y]=='O' || a[z][2][y]=='T')&&(a[z][3][y]=='O' || a[z][3][y]=='T') )
	   { w=1; s='O'; break;}
	 }

      else if ( a[z][0][y]=='X' )
	 {
	   if( (a[z][1][y]=='X' || a[z][1][y]=='T')&&(a[z][2][y]=='X' || a[z][2][y]=='T')&&(a[z][3][y]=='X' || a[z][3][y]=='T') )
	   { w=1; s='X'; break;}
	 }


      else if( a[z][0][y]=='T' )
	 {
	   if( a[z][1][y] =='O' && a[z][2][y] =='O' &&a[z][3][y] =='O')
	   { w=1; s='O'; break; }


	   else if( a[z][1][y] =='X' && a[z][2][y] =='X' &&a[z][3][y] =='X')
	   { w=1; s='X'; break; }

	 }

   }
  }

 if( w==0 )    //diagonal
  {
    if( a[z][0][0]=='O' || a[z][0][0]=='T' )
	 {
	   if( (a[z][1][1]=='O' || a[z][1][1]=='T')&&(a[z][2][2]=='O' || a[z][2][2]=='T')&&(a[z][3][3]=='O' || a[z][3][3]=='T') )
	   { w=1; s='O'; }
	 }

    else if ( a[z][0][0]=='X'|| a[z][0][0]=='T' )
	 {
	   if( (a[z][1][1]=='X' || a[z][1][1]=='T')&&(a[z][2][2]=='X' || a[z][2][2]=='T')&&(a[z][3][3]=='X' || a[z][3][3]=='T') )
	   { w=1; s='X';}
	 }

 }

 if( w==0 ) // diag 2
 {
	 if( a[z][0][3]=='O'|| a[z][0][3]=='T' )
	 {
	   if( (a[z][1][2]=='O' || a[z][1][2]=='T')&&(a[z][2][1]=='O' || a[z][2][1]=='T')&&(a[z][3][0]=='O' || a[z][3][0]=='T') )
	   { w=1; s='O'; }
	 }

    else if ( a[z][0][3]=='X'|| a[z][0][3]=='T' )
	 {
	   if( (a[z][1][2]=='X' || a[z][1][2]=='T')&&(a[z][2][1]=='X' || a[z][2][1]=='T')&&(a[z][3][0]=='X' || a[z][3][0]=='T') )
	   { w=1; s='X'; }
	 }

  }


if( w==0 )
{
  for( x=0; x<4; x++ )
  for( y=0; y<4; y++ )
 {
  if( a[z][x][y]=='.')
  d=1;
 }

}


if( d==1 )
  f<<"Case #"<<z+1<<": "<<"Game has not completed\n";


else if( w==1 )
f<<"Case #"<<z+1<<": "<<s<<" won\n";

else if( w==0 && d==0 )
f<<"Case #"<<z+1<<": "<<"Draw\n";


}

f.close();

getch();
}