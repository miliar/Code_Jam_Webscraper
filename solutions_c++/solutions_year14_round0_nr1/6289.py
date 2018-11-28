#include<fstream.h>
#include<conio.h>
#include<iostream.h>
#include<process.h>
#include<stdio.h>

class file
{
ifstream infile;
ofstream outfile;
int ncases;
int ans1;
int ans2;
int pattern1[4][4];
int pattern2[4][4];
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
       void writeline(int n)
       {
	outfile<<n;
       }
       void getans1()
       {

	  char  ch;
	 infile>>ans1;
      }
      void getpattern1()
      {
	int i=0,j=0;
	char ch;

	while(infile&&i<4)
	{
	 infile>>pattern1[i][j];

	 infile>>pattern1[i][j+1];

	 infile>>pattern1[i][j+2];

	 infile>>pattern1[i][j+3];
	 i++;
	}
      }

      void getans2()
       {
	  char  ch;
	 infile>>ans2;
      }
      void getpattern2()
      {
	int i=0,j=0;
	char ch;
	while(infile&&i<4)
	{
	 infile>>pattern2[i][j];
	 infile.get(ch);
	 infile>>pattern2[i][j+1];
	 infile.get(ch);
	 infile>>pattern2[i][j+2];
	 infile.get(ch);
	 infile>>pattern2[i][j+3];
	 infile.get(ch);
	 i++;
	}
      }
      void display()
      {   int i,j;
      cout<<"ans1="<<ans1<<"\n" ;
       for(i=0;i<4;i++)
       for(j=0;j<4;j++)
       cout<<pattern1[i][j]<<" ";

       cout<<"ans2="<<ans2<<"\n";
       for(i=0;i<4;i++)
       for(j=0;j<4;j++)
       cout<<pattern2[i][j]<<" ";
       cout<<"\n" ;
       }
     void reset()
     {
      ans1=0;ans2=0;
      for(int i=0;i<4;i++)
      for(int j=0;j<4;j++)
      {
       pattern1[i][j]=0  ;
       pattern2[i][j]=0;
      }
    }
    void checkcard()
    {
      int i1=ans1-1;
      int i2=ans2-1;
      int j1,j2;
      int found=0;
      int card;

     for(j2=0;j2<4;j2++)
     {
      for(j1=0;j1<4;j1++)
      {
	if(pattern2[i2][j2]==pattern1[i1][j1])
	{found++;
	  card=pattern2[i2][j2]  ;
	}
       }
     }

     if(found==1)
     {
     writeline(card);
     }
     else if(found>1)
     {
      writeline("Bad magician!")  ;
     }
     else          //found=0
     {
      writeline("Volunteer cheated!")  ;
     }

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
f1.getans1();
f1.getpattern1();
f1.getans2() ;
f1.getpattern2();
f1.checkcard();
f1.writeline("\n");
}

getch();
}
