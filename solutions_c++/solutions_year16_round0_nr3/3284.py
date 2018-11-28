#include<iostream>
#include<vector>
#define LIMIT 200000010
using namespace std;
bool *sieve = new bool [LIMIT];
long long int isPrime(long long int n) // returns a non trivial divisor or just 1 itself.
{
	long long int it;
	for(it=2;it<LIMIT;it++)
	{
		if(sieve[it] && (n%it==0) && it<n)
			return it;
		else if(it*it > n)
			return 1;
	}
	return 1;
}
void calc_sieve()
{
	long long int it,jt;
	for(it=0;it<LIMIT;it++)
		sieve[it] = true;
	for(it=2;it<LIMIT;it++)
	{
		if(sieve[it])
		{
			for(jt=2*it;jt<LIMIT;jt=jt+it)
				sieve[jt]=false;
		}
	}
	
}

int main()
{
	cout<<"Case #1:\n";
	int n=16;
	int j=50;
	int *dig = new int [n];
	calc_sieve();
	for(int i=0;i<n;i++)
		dig[i]=0;
	dig[0]=1;
	dig[n-1]=1;
	for(long long it=0;((it<(1<<n-2)) && j>0);it++)	
	{
		//cout<<it<<"\n";
		long long curr = it;
		for(int jt=1;jt<=n-2;jt++)
		{
			dig[jt]=curr%2;
			curr=curr/2;
		}
		// Jam Coin test begins!
		bool flag=true;
		vector<long long int> list;
		for(int exp=2;exp<=10;exp++)
		{
			long long int num=0;
			for(int i=0;i<n;i++)
				num = num*exp + dig[i];
			long long int ans = isPrime(num);
			if(ans == 1)
			{
				flag=false;
				break;
			}
			else
				list.push_back(ans);
		}
		if(flag)
		{
			//continue;
			for(int i=0;i<n;i++)
				cout<<dig[i];
			cout<<" ";
			for(int i=0;i<(int)list.size();++i)
				cout<<list[i]<<" ";
			cout<<"\n";
			j--;
		}
	}
	return 0;
}
