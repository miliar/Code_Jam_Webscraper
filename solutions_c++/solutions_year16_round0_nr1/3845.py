#include <iostream>
#include <fstream>
#include <set>
using namespace std;

void solutionA(int a, int num){
	set<int> hashset;
	for (int i = 1; i <= 100; i++){
		int tmp = a * i;
		int result = tmp;
		while (tmp != 0){
			hashset.insert(tmp % 10);
			tmp = tmp / 10;
		}
		if (hashset.size() == 10){
			cout << "Case #" << num << ": " << result<<endl;
			return;
		}
	}
	cout << "Case #" << num << ": INSOMNIA"<<endl;
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	int a;
	int num = 1;
	while (cin >> a){
		solutionA(a, num);
		num++;
	}
	return 1;
}
