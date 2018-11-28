#include <iostream>
#include <fstream>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

//#define DEBUG

#ifdef DEBUG
ifstream fin("A.in");
ofstream fout("A.out");
#else
ifstream fin("A2.in.txt");
ofstream fout("A2.out.txt");
#endif

int flip(int n)
{
    int res = 0;
    while(n > 0) {
	res = res*10 + n%10;
	n /= 10;
    }
    return res;
}

void solve()
{
    int N; fin >> N;
    int n = N, cnt = 1;
    while(true) {
	if(n == 1) break;
	if(n%10 != 0 && flip(n) < n) n = flip(n);
	else n--;
	cnt++;
    }
    fout << cnt << endl;
}

int dp[1000001];
int main()
{
    int T; fin >> T;
    for(int c = 1; c <= T; c++)
    {
	fout << "Case #" << c << ": ";
	//solve();
	int N; fin >> N;
	for(int i = 0; i <= N; i++) dp[i] = i;
	for(int i = 1; i <= N; i++) {
	    dp[i] = min<int>(dp[i], dp[i-1]+1);
	    dp[flip(i)] = min<int>(dp[flip(i)], dp[i]+1);
	}
	fout << dp[N] << endl;
	//for(int i = 0; i <= N; i++) cout << dp[i] << " ";
	//cout << endl;
    }

    return 0;
}
