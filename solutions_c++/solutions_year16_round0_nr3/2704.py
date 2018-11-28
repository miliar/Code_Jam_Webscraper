#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef map<int, int> mii;


ll _sieve_size;
bitset<100000100> bs;   // 10^7 should be enough for most cases
vi primes;   // compact list of primes in form of vector<int>

void sieve(ll upperbound) {          // create list of primes in [0..upperbound]
	_sieve_size = upperbound + 1;                   // add 1 to include upperbound
	bs.set();                                                 // set all bits to 1
	bs[0] = bs[1] = 0;                                     // except index 0 and 1
	for (ll i = 2; i <= _sieve_size; i++) if (bs[i]) {
			// cross out multiples of i starting from i * i!
			for (ll j = i * i; j <= _sieve_size; j += i) bs[j] = 0;
			primes.push_back((int)i);  // also add this vector containing list of primes
		}
}

bool isPrime(ll N) {                 // a good enough deterministic prime tester
	if (N <= _sieve_size) return bs[N];                   // O(1) for small primes
	for (int i = 0; i < (int)primes.size(); i++)
		if (N % primes[i] == 0) return false;
	return true;                    // it takes longer time if N is a large prime!
}

bool check(int arr[], int n) {
	bool found = false;
	for (int i = 2; i <= 10; i++) {
		ll sum = 0;
		for (int c = 0; c < n; c++) {
			int ind = n - 1 - c;
			ll pp = pow(i, ind);
			// cout<<pp<" ";
			sum += ( pp * arr[c]);
		}
		// cout<<i <<" "<<sum<<endl;
		if (isPrime(sum)) {
			// cout<<i <<" "<<sum<<endl;
			found = true;
		}
	}
	if (!found)
		return true;
	else
		return false;
}

vector<ll> get(int arr[], int n) {
	vector<ll> srr2(12);
	// srr2.assign(12,0l);
	for (int i = 2; i <= 10; i++) {
		ll sum = 0;
		for (int c = 0; c < n; c++) {
			int ind = n - 1 - c;
			ll pp = pow(i, ind);
			sum += ( pp * arr[c]);
		}
		srr2[i] = sum;
	}
	return srr2;
}
ll div(ll curr){
	for(ll i=2;i<curr;i++){
		if(curr%i == 0)
			return i;
	}
}
int main() {
	int tc;
	sieve(10000000);
	cin >> tc;
	for (int tt = 1; tt <= tc; tt++) {
		int n, j;
		cin >> n >> j;
		int count = 0;
		printf("Case #%d:\n", tt);
		for (int i = 0; i < (1 << n); i++) {
			int arr[n];
			vector<ll> arr2(12);
			memset(arr, 0, sizeof arr);
			for (int j = 0; j < n; j++) {
				if (i & (1 << j))
					arr[j] = 1;
			}
			if (arr[0] == 0 || arr[n - 1] == 0)
				continue;

			if (check(arr, n)) {
				arr2 = get(arr,n);
				count++;
				for (int cc = 0; cc < n; cc++)
					printf("%d", arr[cc]);
				printf(" ");
				for(int k=2;k<=10;k++)
					cout<<div(arr2[k])<<" ";
				printf("\n");

			}
			if (count == j)
				break;
		}

	}
}