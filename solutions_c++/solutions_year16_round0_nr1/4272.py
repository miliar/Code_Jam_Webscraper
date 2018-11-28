#include<iostream>

using namespace std;

long long n, i, x, k, T;

int main(){
	cin>>T;
	for(int t=0; t<T; t++) {
		k = (1<<10) - 1;
		cin>>n;
		cout<<"Case #"<<t+1<<": ";
		if(!n) {
			cout<<"INSOMNIA\n"; 
			continue;
		}
		i = 1;
		while(true) {
			x = n*i;
			while(x) {
				if(k & (1<<(x%10))) k = k ^ (1<<(x%10));
				x/=10;
			}
			if(!k) break;
			i++;
		}
		cout<<n*i<<endl;
	}
}