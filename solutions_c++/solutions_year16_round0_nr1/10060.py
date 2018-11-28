#include <iostream>
#include <vector>
using namespace std;

int update(bool *found, int n){
	int cnt = 0;
	while (n > 0){
		int t = n % 10;
		if (!found[t]){
			found[t] = true;
			cnt++;
		}
		n /= 10;
	}
	return cnt;
}

int calc(int n){
	if (n == 0)
		return -1;
	bool found[10] = {0};
	int cnt = 0;
	int i =1;
	while(true){
		cnt += update(found, n * i);
		if (cnt == 10)
			return i;
		i++;
	}
	return -1;
}

int main(){
	int ntest;
	cin >> ntest;
	for(int i = 0; i < ntest;i ++){
		int n;
		cin >> n;
		int t = calc(n);
		cout << "Case #" << (i + 1) << ": ";
		if (t == -1)
			cout << "INSOMNIA";
		else
			cout << t * n;
		cout << endl;
	}
	return 0;
}
