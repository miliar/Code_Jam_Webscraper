#include <iostream>
#include <stdio.h>

using namespace std;

const int SIZE = 4;

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int count;
	bool pline;
	cin >> count;
	char * mtx = new char[16];
	for(int i=0; i<count; ++i) {
		pline = false;
		int j=0, k=0;
		char st;
		for(j=0; j<SIZE; ++j) {
			for(k=0; k<SIZE; ++k) {
				cin >> *(mtx+SIZE*j+k);
			}
		}
		for(j=0; j<SIZE; ++j) {
			st = *(mtx+SIZE*j);
			k=1;
			if(st=='T') st = *(mtx+SIZE*j+ k++);
			for(;k<SIZE; ++k) {
				if(st!=*(mtx+SIZE*j+k)&&*(mtx+SIZE*j+k)!='T') break;
			}
			if(k==SIZE) {
				if('.'==st) { pline = true; }
				else {
					cout << "Case #" << i+1 << ": " << st << " won\n";
					j = SIZE + 1;
					break;
				}
			}
		}
		if(j<=SIZE) {
			for(j=0; j<SIZE; ++j) {
				st = *(mtx+j);
				k=1;
				if(st=='T') st = *(mtx+SIZE*k++ +j);
				for(;k<SIZE; ++k) {
					if(st!=*(mtx+SIZE*k+j)&&*(mtx+SIZE*k+j)!='T') break;
				}
				if(k==SIZE) {
					if('.'==st) { pline = true; }
				else {
					cout << "Case #" << i+1 << ": " << st << " won\n";
					j = SIZE + 1;
					break;
				}
				}
			}
		}
		if(j<=SIZE) {
			k=0;
			st = *(mtx+SIZE*k+k);
			if('T'==st) st = *(mtx+SIZE*++k + k);
			for(;k<SIZE; ++k) {
				if(st!=*(mtx+SIZE*k+k)&&*(mtx+SIZE*k+k)!='T') break;
			}
			if(k==SIZE) {
				if('.'==st) { pline = true; }
				else {
				cout << "Case #" << i+1 << ": " << st << " won\n";
				j=SIZE+1;
				continue;
			}
			}
		}
		if(j<=SIZE) {
			k=3;
			char st = *(mtx+SIZE*(SIZE-k-1)+k);
			if(st=='T') st = *(mtx+SIZE*(SIZE- --k-1)+k);
			for(;k>=0; --k) {
				if(st!=*(mtx+SIZE*(SIZE-k-1)+k)&&*(mtx+SIZE*(SIZE-k-1)+k)!='T') break;
			}
			if(k==-1) {
				if('.'==st) { pline = true; }
				else {
				cout << "Case #" << i+1 << ": " << st << " won\n";
				j=SIZE+1;
				continue;
			}
			}
		}
		if(j<=SIZE) {
			if(pline) cout << "Case #" << i+1 << ": Game has not completed\n";
			else cout << "Case #" << i+1 << ": Draw\n";
		}
	}
    return 0;
}
