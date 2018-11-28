#include<bits/stdc++.h>

using namespace std;

int jj,cnt=0,num[50];

long long mulmod(long long a, long long b, long long mod)
{
    long long x = 0,y = a % mod;
    while (b > 0)
    {
        if (b % 2 == 1)
        {    
            x = (x + y) % mod;
        }
        y = (y * 2) % mod;
        b /= 2;
    }
    return x % mod;
}
/* 
 * modular exponentiation
 */
long long modulo(long long base, long long exponent, long long mod)
{
    long long x = 1;
    long long y = base;
    while (exponent > 0)
    {
        if (exponent % 2 == 1)
            x = (x * y) % mod;
        y = (y * y) % mod;
        exponent = exponent / 2;
    }
    return x % mod;
}

bool Miller(long long p,int iteration)
{
    if (p < 2)
    {
        return false;
    }
    if (p != 2 && p % 2==0)
    {
        return false;
    }
    long long s = p - 1;
    while (s % 2 == 0)
    {
        s /= 2;
    }
    for (int i = 0; i < iteration; i++)
    {
        long long a = rand() % (p - 1) + 1, temp = s;
        long long mod = modulo(a, temp, p);
        while (temp != p - 1 && mod != 1 && mod != p - 1)
        {
            mod = mulmod(mod, mod, p);
            temp *= 2;
        }
        if (mod != p - 1 && temp % 2 == 0)
        {
            return false;
        }
    }
    return true;
}

long long convert(long long b,int s)
{
	long long n=0;
	
	for(int i=0;i<s;i++)
		n=n*b+(long long)(num[i]);
		
	return n;
}

void check(int s,int n)
{
	if(s==n-1)
	{
		if(cnt==jj)
			return;
		
		int f=0;
		
		long long c[20],ans=0,aa[20];
		
		num[s]=1;
		
		for(int i=2;i<11;i++)
			c[i]=convert(i,n);
			
		for(long long i=2;i<11;i++)
		{
			int ff=1;
			
			for(long long j=2;j*j<=c[i];j++)
				if(c[i]%j==0)
				{
					ff=0;
					aa[i]=j;
					break;
				}
				
			if(ff)
			{
				f=1;
				break;
			}
		}
	
		if(f)
			return;
			
		cnt++;
			
		cout << c[10] << " ";
	
		for(long long i=2;i<11;i++)
			cout << aa[i] << " "; 
		
		cout << endl;
		
		return;
	}
	
	num[s]=0;
	
	check(s+1,n);
	
	num[s]=1;
	
	check(s+1,n);
}

int main()
{
	int t;
	
	freopen("C-small-attempt0.in","r",stdin);
	freopen("a.txt","w",stdout);
	
	cin >> t;
	
	for(int tt=0;tt<t;tt++)
	{
		int n;
		
		cin >> n >> jj;
		
		cout << "Case #" << tt+1 << ":" << endl;
		
		num[0]=1;
		
		check(1,n);
	}
	
	return 0;
}
