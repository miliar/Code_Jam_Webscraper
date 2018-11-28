#include<iostream>
#include<algorithm>
using namespace std;

int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		int n,x;
		cin>>n>>x;
		int s[10000];
		for(int j=0;j<n;j++)
			cin>>s[j];
		sort(s,s+n);
		int j=0;
		for(int k=n-1;j<k;k--)
			if(s[j]+s[k]<=x)
				j++;
		cout<<"Case #"<<i<<": "<<n-j<<endl;
	}
	return 0;
}
