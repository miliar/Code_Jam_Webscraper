#include<iostream>
using namespace std;
int main()
{
	int n;
	int v[6]={1,4,9,121,484,1001};
	int a,b;
	cin>>n;
	for(int ii=0;ii<n;ii++){
	cin>>a>>b;
	int i=0;
	int j=0;
	while(a>v[i]) i++;
	while(b>=v[j]) j++;
	cout<<"Case #"<<ii+1<<": ";
	cout<<j-i<<endl;}
}
