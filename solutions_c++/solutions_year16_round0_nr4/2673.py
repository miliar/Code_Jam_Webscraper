#include<iostream>
using namespace std;
int main(){
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	int t,k,c,s;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>k>>c>>s;
		cout<<"Case #"<<i+1<<":";
		for(int j=0;j<k;j++)
		{
			cout<<" "<<j+1;
		}
		cout<<"\n";
	}
	return 0;
}
