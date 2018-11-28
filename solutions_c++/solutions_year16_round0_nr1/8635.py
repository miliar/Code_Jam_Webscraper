#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
using namespace std;
int main()
{
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A-large.out", "w", stdout);
	int r,t=1;
	cin>>r;
	while(t<=r)
	{
		long long int n,p,d,num[10],i,s=1,b=0;
				for(i=0;i<10;i++)
					num[i]=12;
		char c='n';
		cin>>n;
			if(n==0)
			cout<<"Case #"<<t<<": INSOMNIA"<<endl;
			else
				{
					p=n;
					while(c!='y')				
					{
						c='y';
							while(p!=0)
							{
								d=p%10;
								if(num[d]==12)
									{
									num[d]=d;
									}
								p=p/10;
							} 								
							for(i=0;i<10;i++)
							{
								if(c=='y')
								if((num[i]==12))
									{
										s=s+1;
										d=0;
										p=n*s;
										b=p;
										c='n';
									}
							}
							if(c=='y')
								{
								cout<<"Case #"<<t<<": "<<b<<endl;
								}
					}

		
		}

		t=t+1;	
	}
	return 0;
	
}
