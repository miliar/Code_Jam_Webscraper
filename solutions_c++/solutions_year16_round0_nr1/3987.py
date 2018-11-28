#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <cmath>
using namespace std;

struct node
{
	bool a[10];
	bool ok;

	node() {
		for(int i = 0; i < 10; ++i) {
			a[i] = false;
		}
		ok = false;
	}

	void ins(int k) {
		while(k) {
			a[k%10] = true;
			k /= 10;
		}
		bool all = true;
		for(int i = 0; i < 10; ++i) {
			if(! a[i]) {
				all = false;
				break;
			}
		}
		ok = all;
	}
};

void work(int p)
{
	node res;
	int n;
	cin >> n;
	if(n == 0) {
		cout << "Case #" << p << ": " << "INSOMNIA" << endl;
		return;
	}
	for(int i = n; ; i += n) {
		res.ins(i);
		if(res.ok == true) {
			cout << "Case #" << p << ": " << i << endl;
			break;
		}
	}

}

int main()
{
	int n;
	cin >> n;
	for(int i = 1; i <= n; ++i) {
		work(i);
	}
	return 0;
}
