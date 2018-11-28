#include <fstream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
int compare (const void * a, const void * b)
{
	if(*(double*)b < *(double*)a)
		return 1;
	else
		return -1;
}
int play_war(double* N,double* K,int n){
	int count=0;
	int m=n;
	for(int i=0;i<n;i++)
	{
		if(N[i]>K[m-1])
		{
			count++;
		}
		for(int j=count;j<m;j++)
			if(N[i]<K[j])
			{
				if(j==m-1)
					m--;
				K[j]=-1;
				j=n+1;
			}

	}
	return count;
}
int play_deceitful(double* N,double* K,int n){
	int count=0;
	for(int i=0;i<n;i++)
	{
		
		if(N[i]>K[count])
		{
			count++;
		}
	}
	return count;
}
int main(){
	ifstream input;
	ofstream output;
	output.open("output.txt");
	input.open("input.txt");
	int T;
	input>>T;
	for(int i=0;i<T;i++)
	{
		int n;
		input>>n;
		double* N,*K,*K1;
		N=new double[n];
		K=new double[n];
		K1=new double[n];
		for(int i=0;i<n;i++)
			input>>N[i];
		for(int i=0;i<n;i++)
			input>>K[i];
		qsort (N, n, sizeof(double), compare);
		qsort(K,n,sizeof(double),compare);
		for(int i=0;i<n;i++)
		{
			K1[i]=K[i];
		}
		int war= play_war(N,K,n);
		int d_war=play_deceitful(N,K1,n);
		output<<"Case #"<<i+1<<": "<<d_war<<" "<<war<<endl;
		delete[] N;
		delete[] K1;
		delete[] K;

	}
	input.close();
	output.close();
	return 0;
}