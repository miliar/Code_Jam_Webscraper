#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	double nao[10000], ken[10000], nao1[10000], ken1[10000];
	long long m;
	cin>>m;
	for(long long t=1; t<=m;t++)
	{
		long long n; 
		cin>>n;
		for(long long i=0;i<n;i++)
			cin>>nao[i];
		for(long long i=0;i<n;i++)
			cin>>ken[i];
		sort(nao, nao+n);
		sort(ken, ken+n);
		copy(nao,nao+n,nao1);
		copy(ken,ken+n,ken1);
		
		
		long long war=0, dec_war=0;
		for(long long i=0;i<n;i++)
		{
			long long j;
			for(j=0;j<n;j++)
			{
				if(ken[j]>nao[i])
				{
					break;
				}
			}
			if(j==n)
			{
				j=0;
				while(ken[j++]<0);
			}
			if(ken[j]<nao[i])
				war++;
			ken[j]=-1;
			nao[i]=-1;
		}
		
		long long j=0, j_opp= n-1, index;
		for(long long i=0;i<n;i++)
		{
			if(ken1[j] > nao1[i])
			{
				index = j_opp;
				j_opp--;
			}
			else
			{
				index = j;
				j++;
				dec_war++;
			}
			ken1[index]=-1;
			nao1[i]=-1;
		}
		cout<<"Case #"<<t<<": "<<dec_war<<" "<<war<<endl;
	}
	return 0;
}
