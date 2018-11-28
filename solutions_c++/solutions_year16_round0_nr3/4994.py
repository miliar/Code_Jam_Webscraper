#include<stdio.h>
#include<iostream>
#include<math.h>

using namespace std;

long long a[66000],n;

long long bas(long long num, long long b)
{
    long long nb=0;
    int p=0;
    while(num>0)
    {
    	long long r= num%10;
    	long long m=1;
    	for(int i=1;i<=p;i++)
    	    m*=b;
    	
    	//long long m = pow(b, p);
    	
    	nb = nb + m*r;
    	p++;
    	num/=10;
    }
    return nb;
}

long long prime(long long num)
{
	long long r = sqrt(num);
	if(num<=3)
	       return 0;
	if(num%2==0) 
        return 2;       
	for(int i=3;i<=r;i+=2)
	      if(num%i==0)
	             return i;
	             
    return 0;
}
int main()
{
	//freopen("in.txt", "r", stdin);
	//freopen("c.txt", "w", stdout);
    int t, cas, k, i, j, c, total;
    cin>>t;
    for(cas=1;cas<=t;cas++)
    {
        cin>>n>>k;
        
        c = 0, i=0, j=0;
        a[i++] = 1;
        c = 2;
        while(c<=n)
        {
            for(j=0;j<i;j++)
                a[j]*=10;
            for(j=i;j<2*i;j++)
                a[j]= a[j-i] + 1;
            i = j;
            c++;
        }
        total = i;
        cout << "Case #" << cas << ":\n";
        
        for(i=0;i<total && k>0;i++)
        {
        	int f=1;
        	long long d[15];
        	if(a[i]%10 == 0)
        	     f=0;
        	for(j=2;j<=10&&f==1;j++)
        	{
        		
        		long long num = bas(a[i], j);
        		d[j] = prime(num);
        		if(d[j] == 0)
        		{
        			f = 0;
        			break;
        		}
        	}
        	if(f == 1)
        	{
        		cout << a[i];
        		for(j=2;j<=10;j++)
                    cout << " " << d[j];
        	    printf("\n");
        	    k--;
        	}
        }
        
    }
    return 0;
    
}
