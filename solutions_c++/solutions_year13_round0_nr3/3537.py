#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

const int MAXN = 200;
const int inf = 2000000;

bool is_palindorme(long long x){
	vector<long long> sk;
	while(x > 0)
		sk.push_back(x % 10),
		x /= 10;
	for(int i = 0; i < sk.size(); i++)
		if(sk[i] != sk[sk.size() - 1 - i])
			return false;
	return true;
	}

long long make_palindrome(int x, bool middle, int middlenum){
	vector<long long> sk;
	while(x > 0)
		sk.push_back(x % 10),
		x /= 10;
	
	long long answ = 0;
	
	for(int i = sk.size()-1; i >= 0; i--)
		answ *= 10, answ += sk[i];
	
	if(middle)
		answ *= 10,
		answ += middlenum;
	
	for(int i = 0; i < sk.size(); i++)
		answ *= 10,
		answ += sk[i];
	
	return answ;
	};

vector<long long> visi;

void solve(long long x){
	if(is_palindorme(x*x))
		visi.push_back(x*x);
			//~ printf("%lld %lld\n", x, x*x);
	}

int main(){
	
	int gen;
	for(int i = 0; i < 10000; i++)
		for(int j = 0; j <= 1; j++)
			if(j == 1)
				for(int k = 0; k <= 9; k++)
					solve(make_palindrome(i, j, k));
			else
				solve(make_palindrome(i, j, 0));
		
	int testcases;
	scanf("%d", &testcases);
	
	for(int testcase = 0; testcase < testcases; testcase++){
		int A, B;
		int cnt = 0;
		scanf("%d%d", &A, &B);
		for(int i = 0; i < visi.size(); i++)
			if(A <= visi[i] && visi[i] <= B)
				cnt++;
		printf("Case #%d: %d\n", testcase + 1, cnt);
		}
	
	
	return 0;
}
