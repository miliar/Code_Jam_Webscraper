#include <unordered_map>
#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>
#include <functional>
#include <map>
#include <cmath>
#include <fstream>
using namespace std;
typedef long long ll;

const ll MOD = 1000000007;

int main()
{
	ofstream outfile;
	outfile.open("CS.out");
	
	ifstream infile;
	//infile.open("A-large-attempt0.in");
	infile.open("A-large.in");
	int t;
	infile>>t;
	for(int k=1;k<=t;k++)
	{
		int a[10]={0,0,0,0,0,0,0,0,0,0};
		ll n,temp,j;
		int count=0,i;
		
		infile>>n;
		
		if(n==0)
		{
		outfile<<"Case #"<<k<<": "<<"INSOMNIA"<<'\n';
		continue;
		}
		
		
		for(i=1;;i++)
		{
			temp=n*i;
			for(j=temp;j!=0;j=j/10)
			{
				if(a[j%10]==0)
				{
					a[j%10]=1;
					count++;
					if(count==10)
					break;
				}
			}
			if(count==10)
			break;
		}
		
		outfile<<"Case #"<<k<<": "<<temp<<'\n';
			
	}
}
