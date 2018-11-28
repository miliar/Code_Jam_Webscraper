#include<iostream>
#include<iomanip>
#include<algorithm>
#include<vector>
long war(std::vector<double> n,std::vector<double> k)
{
	if(n.size()==1)
		return n[0]>k[0];
	for(int j=0;j<n.size();++j)
	{
		if(k[j]>n[0])
		{
			n.erase(n.begin()+0);
			k.erase(k.begin()+j);
			return war(n,k);
		}
	}
	n.erase(n.begin()+0);
	k.erase(k.begin()+0);
	return 1+war(n,k);
	
}
long dwar(std::vector<double>& n,std::vector<double>& k)
{
	if(n.size()==1)
		return n[0]>k[0];
	
	bool flag=true;
	for(int i=0;i<n.size();++i)
		if(n[i]<k[i])
			flag=false;
	if(flag)
		return n.size();
	double x=n[0];
	double y=k[k.size()-1];
	n.erase(n.begin());
	k.erase(k.end()-1);
	
	return (x>y)+dwar(n,k);
	
}
int main()
{
	long T;
	std::cin>>T;
	long  n=T;
	while(T--)
	{
		long x;
		std::cin>>x;
		std::vector<double> naomi(x),ken(x);
		for(long i=0;i<x;++i)
			std::cin>>naomi[i];
		for(long i=0;i<x;++i)
			std::cin>>ken[i];
		
		std::sort(naomi.begin(),naomi.end());
		std::sort(ken.begin(),ken.end());
		
		std::cout<<"Case #"<<n-T<<": "<<dwar(naomi,ken)
		<<' '<<war(naomi,ken)<<std::endl;
		
	}
}