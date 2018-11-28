#include <iostream.h>
#include <stdio.h>
#include <fstream.h>
#include <conio.h>

int main()
{
	long int test;
   ifstream myfile;
   myfile.open("example4.txt");
   myfile>>test;
   ofstream yourfile("output5.txt");
   int N,M;
	bool ok;
	int *rows,*cols;
	int **n;
	int i,j,max;
	for(int k=1;k<=test;k++)
	{
		ok=true;
		myfile>>N;
      myfile>>M;
      n=new int*[N];
		rows=new int[N];
		cols=new int[M];
		for(i=0;i<N;i++)
		{
			n[i]=new int[M];
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
