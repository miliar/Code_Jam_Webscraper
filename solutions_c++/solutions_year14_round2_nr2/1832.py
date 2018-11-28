#include <iostream>
using namespace std;

int main() {
	
	long long i,j,t,q,a,b,k,ans;
	cin>>t;
	q=1;
	while(t--)
	{   ans=0;
		cin>>a>>b>>k;
		for(i=0;i<a;i++)
		{//cout<<i<<endl;
			for(j=0;j<b;j++)
			{
				if((i&j)<k)
				{ans++;
				
				}
			}
			
		}
		cout<<"Case #"<<q++<<": "<<ans<<endl;
	}
	return 0;
}
