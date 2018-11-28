#include<iostream>
#include<vector>
#include<list>
#include<algorithm>
#include<cstdlib>
typedef unsigned long int ul;
using namespace std;
int main()
{	int t;
	list<ul> a;
	cin>>t;
	ul n,ans,val;
	while(t--)
	{	
		vector<ul> d;
		cin>>n;
		int i=1;
	
		if(n!=0)
		{	
			while(d.size()<10)
			{	
				ans=n*i;
				val=ans;
			
				while(val>0)

				{	
					if(std::find(d.begin(), d.end(),val%10)==d.end())
					
					{	
						d.push_back(val%10);
					}
					
					
					val=val/10;				

				}
				i++;
			
			
			}
			a.push_back(ans);
		
	

		}
		else
			{
				a.push_back(0);
				
			}
	}


list <ul> :: iterator l;
int i=1;
for(l=a.begin(); l!=a.end();l++)
{
	if(*l==0)
		cout<<"Case #"<<i<<": "<<"INSOMNIA\n";
	else
		{cout<<"Case #"<<i<<": ";
		 cout<<*l<<"\n";}
	i++;
}

		
		

return 0;
}
