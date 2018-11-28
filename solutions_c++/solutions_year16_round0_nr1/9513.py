#include <bits/stdc++.h>
using namespace std;
bool check[10];
bool tes(){
	bool a=true;
	for (int i=0;i<10;i++){
		a=a&check[i];
	}
	return a;
}
int main() {
	int n;cin>>n;
	for (int i=1;i<=n;i++){
		int x;cin>>x;
		bool ada=false;
		memset(check,0,sizeof(check));
		for (int j=1;j<1000;j++){
			int t=x*j;
			while (t>0){
				check[t%10]=1;
				t=t/10;
			}
			if (tes()){
				ada=true;
				cout<<"Case #"<<i<<": "<<(x*j)<<endl;
				break;
			}
		}
		if (!ada) cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
	}
	return 0;
}