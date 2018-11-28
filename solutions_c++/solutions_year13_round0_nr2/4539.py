#include<iostream>
#include<fstream>
#include<string>

using namespace std;
void main()
{
	int i,j,k,T,N,M,flag,lawn[100][100],hor[100],vert[100];
	char tmp;
	ifstream ifile("B-large.in");
	ofstream ofile("output.txt");
	if (ifile.is_open())
	{
		ifile>>T;
		cout<<T<<endl;
		for(j=0;j<T;j++)
		{
			ifile>>N;
		    ifile>>M;

			flag = 0;
			for(k=0; k<N; k++)
			{
				hor[k]=0;
				for(i=0;i<M;i++)
				{
					ifile>>lawn[k][i];
					if(lawn[k][i]>hor[k])
						hor[k] = lawn[k][i];
				}
			}
			for(i=0; i<M; i++)
			{
				vert[i]=0;
				for(k=0; k<N; k++)
					if(lawn[k][i]>vert[i])
						vert[i] = lawn[k][i];
			}

			flag=0;
			for(k=0; k<N; k++)
			{
				for(i=0;i<M;i++)
				{
					if(!(lawn[k][i] == hor[k] || lawn[k][i] == vert[i]))
						flag = 1;
				}
			}
			cout<<endl;
			//cout<<tmp;
			if(flag == 1)
				ofile<<"Case #"<<j+1<<": NO"<<endl;
			else
				ofile<<"Case #"<<j+1<<": YES"<<endl;
			}
			
			//cout<<endl;
	}
	cin>>tmp;
}