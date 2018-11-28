#include <bits/stdc++.h>
using namespace std;

int main() {
	long long int t,r,c,w,ans,i,tp,ans1;
	cin>>t;
	for(i=0;i<t;i++){
		cin>>r>>c>>w;
		cout<<"Case #"<<i+1<<": "<<((r-1)*c)/w+w-1+(w+c-1)/w<<endl;
	}
	return 0;
}