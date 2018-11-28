#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

const double eps = 1e-8;
const int dx[] = { 1, 0, -1, 0, -1, -1, 1, 1 };
const int dy[] = { 0, 1, 0, -1, -1, 1, -1, 1 };
const int OO = INT_MAX;

#define SZ(x)          (int)x.size()
#define ALL(x)         (x).begin(),(x).end()
#define ALLR(x)        (x).rbegin(),(x).rend()
#define rep(i,st,en)    for(int i=st ; i< en; i++)
#define repR(i,st,en)   for(int i=st;i>=en ; i--)
#define fill(v, d)       memset(v, d, sizeof(v))
/**************************************************************/
bool digit[10];
bool isFallAsleep(){
	rep(i, 0, 10){
		if(!digit[i]){
			return false;
		}
	}
	return true;
}

void markAsleep(int n){
	while(n){
		digit[n%10] = true;
		n/=10;
	}
}

int main() {

	freopen("A-large.in" , "r",stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	rep(t, 1, T+1){
		fill(digit, false);
		int n;
		cin >> n;
		if(n == 0){
			printf("Case #%d: INSOMNIA\n", t);
			continue;
		}
		int num = 0;
		int cnt = 1;
		while(true){
			num = cnt * n;
			markAsleep(num);
			if(isFallAsleep()){
				break;
			}
			cnt++;
		}
		printf("Case #%d: %d\n", t, num);
	}
	return 0;
}
