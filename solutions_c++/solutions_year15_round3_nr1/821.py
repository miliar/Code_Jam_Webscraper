#include <iostream>
using namespace std;
int arr[60][20];
int main() {
	int t, r, c, w;
	cin>>t;
	for(int k=1; k<=t; k++)
	{
		cin>>r>>c>>w;
		int count=c/w;
		count=count*r;
		int x;
		if(c%w==0)
		x=0;
		else
		x=1;
		cout<<"Case #"<<k<<": "<<count+w-1+x<<endl;
		
	}
	return 0;
}