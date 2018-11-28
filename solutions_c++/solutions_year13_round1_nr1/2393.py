#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	int Z;
	cin >> Z;
	
	for(int z=1; z<=Z; z++)
	{
		long long r;
		cin >> r;
		long long t;
		cin >> t;
		
		long long x=0;
		long long res=0;
		
		/*while(x<=t)
		{
			res++;
			if(x+2*r+1<x)
				x=t+1;
			else
				x+=2*r+1;
			r+=2;
			cout << x << endl;
		}*/
		
		
		long long p=0;
		long long q=min(t,(long long)8*100000000);
		
		while(q!=p)
		{
			long long s=(p+q+1)/2;
			//cout << p << " " << q << " " << s << endl;
			//cout << (long long)(2*r+2*s-1)*s << endl;
			
			int ile=0;
			long long x=(2*r+2*s-1);
			while(x)
			{
				ile++;
				x/=10;
			}
			x=s;
			while(x)
			{
				ile++;
				x/=10;
			}
			ile--;
			
			if(ile>19 || (long long)2*r>=t || (long long)2*s>=t || (long long)(2*s+2*r)<0)
				q=s-1;
			else if((long long)(2*r+2*s-1)*s<=t && (long long)(2*r+2*s-1)*s>0)
				p=s;
			else
				q=s-1;
				
		}
		
		
		cout << "Case #" << z << ": " << p << endl;
	}
}
