#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

bool f(int** data,int N,int M,int x,int y);

int main()
{
	fstream ifs("Google.in");
	ofstream ofs("Google.out");
	int T,N,M;
	ifs>>T;
	for(int i=1;i<=T;i++)
	{
		bool a=true;
		ifs>>N>>M;
		int** data=new int*[N];
		for(int j=0;j<N;j++)
		{
			data[j]=new int[M];
		}
		for(int j=0;j<N;j++)
		{
			for(int k=0;k<M;k++)
			{
				ifs>>data[j][k];
			}
		}
		for(int i=0;i<N;i++)
		{
			for(int k=0;k<M;k++)
			{
				a=f(data,N,M,i,k);
				if(a==false)
				{
					goto M1;
				}
			}
		}
	M1:	if(a==true)
		{
			ofs<<"Case #"<<i<<": "<<"YES"<<endl;
		}
		else
		{
			ofs<<"Case #"<<i<<": "<<"NO"<<endl;
		}
	}
	system("pause");
}

bool f(int** data,int N,int M,int x,int y)
{
	bool horizontal=true,vertical=true;
	for(int i=0;i<N;i++)
	{
		if(data[i][y]>data[x][y]) vertical=false; 
	}
	for(int i=0;i<M;i++)
	{
		if(data[x][i]>data[x][y]) horizontal=false; 
	}
	if(horizontal==false && vertical==false) return false;
	return true;
}

