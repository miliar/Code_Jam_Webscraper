#include <bits/stdc++.h>
using namespace std;

int main() {
	
	ios_base::sync_with_stdio(false);
	long long int t,i,j,k,l,m,n,num;
	cin>>t;
	l=1;
	while(t--)
	{
		cin>>n;
		
		if(n==0)
		{
			cout<<"Case #"<<l++<<": INSOMNIA\n";
			continue;
		}
		
		set <int> s;
		
		k=s.size();
		
		i=1;
		
		num=i*n;
		
		while(k!=10)
		{
			i++;
			while(num!=0)
			{
				
				j=num%10;
				s.insert(j);
				num/=10;
				
			}
			
			k=s.size();
			
			num=i*n;
			
			
			
		}
		
		num=(i-1)*n;
		
		cout<<"Case #"<<l++<<": "<<num<<"\n";
		
		
	}
	
}
