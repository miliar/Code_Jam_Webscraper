#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	int n,arr[2502]={},x;
	for(int l=1;l<=t;l++)
	{
	int mx=-1;
	cin>>n;
	for(int j=0;j<n*2-1;j++)
	for(int i=0;i<n;i++)
	{
	cin>>x;
	if(x>mx) mx=x;
	arr[x]++;
	}
		cout<<"Case #"<<l<<": ";
	//	cout<<x<<endl;
	for(int i=1;i<=mx;i++) 
	if(arr[i]%2==1) { cout<<i<<" "; arr[i]=0;}
	cout<<endl;
	}
	return 0;
}