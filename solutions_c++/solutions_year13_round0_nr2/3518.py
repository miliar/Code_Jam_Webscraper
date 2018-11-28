#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
using namespace std;

vector<int> matrix;
bool myfunction(int i,int j) 
{
	return (matrix[i]<matrix[j]); 
}

int main(int argc, char * argv[])
{
	ifstream ifs;
	if(argc == 2) ifs.open(argv[1]);

	int T; 
	if(argc == 1) cin >> T;
	else if(argc == 2) ifs >> T;

	for(int t = 0; t < T; t++)
	{
		int N, M;
		if(argc == 1) cin >> N >> M;
		if(argc == 2) ifs >> N >> M;
		matrix.clear();
		matrix.resize(N*M);
		for(int n = 0; n < N; n++)
		{
			for(int m = 0; m < M; m++) 
			{
				if(argc == 1) cin >> matrix[n*M + m];
				else if(argc == 2) ifs >> matrix[n*M + m];
			}
		}
		vector<int> order(M*N);
		for(int i = 0; i < M*N; i++) order[i] = i;
		sort(order.begin(), order.end(), myfunction);
		for(int i = 0; i < M*N; i++)
		{
			int j = order[i];
			int n = j/M;
			int m = j%M;
			bool bflag1 = true;
			bool bflag2 = true;
			for(int k = 0; k < M; k++) 
			{
				if(matrix[n*M + k] > matrix[j]) 
				{
					bflag1 = false;
					break;
				}
			}
			if(!bflag1)
			{
				for(int k = 0; k < N; k++)
				{
					if(matrix[k*M + m] > matrix[j])
					{
						bflag2 = false;
						break;
					}
				}
				if(!bflag2) 
				{
					cout<<"Case #"<<t+1<<": NO"<<endl;
					goto out;
				}
			}
		}
		cout<<"Case #"<<t+1<<": YES"<<endl;
out:
		T=T;
	}

	if(argc == 2) ifs.close();
}
