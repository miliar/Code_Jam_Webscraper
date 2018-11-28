#include<iostream>

using namespace std;

int tens[] = {1,10,100,1000,10*1000,100*1000,1000*1000};
int T;
int ans;
int A,B;

bool isPalin(int x) {
	int digs;
	for(digs = 0 ; x >= tens[digs] ; digs++) ;
	for(int i=0;i*2<=digs;i++)
		if((x/tens[i])%10 != (x/tens[digs-i-1])%10)
			return false;
	return true;
}
int main() {
	cin>>T;
	for(int ti=0;ti<T;ti++) {
		ans = 0;
		cin>>A>>B;

		int i;
		for(i=0;i*i<A;i++) ;
		for(;i*i<=B;i++)
			if(isPalin(i)&&isPalin(i*i))
				ans++;

		cout<<"Case #"<<ti+1<<": "<<ans<<endl;
	}
	
//	for(int i=1;i<10000;i++) {
//		if(isPalin(i)&&isPalin(i*i))
//			cout<<i<<" : "<<i*i<<endl;
//	}
	return 0;
}