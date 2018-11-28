#include <iostream>
#include <stdlib.h>
#include <time.h>


using namespace std;

typedef long long ll;

void count(ll n, int carray[]) {
	while(n) {
		int d = n%10;
		carray[d]+=1;
		n=n/10;
	}
}

bool isDone(int carray[]) {
	bool ans = true;
	for(int i=0;i<10;++i) {
		if(!carray[i]) {
			ans = false;
			break;
		}
	}
	return ans;
}

bool sleepCheck(ll n, ll& lastn) {
	if(n==0) return false;
	int carray[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	count(n, carray);
	ll i = 2;
	while(!isDone(carray)) {
		ll next = i*n;
		count(next, carray);
		lastn = next;
		i++;
	}
	return true;
}

int main() {
	int t;
	cin>>t;
	for(int i=1; i<=t; ++i) {
		ll n;
		cin>>n;
		ll lastn;
		cout<<"Case #"<<i<<": ";
		if(sleepCheck(n, lastn)) {
			cout<<lastn<<"\n";
		} else {
			cout<<"INSOMNIA\n";
		}
	}
#if 0
    srand (time(NULL));
    t = rand() % 10;
    cout<<t<<endl;
	for(int i=0;i<t; ++i) {
		ll n = rand() % 100;
		ll lastn;
		cout<<n<<" ====> ";
		if(sleepCheck(n, lastn)) {
			cout<<lastn<<"\n";
		} else {
			cout<<"INSOMNIA\n";
		}
	}
	return 0;
#endif
}
