#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int t,n,q;
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>n;
		int z = 2*n - 1;
		int vis[3000]={0};
		while(z--){
			for(int j=1;j<=n;j++){
				cin>>q;
				vis[q]++;
			}
		}
		cout<<"Case #"<<i<<": ";
		for(int j=1;j<=2500;j++){
			if(vis[j]%2==1)
				cout<<j<<" ";
		}
		cout<<endl;
		
	}
	return 0;
}