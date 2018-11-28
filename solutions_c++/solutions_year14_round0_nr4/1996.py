// CodeJam 2014: sudip1401
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<double> n,k,ntemp,ktemp;

double N()
{
	double ret = ntemp[ntemp.size()-1];
	ntemp.pop_back();
	return ret;
}

double K(double valN)
{
	int f = 0;
	int i = 0;
	for(i=0;i<ktemp.size();i++)
	{
		if(ktemp[i] > valN)
		{
			f = 1;
			break;
		}
	}
	
	if(f == 0)
	{
		double ret = ktemp[0];
		ktemp.erase(ktemp.begin());
		return ret;
	}
	else
	{
		double ret = ktemp[i];
		ktemp.erase(ktemp.begin() + i);
		return ret;
	}
}

int main() {
	int tc;
	cin>>tc;
	for(int t=1;t<=tc;t++)
	{
		int nx;
		cin>>nx;
		for(int i=0;i<nx;i++)
		{
			double x;
			cin>>x;
			n.push_back(x);
			ntemp.push_back(x);
		}
		for(int i=0;i<nx;i++)
		{
			double x;
			cin>>x;
			k.push_back(x);
			ktemp.push_back(x);
		}
		
		sort(n.begin(), n.end());
		sort(k.begin(), k.end());
		sort(ntemp.begin(), ntemp.end());
		sort(ktemp.begin(), ktemp.end());
		
		int sn1=0, sk1=0, sn2=0, sk2=0;
		
		for(int i=0;i<nx;i++)
		{
			double valN = N();
			double valK = K(valN);
			if(valN > valK) sn1++;
			else sk1++;
		}
		
		ktemp.clear();
		ntemp.clear();
		for(int i=0;i<nx;i++) 
		{
			ntemp.push_back(n[i]);
			ktemp.push_back(k[i]);
		}
		
		
		sort(ntemp.begin(), ntemp.end());
		sort(ktemp.begin(), ktemp.end());
		
		for(int i=0;i<nx;i++)
		{
			double valN = ntemp[0];
			double valK;
			if(valN > ktemp[ktemp.size()-1])
			{
				valK = ktemp[0];
				ntemp.erase(ntemp.begin());
				ktemp.erase(ktemp.begin());
				sn2++;
			}
			else if(valN > ktemp[0])
			{
				valN = ktemp[ktemp.size()-1]+1;
				valK = ktemp[0];
				ktemp.erase(ktemp.begin());
				ntemp.erase(ntemp.begin());
				sn2++;
			}
			else
			{
				valK = ktemp[ktemp.size()-1];
				ntemp.erase(ntemp.begin());
				ktemp.pop_back();
				sk2++;
			}
		}
		
		cout<<"Case #"<<t<<": "<<sn2<<" "<<sn1<<endl;
		
		
		n.clear(); ntemp.clear();
		k.clear(); ktemp.clear();
	}
	return 0;
}
