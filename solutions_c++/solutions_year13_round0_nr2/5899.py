#include <iostream>
using namespace std;
int findMax(int a[100][100],int Sz,int row_col,int r_or_c)
{
	int irmax=-1,icmax=-1;
	for(int i=0;i<Sz;++i)
	{
		
		if(r_or_c)
		{
		if(irmax<a[row_col][i])
		{
				irmax = a[row_col][i];
		}
	
		}
else
{

	if(icmax<a[i][row_col])
		{
				icmax = a[i][row_col];
		}

}
	
	}
	if(r_or_c)
	{
			return irmax;
	}
	return icmax;
}


int main()
{

	int caseNum,a[100][100],N,M,iTh=1;
	cin>>caseNum;
	while(caseNum>0)
	{
		cin>>N>>M;
		for(int i=0;i<N;++i)
		{
			for(int j=0;j<M;j++)
			{
				cin>>a[i][j];
			}
		}

///		char rmax[100],cmax[100];
//		memset(rmax,-1,sizeof(rmax));
//		memset(cmax,-1,sizeof(cmax));
		int rmax=0,cmax=0;
		int fail = 0;
		for(int i=0;i<N;++i)
		{
			for(int j=0;j<M;j++)
			{
			//	if(rmax[i]<0 || cmax[j]<0 )
				{
					rmax = findMax(a,M,i,1);
					cmax = findMax(a,N,j,0);
				}
				if(rmax>a[i][j]&&cmax>a[i][j])
				{
						fail = 1;
						goto RESULT;
				}
			}
		}
		
RESULT:		
		if(fail)
		{
			cout<<"Case #"<<iTh<<": NO"<<endl;
		}
		else
		{
			cout<<"Case #"<<iTh<<": YES"<<endl;
		}	

		iTh++;
		caseNum--;
	}
	return 0;
}

