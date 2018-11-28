#include <iostream>
#include <cstring>
using namespace std;

const int N = 20;

int dist[1 << N];

int flip(int mask, int cnt){
	int aux = 0;
	for (int i = 1; i <= cnt; i++, mask >>= 1)
		aux = (aux << 1) ^ (mask & 1);
	return (mask << cnt) ^ aux ^ ( (1 << cnt) - 1 );
}

int fast(int n, int size){
	int ans = 0;
	bool e = false;
	for (int mask = 1 << N; mask; mask >>= 1)
		if ( !!(n & mask) != e ){
			e ^= 1;
			ans++;
		}
	return ans;
}

int fast_parse(char* s){
	int ans = 0;
	bool expect = true;
	for (int i = strlen(s) - 1; i >= 0; i--)
		if ( (s[i] == '+') != expect ){
			ans++;
			expect ^= 1;
		}
	return ans;
}

int main(){
/*
	queue<int> Q;
	Q.push(0);

	while ( !Q.empty() ){
		int x = Q.front();
		Q.pop();

		for (int i = 1; i <= N; i++){
			int y = flip(x, i);
			if ( y && !dist[y] ){
				dist[y] = 1 + dist[x];
				Q.push(y);
			}
		}
	}

	for (int i = 1; i < (1 << N); i++)
		if ( dist[i] != fast(i, N) )
			cout << i << ": " << dist[i] << " / " << fast(i, N) << '\n';
*/
	char s[102];
	int times;
	cin >> times;
	for (int i = 1; i <= times; i++){
		cin >> s;
		cout << "Case #" << i << ": " << fast_parse(s) << '\n';
	}
	return 0;
}
