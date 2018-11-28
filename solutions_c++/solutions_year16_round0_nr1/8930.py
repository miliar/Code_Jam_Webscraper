#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main(){
	int n;
	unordered_map<int, int> digs;
	int j=1;
	int inputs;
	cin >> inputs;
	while(inputs --){
		digs.clear();
		cin >> n;
		int i = 1;
		while(digs.size() < 10){
			int tmp = i*n;
			if(i>1 && tmp <= n){
				cout << "case #" << j << ": INSOMNIA\n";
				break;
			}
			while(tmp){
				digs[tmp%10] = tmp%10;
				tmp /= 10;
			}
			i++;
		}
		if (digs.size() == 10) cout << "case #"<<j <<": " << (i-1)*n << endl;
		j++;
	}
}
