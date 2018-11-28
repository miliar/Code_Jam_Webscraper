#include<iostream>
#include<vector>

using namespace std;

int main(void){
	ios::sync_with_stdio(0);
	int t;
	cin >> t;
	for(int q=1; q<=t; q++){
		unsigned long long n;
		cin >> n;

		if (n == 0){
			cout << "Case #" << q << ": INSOMNIA\n";
			continue;
		}

		vector<bool> digit(10, false);
		int count = 0;
		for(int i=1;;i++){
			unsigned long long aux = i*n;
			while(aux != 0){
				if (!digit[aux%10]){
					digit[aux%10] = true;
					count++;
				}
				aux /= 10;
			}

			if(count == 10){
				cout << "Case #" << q << ": " << (i*n) << "\n";
				break;
			}
		}
	}
	return 0;
}