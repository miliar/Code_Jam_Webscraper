#include <iostream>
using namespace std;
int N[10];
int main(){
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	int TC,tc;
	cin >> TC;
	int num, i, j;
	for (tc = 1; tc <= TC;tc++){
		cin >> num;
		for (i = 0; i < 10; i++)
			N[i] = 0;
		if (num == 0){
			cout <<"Case #"<<tc<<": INSOMNIA" << endl;
			continue;
		}
		for (i = 1;; i++){
			int cur = num*i;
			while (cur){
				N[cur % 10] = 1;
				cur /= 10;
			}
			for (j = 0; j < 10; j++)
				if (!N[j])
					break;
			if (j == 10)
				break;				
		}
		cout << "Case #" << tc << ": "<< num*i << endl;
	}
	return 0;
}