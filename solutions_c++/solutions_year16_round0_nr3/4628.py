#include<cstdio>
#include<iostream>
#include<cmath>
#include<vector>

#define TOT 16
using namespace std;


int number[TOT];

long long smallestFactor(long long num)
{
	long long i;
	for(i=2;i*i<=num;i++)
	{
		if(num%i == 0)
			return i;
		
	}
	return -1;
}

long long numberInBase(int base)
{
	int i;
	long long ans = 0;
	for(i=0;i<TOT;i++)
		ans = ans*base + number[i];
	return ans;

}


int main()
{
	int t;
	scanf("%d", &t);
	
	//cout<<smallestFactor(1000000000000001)<<endl;
	
		ios_base::sync_with_stdio(false);
		
		int n,j;
		cin>>n>>j;
		
		cout<<"Case #1:"<<endl;
		
		
		int i;
		number[0] = 1;
		number [TOT-1] = 1;
		
		for(i=1;i<TOT-1;i++)
			number[i] = 0;			
		
		int h = 0;
		int lim = pow(2, TOT-2);
		int count = 0;
		while(h<lim)
		{
			int r;
			bool valid = true;
			vector<long long> anss;
			
			for(r=2;r<=10;r++)
			{
				long long val = numberInBase(r);
				long long fac = smallestFactor(val);
				//cout<<val<<" "<<fac<<endl;
				if(fac == -1)
				{
					
					valid = false;
					break;
				}
				anss.push_back(fac);
			}
			if(valid)
			{
				count++;
				for(r=0;r<TOT;r++)
					cout<<number[r];
				
				cout<<" ";
				
				for(r=0;r<=8;r++)
				{
					if(r!=8)
						cout<<anss[r]<<" ";
					else
						cout<<anss[r]<<endl;
					
				}
				
			}
			if(count>=j)
			{
				break;
			}	
			
			for(r=TOT-2;r>=1;r--)
			{
				if(number[r] == 1)
				{
					number[r] = 0;
					
				}
				else
				{
					number[r] = 1;
					break;
				}
				
			}
			
			anss.clear();
			h++;
			
		}
		
		

	
	
	
	
}