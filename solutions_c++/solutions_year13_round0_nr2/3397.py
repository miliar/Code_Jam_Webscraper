#include<iostream>
#include<map>
#include<vector>
#include<string>
using namespace std;

void solve(int t, int N, int M, int** lawn)
{
	FILE * fpOut = fopen("/Users/adarshkumarsharma/cpp/Code/CodeJam/LawnMower/src/B-large.out","a+");
	bool possible = true;

	for(int n=0;n<N && possible==true;n++)
	{
		for(int m=0;m<M && possible==true;m++)
		{
			bool h = true;
			bool v = true;

			for(int j=0;j<M;j++)
			{
				if(lawn[n][j]>lawn[n][m])
				{
					h = false;
					break;
				}
			}
			for(int i=0;i<N;i++)
			{
				if(lawn[i][m]>lawn[n][m])
				{
					v = false;
					break;
				}
			}

			if(h==false && v==false)
				possible = false;
		}
	}
	if(possible==true)
		fprintf(fpOut,"Case #%d: YES\n", t);
	else
		fprintf(fpOut,"Case #%d: NO\n", t);

	fclose(fpOut);
}

int main()
{
	FILE * fpIn = fopen("/Users/adarshkumarsharma/cpp/Code/CodeJam/LawnMower/src/B-large.in","r");
	int T;
	fscanf(fpIn,"%d",&T);

	for(int t=0;t<T;t++)
	{
		int N,M;
		fscanf(fpIn,"%d %d", &N, &M);

		int** lawn = new int*[N];

		for(int i=0;i<N;i++)
		{
			lawn[i] = new int[M];
			memset(lawn[i],0,M*sizeof(int));
			for(int j=0;j<M;j++)
				fscanf(fpIn,"%d",&lawn[i][j]);
		}

		solve(t+1, N, M, lawn);

		for(int i=0;i<N;i++)
			delete[] lawn[i];
		delete[] lawn;
	}

	fclose(fpIn);

}
