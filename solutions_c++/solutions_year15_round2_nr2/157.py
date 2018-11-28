#include <iostream>
using namespace std;

int getAns(int r, int c, int n) {
		if (r==3 && c==3 && n==8)
			return 8;
		int ans = 0;
		int t1 = (r*c+1)/2;
		if (n<=t1) {
			return 0;
		}
		n -= t1;
		if (c>r)
			swap(r,c);
		if (c==1) {
			if (r%2==0) {
				if (n==1)
					return 1;
				ans += 1;
				n -= 1;
				return ans + n*2;
			}
			else {
				return n*2;
			}			
		}
		else if (r%2==1 && c%2==1) {
			if (n<=r+c-2) {
				return ans + n * 3;
			}
			ans += (r+c-2)*3;
			n -= (r+c-2);
			ans += n*4;
			return ans;
		}
		else {
			if (n<=2)
				return ans + n*2;
			ans += 4;
			n -= 2;
			if (n<=r+c-4)
				return ans + n*3;
			ans += (r+c-4)*3;
			n -= (r+c-4);
			ans += n*4;
			return ans;
		}
}

int getAns2(int r, int c, int n) {
			
	int ans = 2*r*c-c-r;
	//if (r==3 && c==3) return ans;
	if (r<=2 || c<=2)
		return ans;
	int t1 = ((r-2)*(c-2)+1)/2;
	int tmp = r*c-n;
	if (r*c-n <= t1) {
		return ans - tmp*4;
	}
	tmp -= t1;
	ans -= t1*4;
	int t2 = 0;
	t2 += ((c-2)*r+1)/2 - t1;
	if (r%2==1) {
		t2 -= 1;
	}
	t2 += ((r-2)*c+1)/2 - t1;
	if (c%2==1) {
		t2 -= 1;
	}
	if (tmp <= t2) {
		return ans - tmp*3;
	}

	return 2*r*c-r-c;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int Tn;
	cin >> Tn;
	for (int T=1;T<=Tn;T++) {
		
		int r,c,n;
		cin >> r >> c >> n;

		cout << "Case #" << T << ": " << min(getAns(r,c,n), getAns2(r,c,n)) << endl;
	}
}