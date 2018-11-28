#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen ("input.txt","r",stdin);
	freopen ("myfile.txt","w",stdout);
	long long n,b[10],i,j,s1,r;
	int t;cin>>t;
	int p=1;
	while(t--)
	{
		
		long long s=0;
		for(i=0;i<10;++i)
		b[i]=0;	
		
		cin>>n;
		if(n==0){cout<<"Case #"<<p<<": "<<"INSOMNIA"<<endl;p++;continue;}
		while(true)
		{
			s+=n; s1=s;
			while(s1>0)
			{
				
				r=s1%10;
				s1=s1/10;
				b[r]++;
				}
				long long c=0;
			for(i=0;i<10;++i)
			{
				if(b[i]>0)c++;
				
			}
		
			if(c>=10){cout<<"Case #"<<p<<": "<<s<<endl;break;}
		}
		p++;
	}
	return 0;
}
