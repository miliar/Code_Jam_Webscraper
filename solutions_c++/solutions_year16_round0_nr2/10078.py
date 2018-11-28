#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <bitset>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <iostream>

using namespace std;
#define VARIABLE(x) cerr << #x << "=" << x << endl
#define BINARY(x) static_cast<bitset<16> >(x);
#define if_range(x, w, h) if (w <= x && x <= h)
#define BitCheck(a,b)   (a >> b) & 1
#define BitSet(a,b)       a |= (1 << b)
#define BitunSet(a,b)    a &= ~(1 << b)
#define MAX(a,b) (((a) > (b)) ? (a) : (b))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))
#define Numof(array)  (sizeof (array) / sizeof *(array))

struct cmp_c {
	bool operator()(int x, int y) {
		return x < y;
	}
} cmp;

void clear(queue<pair<bitset<10>,int> > &q)
{
	queue<pair<bitset<10> ,int> > empty;
	swap(q, empty);
}


bitset<10> change(bitset<10> cake, int amount) {
	bitset<10> buf(cake);

	for (int i = 0; amount > i; i++) {
		buf[i] = ~(cake[amount - i-1]);
	}
	return buf;
}

bool check(bitset<10> cake, int amount) {
	for (int i = 0; amount > i; i++) {
		if (!cake[i])return false;
	}
	return true;
}

int main() {
	queue<pair<bitset<10>,int> > que;
	int n;
	scanf("%d%*c", &n);
	for (int counter = 0; n > counter; counter++) {
		bitset<10> cake(0);
		bool memo[2][2][2][2][2][2][2][2][2][2] = {};
		int amount = 0;
		for (int i = 0; ; i++) {
			char buf;
			scanf("%c", &buf);
			if (buf == '+') cake.set(i);
			else if (buf == '\n')break;
			amount++;
		}
		que.push({ cake , 0});
		while(que.size()) {
			if (check(que.front().first, amount)) {
				printf("Case #%d: %d\n", counter + 1, que.front().second);
				clear(que);
				break;
			}
			for (int i = 0; amount > i; i++) {
				bitset<10> buf(0);
				buf= change(que.front().first, i+1);
				if (memo[buf[0]][buf[1]][buf[2]][buf[3]][buf[4]][buf[5]][buf[6]][buf[7]][buf[8]][buf[9]])
					continue;
				memo[buf[0]][buf[1]][buf[2]][buf[3]][buf[4]][buf[5]][buf[6]][buf[7]][buf[8]][buf[9]] = 1;
				que.push({ buf, que.front().second+1});
			}
			que.pop();
		}
	}
}




//int main() {
//	char num[7];
//	int t;
//	scanf("%d", &t);
//
//	for (int i = 0; t > i; i++){
//		int n,chs = {};
//		long long int n_temp, n_tempt;
//		scanf("%d", &n);
//		if (n == 0) {
//			printf("Case #%d: INSOMNIA\n", i + 1);
//			continue;
//		}
//
//		itoa(n, num, 10);
//
//		for (int j = 1; chs != 1023; j++) {
//			n_temp = n*j;
//			n_tempt = n_temp;
//			while (n_temp > 0) {
//				BitSet(chs, n_temp % 10);
//				n_temp = n_temp/10;
//			}
//		}
//		printf("Case #%d: %lld\n", i+1, n_tempt);
//	}
//}