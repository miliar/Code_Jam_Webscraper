#include<iostream>
#include<vector>
using namespace std;

bool pld(int r) {
	vector<int> v;
	while(r > 0) {
		v.push_back(r%10);
		r = r/10;
	}
	int len = v.size();
	for(int i=0; i<=(len-1)/2; i++) {
		if(v[i] != v[len-i-1]) return false;
	}
	return true;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int n, cs, cnt=0;
	double a, b;
	cin>>n;

	for(cs=1; cs<=n; cs++) {
		cin>>a>>b;
		
		int aa = sqrt(a);
		int bb = sqrt(b);

		for(int i=aa; i<=bb; i++) {
			if(pld(i)) {
				if(i*i >= a && i*i <= b && pld(i*i)) 
					cnt++;
			}
		}

		cout<<"Case #"<<cs<<": "<<cnt<<endl;
		cnt=0;
	}

	return 0;
}