#include<iostream>
using namespace std;

int main()
{
	int T,N,M,ar[100][100],possible;
	cin>>T;
	for(int I=1;I<=T;I++)
	{
		cin>>N>>M;
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<M;j++)
			{
				cin>>ar[i][j];
			}
		}
		
		
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<M;j++)
			{
								possible=1;
								for(int k=0;k<N;k++)
								{
												if(ar[i][j]<ar[k][j]){possible=0;break;}
								}
								if(possible)continue;
								possible=1;
								for(int k=0;k<M;k++)
								{
												if(ar[i][j]<ar[i][k]){possible=0;break;}
								}
								if(!possible) break;
			}if(!possible)break;
		}
		
		if(possible) cout<<"Case #"<<I<<": YES"<<endl;
		else  cout<<"Case #"<<I<<": NO"<<endl;
		
		
	}


	return 0;
}
