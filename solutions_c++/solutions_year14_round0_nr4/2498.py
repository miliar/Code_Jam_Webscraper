#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	
	for(int x=1;x<=t;x++)
	{
		int n,dw=0,w=0;
		cin>>n;
		double a[n],b[n];
		for(int i=0;i<n;i++)
			cin>>a[i];
		for(int i=0;i<n;i++)
			cin>>b[i];
		sort(a,a+n);
		sort(b,b+n);
		
		for(int i=0,j=0;i<n;i++)
		{
			if(a[i]>b[j])
			{
				dw++;
				j++;
			}
		}
		
		for(int i=n-1,j=n-1;i>=0;i--)
			if(a[i]>b[j])
				w++;
			else
				j--;
				
		cout<<"Case #"<<x<<':'<<" "<<dw<<" "<<w<<endl;
	}
	
	return 0;
}
