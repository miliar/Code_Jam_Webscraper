#include<iostream>
#include<vector>
using namespace std;

#define GI ({int t;cin >> t;t;})

bool ispalin(int t) {
	int n = t, nrev = 0;
	while(n > 0) {
		nrev += n % 10;
		n /= 10;
		if(n == 0) break;
		nrev *= 10;
	}
return t == nrev;
}

int main() {
int nt = GI;
vector<int> v;
for(int i = 1;i < 32;++i) {
	if(ispalin(i) && ispalin(i*i)) {
		v.push_back(i*i);
	}
}

for(int i = 1; i <= nt;++i) {
	int A = GI, B = GI;
	int cnt = 0;
	for(int j = 0;j < v.size();j++)
		if(v[j] >= A && v[j] <= B)
			cnt++;
	cout << "Case #" << i << ": "<<cnt<<endl;
}
return 0;
}
