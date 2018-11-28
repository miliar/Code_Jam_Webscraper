#include <bits/stdc++.h>
using namespace std;
int main(){
	int t,te,i,j,k,n,inp[2002],m=0;
	cin>>t;
	for(te=0;te<t;te++){
		cin>>n;
		for(i=0;i<n;i++)cin>>inp[i];
		sort(inp,inp+n);
		k=inp[n-1];
		for(i=1;i<inp[n-1];i++){
			m=i;
			for(j=(n-1);j>=0&&inp[j]>i;j--)m+=(((inp[j]+i-1)/i)-1);
			k=min(k,m);
		}
		cout<<"Case #"<<(1+te)<<": "<<k<<"\n";
	}
}