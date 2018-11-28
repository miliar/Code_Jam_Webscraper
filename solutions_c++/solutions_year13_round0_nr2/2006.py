#include<fstream>
#include<iostream>
int no[100][100];
int m,n;
int check(int a,int b);
using namespace std;
int main()
{  
   ifstream fin;
   ofstream fout;
   fin.open("input.in",ios::in);
   fout.open("output",ios::out);
   int flag,T;
   int i,j;
   fin>>T;
   for(int l=0;l<T;l++)
    {
	flag=1;
	fin>>n>>m;
	for(i=0;i<n;i++)
	{
		for(j=0;j<m;j++)
		{
		fin>>no[i][j];
		}
	}

	if((m==1)||(n==1));
	else
	{

	 for(i=0;i<n;i++)
	 {
	 	for(j=0;j<m;j++)
	 	{
	 		if( (check(i,j)) == 0) { flag=0; break; }
	 	}
	 }


	}



	
      if(flag==1) fout<<"Case #"<<l+1<<": YES\n";
      else fout<<"Case #"<<l+1<<": NO\n";
    }
return 0;
}


int check(int a,int b)
{
int flag,i;

flag=0;

for(i=0;i<m;i++)
{
if(no[a][i]>no[a][b]) flag=1;
}
if(flag==0) return 1;

flag=0;
for(i=0;i<n;i++)
{
if(no[i][b]>no[a][b]) flag=1;
}
if(flag==0) return 1;

else return 0;

}
