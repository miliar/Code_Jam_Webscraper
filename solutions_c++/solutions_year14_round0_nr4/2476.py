#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main(){
	int t;
	double cn,ck;
	int p,wp;
	int n; //number of stones
	double K[1000]; //Ken stones
	double N[1000]; //Naomi
	bool U[1000];
	int best,s;
	int kmax,kmin;

	cin>>t;
	for(int cs=0;cs<t;cs++)
	{
		cin>>n;
		for(int i=0;i<n;i++)
			cin>>N[i];
		for(int i=0;i<n;i++)
			cin>>K[i];
		sort(N,N+n);
		sort(K,K+n);
		////////////////dec war////////////////
		wp=0;
		p=0;
		kmin=0;
		for(int i=0;i<n;i++)
		{
			if(N[i]>K[kmin])
			{
				wp++;
				kmin++;
			}
		}
		////////////////////
		/////////war//////////
		for(int i=0;i<n;i++)
			U[i]=1;
		for(int i=0;i<n;i++)
		{
			cn=N[i];
			best=1000;
			for(int j=0;j<n;j++)
				if(K[j]>cn && U[j] && best==1000)
					best=j;
				else if(K[j]>cn && U[j] && (K[j]-N[i])<(K[best]-N[i]))
					best=j;
			s=0;
			if(best==1000)
			{
				while(!U[s])
				{
					s++;
				}
				best=s;
			}
			ck=K[best];
			U[best]=0;
			if(ck<cn) p++;
		}
		/////////////////////////////////////
		printf("Case #%d: %d %d\n",cs+1,wp,p);
	}
	return 0;
};