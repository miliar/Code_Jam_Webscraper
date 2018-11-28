#include <iostream>
#include <string>
using namespace std;
const int MAXN = 1e6;
int T;
int N;
int dgt[MAXN];
int digits(long long s){
	int a = s / MAXN;
	int b = s % MAXN;
	return ((a > 0 && b < MAXN / 10) ? 1 : 0) | dgt[a] | dgt[b];
}
string solve(){
	cin >> N;
	if(N == 0)
		return "INSOMNIA";
	long long i = N;
	for(int r = 0; r != (1 << 10) - 1; i += N){
		r |= digits(i);
	}
	return to_string(i - N);
}
int main(int argc, char *argv[]){
	cin >> T;
	for(int i = 1; i < MAXN; i++)
		dgt[i] = dgt[i / 10] | (1 << (i % 10));
	for(int i = 0; i < T; i++)
		cout << "Case #" << i + 1 << ": " << solve() << endl;
}