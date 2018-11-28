#include <iostream>
using namespace std;

int main() {
	// your code goes here
	long long a,b;
	char c;
	int n;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		cin>>a;
		cin>>c;
		cin>>b;
		long long d=b;
		while(b%2==0)
			b/=2;
		printf("Case #%d: ",i+1);
		if(b!=1)
			cout<<"impossible\n";
		else
		{
			int x=0;
			while(a<d)
			{
				d/=2;
				x++;
			}
			cout<<x<<endl;
		}
	}
	return 0;
}