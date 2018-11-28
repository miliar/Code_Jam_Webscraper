#include <iostream>
#include <cstring>
using namespace std;

long long T,num,now;
bool u[10];

bool check() {
	for (int i=0; i<10; i++)
		if (!u[i]) return false;
	return true;
}

bool reg(long long k) {
	long long p;
	while (k>0) {
		p=k%10;
		u[p]=true;
		k/=10;
	}
}

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	cin>>T;
	for (int ii=1; ii<=T; ii++) {
		memset(u,0,sizeof(u));
		cin>>num;
		if (num==0) {
			cout<<"Case #"<<ii<<": INSOMNIA\n";
		} else {
			now=0;
			while (!check()) {
				now+=num;
				reg(now);
			}
			cout<<"Case #"<<ii<<": "<<now<<endl;
		}
	}
}
