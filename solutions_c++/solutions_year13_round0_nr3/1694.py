#include<stdio.h>
#include<vector>

using namespace std;

bool palindrome(long long n){
	long long a = n;
	long long p = 0;
	while(n){
		p *= 10;
		p += n%10;
		n /= 10;
	}
	return a == p;
}

int main(){
	int tc = 1, n;
	long long a, b;
	
	vector<long long> pals;
	long long int sq = 0, num = 1;
	while(sq <= 1e14 && sq >= 0){
		sq = num*num;
		if(palindrome(num) && palindrome(sq))
			pals.push_back(sq);
		num++;
	}

	for(scanf("%d", &n); n; n--){
		printf("Case #%d: ", tc++);
		scanf("%lld %lld", &a, &b);
		int indA = 0, indB = 0, ans = 0;
		for(int i = 0; i < pals.size(); i++){
			if(a >= pals[i]) indA = i;
			else break;
		}
		if(a==pals[indA]) ans++;
		for(int i = indA+1; i < pals.size(); i++){
			if(b >= pals[i]){
				ans++;
				indB = i;
			}
			else break;
		}
		printf("%d\n", ans);
	}
}
