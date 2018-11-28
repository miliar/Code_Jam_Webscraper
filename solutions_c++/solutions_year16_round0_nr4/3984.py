#include <iostream>
#include <string>
using namespace std;
int K, C, S;
string solve(){
	cin >> K >> C >> S;
	string r;
	for(int i = 1; i <= K; i++)
		r += to_string(i) + " ";
	return r;
}
int main(int argc, char *argv[]){
	int T;
	cin >> T;
	for(int i = 0; i < T; i++)
		cout << "Case #" << i + 1 << ": " << solve() << endl;
}