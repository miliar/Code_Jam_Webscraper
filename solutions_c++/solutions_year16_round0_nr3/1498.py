#include<iostream>
#include<vector>
#include<cmath>
#include<bitset>
using namespace std;
vector<long long>sievef;
vector<bool>sieve(100000001,1);
long long chkprime(long long num)
{
	if(num<=1)
	return 0;
	long long num1=sqrt(num);
	for(long long i=0;sievef[i]<=num1;i++)
		{
			if(num%sievef[i]==0)
			return sievef[i];
		}
		return 1;
}
void fill()
{
	for(long long i=2;i<=100000001;i++)
	{
		if(sieve[i])
		{
			sievef.push_back(i);
			for(long long j=2*i;j<100000001;j=j+i)
				{
					sieve[j]=0;
				}
		}
	}
}
int main()
{
	fill();
	int t;
	cin>>t;
	int Case=1;
	vector<long long>interp;
        vector<long long>divsor;
	cout<<"Case #"<<Case<<": "<<endl;
				Case++;
	while(t--)
	{
		int n,j;
		cin>>n>>j;
		long long limit=pow(2,n-2);
		for(long long i=0;(i<limit)and(j>0);i++)
		{
			bitset<14>jugu(i);
			bitset<16>jug;
			jug.set(0,1);
			jug.set(n-1,1);
			for(int k=1;k<n-1;k++)
				jug.set(k,jugu[k-1]);
			string bs = jug.to_string();
			
			interp.clear();
			divsor.clear();
			for(int k=2;k<=10;k++)
			{
				interp.push_back(stoull(bs,nullptr,k));
				//cout<<stoull(bs,nullptr,k)<<endl;
			}
			bool f=1;
			long long tempor;
			for(int k=0;k<interp.size();k++)
				{
					tempor=chkprime(interp[k]);
					if(tempor!=1)
					{
						divsor.push_back(tempor);
					}
					else
					{
						f=0;
						break;
					}
				}
			if(f)
			{
					cout<<bs<<" ";
				for(int k=0;k<divsor.size();k++)
					{
						if(k!=divsor.size()-1)
						cout<<divsor[k]<<" ";
						else
						cout<<divsor[k]<<endl;
					}
			 	j--;
			}
				
		}
		
	}
	return 0;
}

