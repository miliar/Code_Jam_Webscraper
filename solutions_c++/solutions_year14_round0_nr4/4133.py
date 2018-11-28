#include<iostream>
#include<algorithm>
using namespace std;

int comp(const void* a, const void* b)
{
	const double *A=(double*)a , *B=(double*)b;
	if (*A < *B)
		return -1;
	else
		return 1;
}

double getMax(double mat[] , int size)
{
	double max=mat[0];
	for (int i=0 ; i<size ; i++)
	{
		if (mat[i]>max && mat[i]>0)
			max=mat[i];
	}
	return max;
}

int getMaxC(double mat[] , int size)
{
	double max=mat[0];
	int C=0;
	for (int i=0 ; i<size ; i++)
	{
		if (mat[i]>max && mat[i]>0)
		{
			max=mat[i];
			C=i;
		}
	}
	return C;
}

int solveWar(double mat1[] , double mat2[] , int size)
{
	int score=0;
		
	for (int i=size-1 ; i>=0 ; i--)
	{
		for (int j=0 ; j<size ; j++)
		{
			if (mat2[j]>0 && mat2[j]>mat1[i])
			{
				mat2[j]=0;
				score++;
				break;
			}
		}
	}
	return (size-score);
}

int solveDWar(double mat1[] , double mat2[] , int size)
{
	int score=0;

	for (int i=0 ; i<size ; i++)
	{
		for (int j=0 ; j<size ; j++)
		{
			if (mat1[j]>0 && mat1[j]>mat2[i])
			{
				mat1[j]=0;
				score++;
				break;
			}
		}
	}
	return score;
}

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("output2.txt","w",stdout);

	int ProbNum;
	cin>>ProbNum;

	for (int i=0 ; i<ProbNum ; i++)
	{
		int BlockNum;
		cin>>BlockNum;

		double *matNaomi= new double[BlockNum];
		double *matKen = new double[BlockNum];

		double *matNaomi2=  new double[BlockNum];
		double *matKen2=  new double[BlockNum];

		for (int j=0 ; j<BlockNum ; j++)
		{
			cin>>matNaomi[j];
			matNaomi2[j]=matNaomi[j];
		}
		for (int j=0 ; j<BlockNum ; j++)
		{
			cin>>matKen[j];
			matKen2[j]=matKen[j];
		}
		qsort(matNaomi,BlockNum,sizeof(double),comp);
		qsort(matKen,BlockNum,sizeof(double),comp);
		qsort(matNaomi2,BlockNum,sizeof(double),comp);
		qsort(matKen2,BlockNum,sizeof(double),comp);
				
		cout<<"Case #"<<i+1<<": "<<solveDWar(matNaomi,matKen,BlockNum)<<" "<<solveWar(matNaomi2,matKen2,BlockNum)<<endl;
	}
}