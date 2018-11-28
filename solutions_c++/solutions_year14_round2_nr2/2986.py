#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	int x=1;
	while(t--){
 		x++;
		long long int a,b,k,i,j;
		cin>>a>>b>>k;
		long long int ans=0;
		for(i=0;i<a;i++)
		{
			for(j=0;j<b;j++)
			{
				if((i&j)<k)
				{
					ans++;
				}
			}
		}
		cout<<"Case #"<<x<<": "<<ans<<endl;
		
	}
	return 0;
}