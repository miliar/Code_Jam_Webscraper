#include <bits/stdc++.h>
using namespace std;

int main() {
	int t,s,ct,i,j,k;
	char arr[1002];
	cin>>t;
	for(k=0;k<t;k++)
	{
		cin>>s>>arr;
		ct=0; j=0;
		for(i=0;i<=s;i++)
		{
			ct+=(arr[i]-48);
			if(ct>=(i+1)) continue;
			else { j+=abs(ct-(i+1)); ct+=abs(ct-(i+1)); }
			//cout<<j<<","<<i<<" ";
		}
		cout<<"Case #"<<k+1<<": "<<j<<endl;
	}
	return 0;
}