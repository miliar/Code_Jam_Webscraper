#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<set>
#include<fstream>
#include<queue>
#include<fstream>
#include<map>

using namespace std;

map<long long,int> FS;



bool isPalin(long long x) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        long long divisor=1;
        long long temp=x;
        
        while(temp/(divisor*10)!=0)
        {
            divisor*=10;
        
        }
        while(divisor!=0)
        {
            long long last=x%10;
            long long first=x/divisor;
            if(first!=last)
                return false;
            x/=10;
            divisor/=10;
			if(x==0)
				return true;
            x%=divisor;
            divisor/=10;
        
        }
        
        return true;
        
    }

bool checkSqrt(long long n)
{
	long long s1=sqrt((long double)n);
	long double s2=sqrt((long double)n);
	if((long double)s1==(long double)s2)
	{
		if(isPalin(s1))
			return true;
	}
	return false;
}




int main()
{
	ifstream cin("C-small-attempt0.in");
	ofstream cout("C-small.out");
	//ifstream cin("C-large.in");
	//ofstream cout("C-large.out");

	int test;
	cin>>test;
	for(int k=0;k<test;k++)
	{

		long long start,end;
		cin>>start>>end;
		long long ans=0;

	
		for(long long i=start;i<=end;i++)
		{
			if(FS[i]==0)
			{
				if(checkSqrt(i) && isPalin(i))
				{
					FS[i]=2;
					ans++;
				}
				else FS[i]=1;
			}
			else if(FS[i]==2)
				ans++;

			
		}


		cout<<"Case #"<<(k+1)<<": "<<ans<<endl;
		
	}


	

	system("pause");
	return 0;
}