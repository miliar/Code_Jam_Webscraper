#include <iostream>
#include <stdio.h>

using namespace std;

int f[10];

void init() {
	for(int i=0;i<10;i++) {
		f[i] = 0;
	}
}

bool check() {
	for(int i=0;i<10;i++) {
		if(f[i] == 0)	return false;
	}
	return true;
}

int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	long long T,N,n,t,c;
	cin >>T;
	for(int i=0;i<T;i++) {
		cin >> N;
		init();
		n = 0;
		c = 0;
		do {
			n+=N;
			t = n;
			while(t!=0) {
				f[t%10]++;
				t/=10;
			}
			c++;
		} while(!check() && n>0);
		if(n<=0)
			cout<<"Case #"<<(i+1)<<": INSOMNIA"<<endl;
		else
			cout<<"Case #"<<(i+1)<<": "<<n<<endl;
	}
	return 0;
}