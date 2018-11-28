#include <bits/stdc++.h>
using namespace std;
#define gc() getchar_unlocked()
inline long long int read_int()
{
	char c = gc();
    	while(c<'0' || c>'9')
    	c = gc();
    	long long int ret = 0;
    	while(c>='0' && c<='9')
    	{
    		ret = (ret<<3) + (ret<<1) + c - 48;
    		c = gc();
    	}
    	return ret;
}
int main()
{
	long long int t,n;
	t = read_int();
	long long int j=1;
	while(t--)
	{
		long long int i = 1;
		long long int result = 0;
		n = read_int();
		if(n==0)
		{
			result = 0;
		}
		else
		{
			long long int val = n;;
			long long i=0;
			long long int count = 0;
			int ctr[10] = {0};
			while(1)
			{
				long long int m = val;
				//cout << m << endl;
				long long int d;
				while(m)
				{
					d = m%10;
					if(ctr[d]==0)
					{
						count++;
					}
					ctr[d]++;
					m = m/10;
				}
				if(count==10)
				{
					result = val;
					break;
				}
				i++;
				val = i*n;
			}
		}
		if(result==0)
		{
			cout << "Case #" << j << ": " << "INSOMNIA" << endl;
		}
		else
		{
			cout << "Case #" << j << ": " << result << endl;
		}
		j++;
	}
	return 0;
}
