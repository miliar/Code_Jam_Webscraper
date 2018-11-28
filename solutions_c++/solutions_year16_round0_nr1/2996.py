#include <bits/stdc++.h>

using namespace std;

long long  f[10];
long long cou;
void fun(long long m)
{
	long long dig=0;
	while(m)
	{
		dig= m%10;
		if(f[dig]==0)
		{
			cou++;
			f[dig]=1;
		}
		m = m/10;
	}
}

int main()
{
	long long n,t;
	freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
	
	scanf("%lld",&t);
	int tst=0;
	
	while(t--)
	{
		tst++;
	    scanf("%lld",&n);
	    memset(f,0,sizeof(f));
	    
		if(n==0)
		{
		   printf("Case #%d: INSOMNIA\n",tst);	
		}	
		else
		{
			 cou = 0 ;
			 long long temp=n;
		     for(int i=1; ;i++)
			 {
			    fun(temp);
			    
			    if(cou==10)
			    {
			       printf("Case #%d: %lld\n",tst,temp);   
				   //cout << i << endl;
				   break; 	
				}
			//	cout<< cou << " " << temp << endl;
				temp = n * (i+1);	
			 }	
		}
	}
	return 0;
}
