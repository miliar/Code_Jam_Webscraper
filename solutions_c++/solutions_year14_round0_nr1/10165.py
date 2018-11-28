#include<conio.h>
#include<iostream.h>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<fstream.h>
static char *filepath="input.in";
static char *opfile="opt.in"  ;


void  fprint(int cas,char *txt,int dl)
{
filebuf fb1;
fb1.open(opfile,ios::out|ios::ate);
if(dl==1)
{
ostream o_file(&fb1);
o_file<<"Case #"<<(cas+1)<<": "<<txt<<"\n";
fb1.close();
}
else
{
fb1.close();
remove(opfile);
}

}



char* logic(int a1,int mat1[4][4],int a2,int mat2[4][4])
{

for(int c=0;c<4;c++)
{
 cout<<"  "<<mat1[a1-1][c];
}
cout<<"\n";
for( c=0;c<4;c++)
{
 cout<<"  "<<mat2[a2-1][c];
}

 int z= 0;
 char *tm;
for(int i=0;i<4;i++)
{
 for(int j=0;j<4;j++)
 {
  if(mat1[a1-1][i]==mat2[a2-1][j])
  {
    ++z;
    itoa(mat1[a1-1][i],tm,10);

  }
 }
}

 switch(z){
  case 0:
	return "Volunteer cheated!";

  case 1:
  {

   return tm;;

   }

 }

return "Bad magician!";
}










void main()
{
int tc,a,i,j;
filebuf fb;


clrscr();
//sprintf(opfile,"%s%s",filepath,"-output.in");
fprint(0,NULL,0);
if(fb.open(filepath,ios::in))
{
 istream is(&fb);
 char t;
 char *tmp;
   t = is.get();
 for( a=0;!(is.eof())&&!(t=='\n')&&a<3;a++)
 {
	tmp[a]=t;
	t = is.get();
 }
 tmp[a]='\0';



if(1<=atoi(tmp)<=100)
{
 tc=atoi(tmp);
}


	for(int atc=0;atc<tc;atc++)
	{
	    int c1,c2,arg1[4][4],arg2[4][4];
	    t=is.get();
	    for( a=0;!(is.eof())&&!(t=='\n')&&a<3;a++)
	    {
		tmp[a]=t;
		t = is.get();
	    }
	    tmp[a]='\0';
	    c1=atoi(tmp);
	    for(i=0;i<4;i++)
	    {
	     for(j=0;j<4;j++)
	     {
	       t = is.get();
	       a=0;
	       while(!(t==' ')&&!(t=='\n'))
	       {
		tmp[a]=t;
		t = is.get();
		a++;
	       }
	       tmp[a]='\0';
	       arg1[i][j]=atoi(tmp);

	      }

	     }

	    t = is.get();
	    for( a=0;!(is.eof())&&!(t=='\n')&&a<3;a++)
	    {
		tmp[a]=t;
		t = is.get();
	    }
	    tmp[a]='\0';
	    c2=atoi(tmp);

	    for(i=0;i<4;i++)
	    {
	     for(j=0;j<4;j++)
	     {
	       t = is.get();
	       a=0;
		while(!(t==' ')&&!(t=='\n'))
		{
		  tmp[a]=t;
		  t = is.get();
		  a++;
		}
	       tmp[a]='\0';
	       arg2[i][j]=atoi(tmp);
	      }
	     }


	    char *fck=logic(c1,arg1,c2,arg2)   ;
	    cout<<"\n  "<<fck<<"\n";
	    fprint(atc,fck,1);


      }
 fb.close();
}
getch();
}
