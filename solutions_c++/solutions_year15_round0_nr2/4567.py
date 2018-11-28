using namespace std;
#include <iostream>
#include <vector>
#include <algorithm>

int t, res, n;
vector <int> vet;

int f(int pos, vector <int> temp);
bool cmp(int a, int b){
	return a > b;
}

int main(){

	cin >> t;
	for(int cont = 1;cont <= t;cont++){
		cin >> n;
		vet.clear();

		for(int i = 0;i < n;i++){
			int x; cin >> x; vet.push_back(x);
		}

		cout << "Case #" << cont << ": " << f(0, vet) << endl;
	}

	return 0;
}

int f(int pos, vector <int> temp){
	int mini;
	if(pos >= temp.size()){
		return 1000000;
	}
	sort(temp.begin(), temp.end(), cmp);

	mini = temp[pos];

	for(int i = 2;temp[pos]/i >= 2;i++){
		temp.push_back(temp[pos]/i+temp[pos]%i);
		temp.push_back(temp[pos]-(temp[pos]/i+temp[pos]%i));
		mini = min(mini, 1+f(pos+1, temp));
		temp.pop_back();
		temp.pop_back();
	}

	return mini;
}
