#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

long long a[16];
long long cn = 0;
void check(){
	long long ans[11]; bool iscoin = true;
	for (long long i=2;i<=10;i++){
		long long num = 0;
		for (long long j=0;j<16;j++){
			num += a[j]; 
			if (j != 15) num*=i;
		}
		bool havefactor = false;
		for (long long j=2;j<=(long long)sqrt(num);j++){
			if (num%j == 0) {
				ans[i] = j;
				havefactor = true;
				break;
			}
		}
		if (!havefactor) {
			iscoin = false; break;
		}
	}
	if (iscoin) {
		for (long long i=0;i<16;i++) cout << a[i];
		for (long long i=2;i<=10;i++){
			cout << " " << ans[i];
		}
		cout << endl;
		cn++;
	}
}
void DFS(long long lvl){
	if (cn > 50) return;
	if (lvl == 15){
		check();
	} else {
		a[lvl] = 0;
		DFS(lvl+1);
		a[lvl] = 1;
		DFS(lvl+1);
		a[lvl] = 0;
	}
}

int main(){
	a[0] = a[15] = 1;
	DFS(1);

	return 0;
}
