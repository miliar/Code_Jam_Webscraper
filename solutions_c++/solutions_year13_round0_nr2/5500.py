#include<iostream>
#include<string>
#include<vector>
using namespace std;
int main()
{
	int T;cin >> T;
	for(int c=1; c<=T; c++)
	{
		int N,M; cin >> N >> M;
		vector<int> R;//vector for storing the max of the rows
		vector<int> C;//vector for storing the max of the columns
		int L[111][111];
		int D[111][111];
		//taking input and  getting max for each row
		for(int i=0;i<N;i++)
		{
			int max=0;int temp;
			for(int j=0; j<M;j++)
			{
				D[i][j]=111;
				cin >> temp;
				if(temp > max)
					max=temp;
				L[i][j]=temp;
			}
			R.push_back(max);
		}
		//calculating max of each of the column
		for(int i=0;i<M;i++)
		{
			int max =0;
			for(int j=0;j<N;j++)
			{
				if(L[j][i] > max)
					max = L[j][i];
			}
			C.push_back(max);
		}
		//changing the columns
		for(int i=0; i<M;i++)
		{
			for(int j=0; j<N;j++)
			{
				if(D[j][i]>C[i])
					D[j][i]=C[i];
			}
		}
		//changing the row
		for(int i=0;i<N;i++)
		{
			for(int j=0; j<M;j++)
			{
				if(D[i][j]>R[i])
					D[i][j]=R[i];
			}
		}
		//checking if created correct matrix or not
		bool Yes = true;
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<M;j++)
			{
				if(L[i][j] != D[i][j]){
					Yes=false;break;}
			}
		}
		if(Yes==false)
			cout<<"Case #"<<c<<": NO"<<endl;
		else
			cout<<"Case #"<<c<<": YES"<<endl;
	}
	return 0;
}