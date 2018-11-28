#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
    ifstream fin;
    fin.open("input.txt");
    ofstream fout;
    fout.open("output.txt");
int cases;
//scanf("%d",&t);
fin>>cases;
int temp=1;
while(temp<=cases)
{
int n,m;
//scanf("%d%d",&n,&m);
fin>>n;
fin>>m;
int arr[n][m];
int set[n][m];
//for(int i=0;i<n;i++)
//r[i]=-1;satr[i]=-1;
//for(int i=0;i<m;i++)
//c[i]=-1;satc[i]=-1;
bool f=true;
int max=0;
int posi=-1;
int posj=-1;
	for(int i=0;i<n;i++)
	for(int j=0;j<m;j++)
	{ //scanf("%d",&ar[i][j]);
	  fin>>arr[i][j];
	  if(max<arr[i][j])
	  {max=arr[i][j];
	   posi=i;
	   posj=j;
	  }
	}
	if(max==1)
	{ fout<<"Case #"<<temp<<": YES"<<endl;
	  
	}
	else
	{
	
	//fout<<"pos "<<posi<<" "<<posj<<endl;
	for(int i=0;i<n;i++)
	for(int j=0;j<m;j++)
	set[i][j]=max;
	/*for(int i=0;i<n;i++)
	for(int j=0;j<m;j++)
	  if(ar[i][j]==max)
		{	
		 r[i]=1;
		 c[j]=1;
		}*/
	for(int i=0;i<n;i++)
	{  if(i !=posi)
	  for(int j=0;j<m;j++)
	   { set[i][j]=min(arr[i][posj],set[i][j] );
	   }	
	}
	for(int j=0;j<m;j++)
	{ if(j!=posj)
	   {
	     for(int i=0;i<n;i++)
	     {
	      set[i][j]=min(arr[posi][j],set[i][j]);
	     }
	   }
	}
	for(int i=0;i<n;i++)
	{for(int j=0;j<m;j++)
	 { if(set[i][j]!=arr[i][j])
	   { f=false;
	     break;
	   }
	 }
	 if(f==false)
	  break;
	}
	if(f==true)
	 fout<<"Case #"<<temp<<": YES"<<endl;
	 else
	 fout<<"Case #"<<temp<<": NO"<<endl;
	 

	}
temp++;
}
fout.close();
}
