#include <bits/stdc++.h>
#define endl '\n'

using namespace std;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int t,n;	
	cin>>t;

	int u = 1;
	
	while(t--){
		cin>>n;
		
		if(!n){
			cout<<"Case #"<<u++<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		
		int mask = 0;
		int o = n;
		
		while(mask!=1023){
			int aux = o;
			while(aux){
				mask |= 1<<( aux%10 );
				aux /= 10;
			}
			o += n;
		}
		
		cout<<"Case #"<<u++<<": "<<o - n<<endl;
	}
	return 0;
}
