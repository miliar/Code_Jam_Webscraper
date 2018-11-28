#include <iostream>
using namespace std;

int res(int a, int b, int c ){
	unsigned long long sum = 0;
	for(int i = a-1; i>=0; i--){
		for(int j = b-1; j>=0; j--){
//			cout<<i<<" - "<<j<<" = "<<(i&j)<<endl;
			if( (i&j) < c )
				sum++;
		}
	}
	return sum;
}

int main(int argc, char *argv[]) {
	int a,b,k;
	int n;
	cin>>n;
	
	for(int i = 1 ; i <= n ; i++ ){
		cin>>a>>b>>k;
		cout<<"Case #"<<i<<": "<<res(a,b,k)<<endl;
	}
	return 0;
}

