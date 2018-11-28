#include <iostream>
#include <vector>
#include <utility>

typedef unsigned long int uli;
typedef long int li;
using namespace std;

void check_all_digit(uli val, vector<bool>& flag, int& ctr) {
	int d;
	while(val>0) {
		d = val%10;
		if (!flag[d]) {
			flag[d] = 1;
			ctr++;
		}
		val /= 10;
	}
	return;
}

li compute_steps(li& N) {
	vector<bool> flag(10,0); //0-9
	int ctr = 0;
	uli tmp;
	li steps;
	for (steps=1; steps<=100 && ctr<10; steps++) {
		tmp = steps*N;
		check_all_digit(tmp, flag, ctr);
	}
	//cout << tmp << " " << steps << endl;
	if (ctr==10) {
		return tmp;
	} else {
		return -1;
	}
}

int main(int argc, char *argv[])
{
	int T;
	li N, res;
	cin >> T;
	for(int i=1; i<=T; i++) {
		cin >> N;
		res = compute_steps(N);
		if (res<0) {
			cout << "Case #" << i << ": INSOMNIA" << endl;
		} else {
			cout << "Case #" << i << ": " << res << endl;
		}
	}
    return 0;
}
