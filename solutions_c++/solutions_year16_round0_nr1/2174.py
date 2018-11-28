#include <bits/stdc++.h>
using namespace std;


bool vis[10];
int rem;
bool add(long long int n){
	while(n > 0){
		if(vis[n%10] == false){
			vis[n%10] = true;
			rem -= 1;
		}
		n /= 10;
	}
	if(rem == 0) return true;
	else return false;
}


int main(){
	int cases;cin>>cases;
	for(int n=0;n<cases;n++){
		for(int i=0;i<10;i++) vis[i] = false;
		rem = 10;
		long long int x;
		cin>>x;
		int i = 1;
		for(i=1;i<100000;i++){
			if(add(x*i)) break;
		}
		if(rem == 0){
			cout<<"Case #"<<n+1<<": "<<x*i<<endl;
		}else{
			cout<<"Case #"<<n+1<<": INSOMNIA"<<endl;
		}
	}
	return 0;
}
