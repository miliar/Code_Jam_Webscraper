//D
//Code Jam 2016
#include <bits/stdc++.h>
using namespace std;
int main(){
	int t,t1;
	cin>>t;
	t1=t;
	while(t--){
		cout<<"Case #"<<t1-t<<": ";
		int k,n,s;
		cin>>k>>n>>s;
		cout<<"1";
		for (int i = 1; i < s; i++)
		{
			cout<<" "<<i+1;
		}
		cout<<endl;
	}
	return 0;
}
