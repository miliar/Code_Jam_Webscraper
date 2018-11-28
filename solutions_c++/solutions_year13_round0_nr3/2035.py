#include <iostream>
#include <vector> 
#include <algorithm> 

using namespace std;

const int maxn = 4;
int digit[maxn];
const int maxm = 16;
int res[maxm];
long long num;
long long product;
vector<long long> ans;

void test(int step, int mid) {
		num = 0l;
		for (int i = 0; i < step; i++)
			num = num * 10 + digit[i];
		if (mid != -1)
			num = num * 10 + mid;
		for (int i = step - 1; i >= 0; i--)
			num = num * 10 + digit[i];
		int m = 0;
		product = num * num;
		while (product > 0) {
			res[m] = product % 10;
			product = product / 10;
			m ++;
		}
		bool flag = true;
		for (int i = 0; i < m / 2; i++)
			if (res[i] != res[m - i - 1]) {
				flag = false;
				break;
			}
		if (flag) {
			//printf("%lld, prod = %lld\n", num, num*num);
			ans.push_back(num*num);
		}
}

void find(int step) {
	if (step > 0) {
		test(step, -1);
		for (int i = 0; i <= 9; i++)
			test(step, i);
	}
	if (step == maxn)
		return;
	for (int i = 0; i < 9; i++) {
		if (step == 0 && i == 0)
			continue;
		digit[step] = i;
		find(step + 1);
	}
}

int main() {
	//long long x = 99980001L;
	//printf("%lld\n", x*x);
	ans.push_back(1);
	ans.push_back(4);
	ans.push_back(9);
	find(0);
	sort(ans.begin(), ans.end());
	//for(vector<long long >::const_iterator i = ans.begin(); i != ans.end(); ++i)
    //	cout << *i << '\n';
    int testcases;
    cin >> testcases;
    long long A, B;
    for (int t = 0; t < testcases; t++) {
    	cin >> A >> B;
    	//printf("A = %lld, B = %lld\n", A, B);
    	int count = 0;
    	for(vector<long long >::const_iterator i = ans.begin(); i != ans.end(); ++i) {
    		long long tmp = *i;
    		if (tmp >= A && tmp <= B)
    			count ++;
    	}
    	printf("Case #%d: %d\n", t + 1, count);
    //	cout << *i << '\n';
    }
	return 0;
}