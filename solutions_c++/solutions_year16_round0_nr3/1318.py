#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <iostream>

using namespace std;

#define ll long long

int primes[10000];
int prNum=0;
int isPr[10000];
int list[11];

int main()
{
	for(int i=2; i<10000; ++i)
		if(!isPr[i]){
			for(int j=i+i; j*j<10000; j+=i)
				isPr[i]=1;
			primes[prNum++]=i;
		}
	int kol=0, ok, p, ost;
	for(ll cfg=0; cfg<1<<29 && kol<500; ++cfg)
	{
		ll n=(((ll)1)<<31)|(cfg<<1);
		n|=1;
		ok=1;
		for(int j=2; j<=10 && ok; ++j)
		{
			list[j]=0;
			for(int l=0; l<prNum; ++l)
			{
				p=1, ost=1;
				for(int i=1; i<32; ++i)
				{
					p=(p*j)%primes[l];
					if((n>>i)&1)
						ost=(ost+p)%primes[l];
				}
				if(ost==0)
					list[j]=primes[l];
			}
			if(list[j]==0)
				ok=0;
		}
		if(ok){
			for(int i=31; i>=0; --i)
				if((n>>i)&1)
					cout << "1";
				else cout << "0";
			for(int i=2; i<=10; ++i)
				cout << " "<< list[i];
			cout << endl;
			++kol;
		}
	}
}