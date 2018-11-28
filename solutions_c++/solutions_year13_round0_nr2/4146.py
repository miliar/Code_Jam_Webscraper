#include <iostream.h>
#include <stdio.h>
#include <fstream.h>
#include <conio.h>

int main()
{
	int test;
   ifstream myfile;
   myfile.open("example.in");
   myfile>>test;
   ofstream yourfile("output.txt");
   long int N,M;
	bool ok;
	long int *rows,*cols;
	long int **n;
	long int i,j,max;
	for(int k=1;k<=test;k++)
	{
		ok=true;
		myfile>>N;
      myfile>>M;
      n=new long int*[N];
		rows=new long int[N];
		cols=new long int[M];
		for(i=0;i<N;i++)
		{
			n[i]=new long int[M];
			for(j=0;j<M;j++)
            myfile>>n[i][j];
		}
		for(j=0;j<M;j++)
		{
			max=0;
			for(i=0;i<N;i++)
           if(n[i][j]>max)
             max=n[i][j];
			cols[j]=max;
		}
		for(i=0;i<N;i++)
		{
			max=0;
			for(j=0;j<M;j++)
            if(n[i][j]>max)
              max=n[i][j];
			rows[i]=max;
		}
		for(i=0;i<N;i++)
			for(j=0;j<M;j++)
				if(n[i][j]!=rows[i]&&n[i][j]!=cols[j]) ok=false;
		if(ok)
         yourfile<<"Case #"<<k<<": YES\n";
		else
         yourfile<<"Case #"<<k<<": NO\n";
	}
	//return 0;
getch();
}
