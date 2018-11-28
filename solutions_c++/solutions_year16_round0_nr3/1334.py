#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cctype>
#include<cstdlib>
#include<algorithm>
#include<bitset>
#include<cstdio>
#include<cstring>
#include<string>
#include<cctype>
#include<cstdlib>
#include<algorithm>
#include<bitset>
#include<vector>
#include<list>
#include<deque>
#include<queue>
#include<map>
#include<set>
#include<stack>
#include<cmath>
#include<sstream>
#include<fstream>
#include<iomanip>
#include<ctime>
#include<complex>
#include<functional>
#include<climits>
#include<cassert>
#include<iterator>
using namespace std;


#define FLAG 32
//#define __int128 long long int

__int128 m2 = 2;
__int128 m10 = 10;
__int128 m0 = 0;
__int128 mm1 = -1;

__int128 pr(__int128 val){
	for (__int128 i = 2; i*i <= val&&i <= 100000LL; i++){
		if (val % (__int128)(i) == m0){
			return i;
		}
	}
	return -1LL;
}



__int128 BASE = 0;


map<__int128, vector<__int128> > mp;


__int128 B[11][FLAG + 3];

vector<__int128> IN;

__int128 ar[12];


vector<__int128> outt;

void output(__int128 a){
	outt.clear();
	for (int i = 0; i < FLAG; i++){
		outt.push_back(a%m10);
		a /= m10;
	}
	for (int i = FLAG - 1; i >= 0; i--){
		long long int OUT = (long long int)(outt[i]);
		printf("%lld", OUT);
	}
}
int main(){
	IN.assign(10, 0);
	for (int i = 2; i <= 10; i++){
		B[i][0] = 1;
		for (int j = 1; j < FLAG + 1; j++){
			B[i][j] = B[i][j - 1];
			B[i][j] *= (__int128)(i);
		}
	}
	BASE = B[10][FLAG - 1];
	srand(time(NULL));
	while (mp.size() < 500){
		__int128 vv = 0;
		__int128 K = rand();
		for (int k = 0; k < FLAG - 1; k++){
			if (K % m2){
				vv += B[10][k];
			}
			K /= m2;
		}
		if (vv % m10 == m0){
			vv++;
		}
		__int128 NE = vv;
		NE += BASE;
		if (mp.count(NE)){
			continue;
		}
		for (int i = 0; i <= 10; i++){
			ar[i] = m0;
		}

		__int128 tmp = NE;
		for (int i = 0; i < FLAG; i++){
			__int128 mul = tmp % m2;
			tmp /= m10;
			if (mul == m0){
				continue;
			}
			for (int k = 2; k <= 10; k++){
				ar[k] += mul*B[k][i];
			}
		}
		bool ok = false;
		for (int k = 2; k <= 10; k++){
			__int128 b = pr(ar[k]);
			if (b == mm1){
				ok = true;
				break;
			}
			IN[k - 2] = b;
		}
		if (ok == false){
			mp[NE] = IN;
		}
	}
	cout << "Case #1:" << endl;
	for (auto it = mp.begin(); it != mp.end(); it++){
		output((*it).first);
		for (int i = 0; i < 9; i++){
			int C = (*it).second[i];
			cout << " " << C;
		}
		cout << endl;
	}
	return 0;
}