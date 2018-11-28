#include <iostream>

using namespace std;

uint64_t count(int start) {
	int found[10] = {0,0,0,0,0,0,0,0,0,0};
	int cnt = 0;
	uint64_t curr = 0;
	while(cnt < 10) {
		curr += start;
		uint64_t tmp = curr;
		while(tmp != 0) {
			int digit = tmp%10;
			tmp = tmp/10;
			if (found[digit] == 0) {
				cnt++;
				found[digit] = 1;
			}
		}
	}
	return curr;
}

int main(int argc, char *argv[]) {
	int cases;
	cin>>cases;
	int ind = 1;
	while(ind <= cases) {
		int inp;
		cin>>inp;
		if (inp == 0) {
			cout<<"Case #"<<ind<<": INSOMNIA"<<endl;
		}
		else {
			cout<<"Case #"<<ind<<": "<<count(inp)<<endl;
		}
		ind++;
	}
	return 0;
}
