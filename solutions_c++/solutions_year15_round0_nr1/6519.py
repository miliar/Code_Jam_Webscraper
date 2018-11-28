
#include <bits/stdc++.h>

using namespace std;

typedef long long      ll;
typedef pair<int, int> ii;
typedef vector<int>    vi;
typedef vector<ll>    vll;
typedef vector<ii>    vii;
#define pb push_back
#define mp make_pair
#define fi first
#define sc second
#define INF 2000000000
#define MAX_N 1010

int arr[MAX_N];

int main() {
	freopen ("A-large.in", "r", stdin);
	freopen ("out.txt","w", stdout);
	int n;
	scanf(" %d", &n);
	for (int CA = 1 ; CA <= n; CA++) {
		int k;
		scanf(" %d", &k);
		
		for (int i = 0; i < k+1; i++) {;
			char a;
			scanf(" %c", &a);
			arr[i] = a - '0';
		}

		int cnt = 0;
		int sum = arr[0];

		for (int i = 1; i < k+1; i++) {
			if (arr[i] && i > sum) { 
				cnt += i - sum;
				sum += i - sum;
			}
			sum += arr[i];
		}
		printf("Case #%d: %d\n", CA,cnt);
	}
}

