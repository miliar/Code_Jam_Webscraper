#include<fstream.h>
#include<iomanip.h>
void main()
{
	ifstream fin;
	ofstream fout;
	fout.open("out.txt") ;
	long T,k,i,j,f,n,m,c,l;


	fin.open ("in.txt");
	fin>>T;

	for( k=1; k<=T; k++)
	{
		fin>>m;
		fin>>n;
		fin>>c;
		f=0;
		for(i=0;i<m;i++)
		{
			for(j=0;j<n;j++)
			{
				for(l=0;l<c;l++)
				{
					if(l==(i&j))
					{f++;}
				}
			}
		}
		fout<<"case #"<<k<<": "<<f<<endl;
	}
  fin.close();
  fout.close();
}