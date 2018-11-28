#include<iostream>
#include<vector>

using namespace std;

long long x, y, n, i, j, T, a[100];
vector<long long> v[100];

long long convert(long long x, long long to) {
	long long p = 1;
	long long res = 0;
	while(x) {
		res += p*(x%2);
		x/=2;
		p*=to;
	}
	return res;
}

bool isprime(long long x) {
	long long y = 2;
	while(y*y<=x) {
		if(x%y==0) {
			v[i].push_back(y);
			//cout<<x<<" : "<<y<<endl;
			return false;
		}
		y++;
	}
	return true;
}

bool check(long long x) {
	long long r;
	v[i].clear();
	for(long long i = 2; i<11; i++) {
		r = convert(x,i);
		if(isprime(r)) return false;
	}
	return true;
}

void bin(long long x) {
	string s = "";
	while(x) {
		if(x%2) s='1'+s; else s='0'+s;
		x/=2;
	}
	cout<<s;
}

int main(){
	cin>>T;
	for(int t=1; t<=T; t++) {
		cin>>n>>j;
		x = (1<<(n-1))+1;
		y = 1<<n;
		i = 0;
		while(i<j && x<y) {
			if(check(x)) a[i++] = x;
			x+=2;
		}
		cout<<"Case #"<<t<<":\n";
		for(int i=0; i<j; i++) {
			bin(a[i]);
			for(int k=0; k<v[i].size(); k++) cout<<" "<<v[i][k];
			cout<<endl;
		}
	}
}