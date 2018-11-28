#include <iostream>

using namespace std;


int main() {
	// your code goes here
	long long i,j,t,q,a,b,k,count;
	cin>>t;
	q=1;
	while(t--)
	{count=0;
		cin>>a>>b>>k;
		for(i=0;i<a;i++)
		{//cout<<i<<endl;
			for(j=0;j<b;j++)
			{
				if((i&j)<k)
				{count++;
				
				}
			}
			
		}
		cout<<"Case #"<<q++<<": "<<count<<endl;
	}
	return 0;
}