#include<bits/stdc++.h>

using namespace std;
int main(){
	int n;
	int t;
	cin>>t;
	int z = 0;
	while(t--){
	z++;
	cin>>n;
	int he[2510];
	memset(he,0,sizeof(he));
	for(int i = 0;i<2*n*n-n;i++){
		int el;
		cin>>el;
		he[el]++;
	}
	cout<<"Case #"<<z<<": ";
	for(int i = 1;i<2502;i++){
		if(he[i]%2!=0){
			cout<<i<<" ";
		}
	}
	cout<<endl;
}
	
}


