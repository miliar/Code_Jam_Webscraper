#include <iostream>
#include <algorithm>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cmath>
using namespace std;

#define N 10000

char s[N+20], sum[N+10], sumRev[N+10];
char x[4][4] = {'h', 'i', 'j', 'k',
				'i', 'H', 'k', 'J',
				'j', 'K', 'H', 'i',
				'k', 'j', 'I', 'H'};

void reverse(char &c){
	if (isupper(c)) c = tolower(c);
	else c = toupper(c);
}

bool solve(){
	int n, m;
	scanf("%d%d\n", &n, &m);
	scanf("%s", s);
	for (int i = n; i < n*m; ++i)
		s[i] = s[i%n];
	n *= m;
	s[n] = '\0';

	sum[0] = s[0];
	for (int i = 1; i < n; ++i){
		sum[i] = x[tolower(sum[i-1])-'h'][s[i]-'h'];
		if (isupper(sum[i-1])) reverse(sum[i]);
	}	

	sumRev[n-1] = s[n-1];
	for (int i = n-2; i >= 0; --i){
		sumRev[i] = x[s[i]-'h'][tolower(sumRev[i+1])-'h'];
		if (isupper(sumRev[i+1])) reverse(sumRev[i]);
	}

//	cout<<sum[n-1]<<endl;
	if (sum[n-1] != 'H') return false;

	for (int i = 0; i < n; ++i)
		if (sum[i] == 'i')
			for (int j = n - 1; j > i+1; --j)
				if (sumRev[j] == 'k')
					if (sum[j-1] == 'k') return true;

	return false;
}

int main(){
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; ++ test){
		printf("Case #%d: %s\n", test, solve()?"YES":"NO");
	}
	return 0;
}
