#include <iostream>
#include <cstdlib>
#include <algorithm>
double m1[100], m2[100], m3[100], m4[100];
bool rsort(double a, double b) {
	return b<a;
}
int war(double m1[], double m2[], int n) {
	double a;
	int aScore(0);
	for (int i=0; i<n; i++)
	{
		a=m1[i]; m1[i]=-1;
		int j(0);
		for (; j<n; j++)
			if (m2[j]>a)
				break;
		if (j==n)
		{
			for (int k=0; k<n; k++)
			{
				if (m2[k]!=-1)
				{
					m2[k]=-1;
					break;
				}
			}
			aScore++;
		}
		else
			m2[j]=-1;
	}
	return aScore;
}
int dwar(double m1[], double m2[], int n) {
	double a, b;
	int aScore(0);
	for (int i=0; i<n; i++)
	{
		b=m2[i]; m2[i]=-1;
		int j(0);
		for (; j<n; j++)
			if (m1[j]>b)
				break;
		if (j==n)
		{
			int k;
			for (k=n-1; k>=0; k--)
				if (m1[k]!=-1)
				{
					m1[k]=-1;
					break;
				}
		}
		else
		{
			aScore++;
			m1[j]=-1;
		}
	}
	return aScore;
}
int main() {
	int nTc, n;
	double x;
	std::cin>>nTc;
	for (int i=0; i<nTc; i++)
	{
		std::cin>>n;
		memset(m1, 0., sizeof(m1));
		memset(m2, 0., sizeof(m2));
		memset(m3, 0., sizeof(m1));
		memset(m4, 0., sizeof(m2));
		for (int j=0; j<n; j++)
		{
			std::cin>>x;
			m1[j]=x; m3[j]=x;
		}
		for (int j=0; j<n; j++)
		{
			std::cin>>x;
			m2[j]=x; m4[j]=x;
		}
		std::sort(m2, m2+n);
		int aScoreWar=war(m1, m2, n);
		std::sort(m3, m3+n, rsort); 
		std::sort(m4, m4+n, rsort);
		int aScoreDWar=dwar(m3, m4, n);
		std::cout<<"Case #"<<i+1<<": "<<aScoreDWar<<' '<<aScoreWar<<'\n';
	}
	return 0;
}