#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <cmath>
using namespace std;

typedef long long ll;
typedef pair<int, int> PII;

int t, n;
pair<int, char> p[26];

int num(){
	int sum = 0;
	for(int i = 0;i < n;i++){
		sum += p[i].first;
	}
	return sum;
}

int max(){
	int m = 0;
	for(int i = 0;i < n;i++){
		if(p[m].first < p[i].first) m = i;
	}
	return m;
}

int main(void){
	cin >> t;
	for(int i = 0;i < t;i++){
		cout << "Case #" << i+1 << ": ";
		cin >> n;
		for(int j = 0;j < n;j++){
			cin >> p[j].first;
			p[j].second = (char)('A' + j);
		}
		while(num()){
			if(num() == 2){
				cout << p[max()].second;
				p[max()].first--;
				cout << p[max()].second;
				p[max()].first--;
				break;
			}
			int tmp = max();
			p[tmp].first--;
			int tmp2 = max();
			p[tmp2].first--;
			if(num()/2 >= p[max()].first){
				cout << p[tmp].second << p[tmp2].second;
			}else{
				cout << p[tmp].second;
				p[tmp2].first++;
			}
			cout << " ";
		}
		cout << endl;
	}

}
