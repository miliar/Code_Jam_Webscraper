#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int cmp( const double &a, const double &b ){
	if( a > b )
		return 1;
	else
		return 0;
}

int main()
{
	ifstream fin("test.in");
	ofstream fout("test.out");
	int t;
	int *result[2];
	fin>>t;
	result[0] = new int[t];
	result[1] = new int[t];
	for (int i=0;i<t;i++)
	{
		int n;
		double *Naomi;
		double *Ken;
		fin>>n;
		Naomi = new double[n];
		Ken = new double[n];
		for(int j=0;j<n;j++)
			fin>>Naomi[j];
		for(int j=0;j<n;j++)
			fin>>Ken[j];
		sort(Naomi,Naomi+n,cmp);
		sort(Ken,Ken+n,cmp);
		//for(int j=0;j<n;j++)
		//	cout<<Naomi[j]<<" ";
		//cout<<endl;
		//for(int j=0;j<n;j++)
		//	cout<<Ken[j]<<" ";
		//cout<<endl;
		int j,k,len;
		result[0][i] = 0;
		result[1][i] = 0;
		for (j=0,k=0,len=n;j<len && k<n;k++)
		{
			if (Ken[j] > Naomi[k])
			{
				result[1][i] ++;
				j++;
			}
			else
				len--;
		}
		result[1][i] = n-result[1][i];
		for (j=n-1,k=n-1; j>=0 && k>=0;j--)
		{
			if (Naomi[j] > Ken[k])
			{
				result[0][i] ++;
				k--;
			}
		}

	}
	for (int i=0;i<t;i++)
	{
		fout<<"Case #"<<i+1<<": "<<result[0][i]<<" "<<result[1][i]<<endl;
	}
	return 0;
}