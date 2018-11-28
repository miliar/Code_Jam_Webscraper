#include<iostream>
#include<fstream>
using namespace std;
int count[2501];
int main()
{
	fstream fin,fout;
	fin.open("opo6.in",fstream::in);
	fout.open("out6.txt",fstream::out);
	int T,N,i,j,ai,temp;
	int *a;
	bool *b;
	ai=1;
	fin>>T;
	while(T--)
	{
		for(i=0;i<2501;i++)count[i]=0;
		fin>>N;
		a=new int[N];
		for(j=0;j<2*N-1;j++)
		{
			for(i=0;i<N;i++)
			{
				fin>>temp;
				count[temp]++;
			}
			
		}
		j=0;
		for(i=0;i<2501;i++)
		{
			if(count[i]%2!=0)
			{
				a[j]=i;
				j++;
			}
		}
		fout<<"Case #"<<ai<<":";
		for(i=0;i<N;i++)fout<<" "<<a[i];
		fout<<endl;
		ai++;
	}

	
	
	fin.close();
	fout.close();
	return 0;
}
