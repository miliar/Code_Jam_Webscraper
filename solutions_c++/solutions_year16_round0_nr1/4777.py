#include<bits/stdc++.h>
using namespace std;
set<int> a;
int main(){
	freopen("a.in","r",stdin);
	freopen("a.txt","w",stdout);
	int n;
	int t;
	int cntt=1,nnn,nn,cnt;
	cin>>t;
	while(t--){
		cin>>n;
		cout<<"Case #"<<cntt++<<": ";
		if(!n)cout<<"INSOMNIA"<<endl;
		else{
			cnt=1;
			a.clear();
			nnn=n;
			while(a.size()!=10){
				nn=nnn;
				while(nn){
					a.insert(nn%10);
					nn/=10;
				}
				nnn+=n;
			}
			cout<<nnn-n<<endl;
		}
	}	
}
