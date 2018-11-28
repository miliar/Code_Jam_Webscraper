#include<bits/stdc++.h>
using namespace std;
set<int> s;
int main()
{
    long long int t,n,i,k,flag,h,r,l;
//    freopen("1.txt","r",stdin);
//    freopen("2.txt","w",stdout);
	cin>>t;
	for(k=1;k<=t;k++)
	{
		flag=0;
		i=1;
		cin>>n;
		while(i<101)
		{
			h=n*i;
			l=h;
			
			while(h!=0)
			{
				r=h%10;
				s.insert(r);
				h/=10;
				
			}
			if(s.size()==10)
			{
			    flag=1;
			    break;
			}
			i++;
			
		}
		if(flag==1)
		cout<<"Case #"<<k<<": "<<l<<endl;
		else
		cout<<"Case #"<<k<<": INSOMNIA"<<endl;
		s.clear();
	}	
	
}
