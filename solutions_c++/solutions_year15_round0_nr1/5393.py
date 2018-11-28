
#include <iostream>
#include <string>

using namespace std;

void logic(){
	string str;
	
	long long maxS;
	cin >> maxS;
	cin >> str;
	
	long long D[1010] = { 0 };
	long long cnt = 0;
	D[0] = str[0] - '0';
	for (int i = 1; i <= maxS; i++){
		if (D[i - 1] < i){
			cnt += i - D[i - 1];
			D[i] += i - D[i - 1];
		}
		D[i] += D[i - 1] + (str[i] - '0');
	}
	cout << cnt << endl;


	
}
int main(){

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int i = 1; i <= T;i++){
		cout << "Case #" << i << ": ";
		logic();
	}
}