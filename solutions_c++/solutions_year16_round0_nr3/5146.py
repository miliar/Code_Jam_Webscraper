#include<bits/stdc++.h>
using namespace std;
int isprime(long long n)
{
	long long i;
	for(i=2;i*i<=n;i++)
	{
		if(n%i==0)
		return i;
	}
	return 0;
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("3.txt","w+",stdout);
	int t,n,j,check,i,m,cse=1,l,count=0,k;
	int a[12];
	long long x,y,u;
	vector<int> vec;
	cin>>t;
	while(t--)
	{
		cin>>n>>m;
		y=(1<<(n-1))+1;
		u=1<<n;
		
		cout<<"Case #"<<cse++<<":\n";
		for(i=y;i<u;i++)
		{
			
			if(i%2==0)
			continue;
			j=i;
			check=isprime(j);
			if(check==0)
			continue;
			else
			a[2]=check;
			while(j)
			{
				vec.push_back(j%2);
				j=j/2;
			}
			
			for(k=3;k<=10;k++)
			{
				x=0;
				for(l=vec.size()-1;l>=0;l--)
				x+=vec[l]*pow(k,l);
				
				check=isprime(x);
				if(check!=0)
				a[k]=check;
				else
				break;
			}
			if(k==11)
			{
				for(l=vec.size()-1;l>=0;l--)
				cout<<vec[l];
				for(k=2;k<=10;k++)
				cout<<" "<<a[k];
				cout<<endl;
				count++;
				if(count==m)
				break;
			}
			vec.clear();
		}
	}	
	
	return 0;
}
		
			
		
