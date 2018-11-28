#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <stack>
#include <bitset>
using namespace std;
bool isPrime(unsigned long long int sum)
{
	unsigned long long int i; 
	int flag=0;
  	for(i=2;i<=sqrt(sum);++i)
  	{
      	if(sum%i==0)
      	{
        	flag=1;
          	break;
      	}
 	}
  	if (flag==0)
      	return 1;
  	else
     	return 0;
}

int getDiv(unsigned long long int sum)
{
	for(unsigned long long int i=2;i<sum;i++)
	{
		if(sum%i==0&&i!=2)
		{
			return i;
		}
	}
	return 0;
}

bool allcombi(bitset<16> combi)
{
	vector<int> vec;
	for(long long int i=2;i<=10;i++)
	{
		unsigned long long int sum=0;
		unsigned long long int k=0;
		for(unsigned long long int j=1;j<=pow(i,15);j=j*i)
		{
			sum=sum+combi[k]*j;
			k++;
		}
		if(isPrime(sum))
		{
			return 0;
		}
		else
		{			
			vec.push_back(getDiv(sum));
		}
	}
	cout<<combi<<" ";
	for(vector<int>::iterator it=vec.begin();it!=vec.end();++it)
	{
		cout<<*it<<" ";
	}
	cout<<"\n";
	vec.clear();
	return 1;
}

int main()
{
	int T;
	cin>>T;
	int N, M;
	cin>>N>>M;
	bitset<16> combi;
	unsigned long long int i=0;
	cout<<"Case #1:"<<"\n";
	while(i<=pow(2,16)&&M>0)
	{
		combi=bitset<16>(i);		
		if(combi[0]==1&&combi[15]==1)
		{				
			if(allcombi(combi))
			{
				M--;
			}
		}
		i++;
	}		
	return 0;
}
