#include<iostream>
#include<string>
#include<algorithm>
#include<fstream>
using namespace std;

#define LL long long

bool ispal(LL x){
	int a[100];
	int i = 0;

	while(x){
		a[i] = x % 10;
		x /= 10;
		i++;
	}
	for(int j = 0; j < i / 2; j++)
		if(a[j] != a[i - 1 - j])
			return false;
	return true;
}

LL x[1000];
int main(){
	freopen("C-large-1.in", "r", stdin);
	freopen("C2.out", "w", stdout);

	LL a = 10000001;
	int t, cnt = 0;
	LL b;
	for(LL i = 1; i < a; i++){
		if(ispal(i)){
			LL j = i * i;
			if(ispal(j))
				x[cnt++] = j;
		}
	}

	cin >> t;
	for(int i = 0; i < t; i++){
		cin >> a >> b;
		int ans = 0;
		for(int i = 0; i < cnt; i++){
			if(x[i] >= a && x[i] <= b)
				ans++;
		}
		cout << "Case #" << i + 1 << ": ";
	cout << ans << endl;
	}


	return 0;
}