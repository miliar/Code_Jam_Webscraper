#include<fstream.h>
#include<conio.h>
#include<iostream.h>
#include<process.h>
#include<stdio.h>

#include<math.h>

class file
{
ifstream infile;
ofstream outfile;
int ncases;
long double c,f,x;
public:
	file(int argc,char **argv)
	{
	   if (argc > 1)
	   {
	     infile .open(argv[1], ios::in);
	     if (infile == NULL)
	     {
	      cout<<"infile not found";
	      exit(0);
	     }
	   }
	   if (argc > 2)
	   {
	     outfile.open(argv[2], ios::out);
	     if (outfile == NULL)
	     {
	       cout<<"outfile error";
	       exit(0) ;
	     }
	    }
	}
	~file()
	{
	   infile.close();
	   outfile.close();
	}
	int getintial()
	{  char  ch;
	 infile>>ncases;
	 return ncases;
	}
       void getline(char str[])
       {
	 infile.getline(str,20)  ;
       }
       int getncases()
       {
       return ncases;
       }
       void writeline(char str[])
       {
	outfile<<str;
       }
       void writeline(char str[],int n,char str2[])
       {
       outfile<<str<<n<<str2;
       }
       void writeline(long double n)
       {
	outfile<< n;
       }
       void getvalues()
       {
	infile>>c;
	infile>>f;
	infile>>x;
       }

      void display()
      {   int i,j;
      cout<<"c="<<c<<"f="<<f<<"x="<<x<<"\n" ;

       }
     void reset()
    {
      c=0.0;f=0.0;x=0.0;
    }
    void checkgame()
    {
      long double rate=2.0,ttime=0.0,newtime=0.0,pretime=0.0;
       newtime=x/rate;

       do
       {
	 pretime=newtime;
	 newtime=ttime+c/rate+x/(rate+f);
	   if(newtime<pretime)
	    {
	      ttime=ttime+c/rate ;
	     rate=rate+f;
	    }
       }while(newtime<pretime);
       ttime=ttime+x/rate;
       writeline(ttime);
     }


};

void main(int argc, char **argv)
{
file f1(argc,argv) ;
int nocases;
char str[20];
clrscr();
nocases=f1.getintial();
for(int i=1;i<=nocases;i++)
{
f1.writeline("Case #",i,": ");
f1.getvalues();
f1.checkgame();
f1.writeline("\n");
}

getch();
}
