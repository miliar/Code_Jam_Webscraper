#include <iostream>
#include <map>
#include <set>
using namespace std;

int main(){
	int n;
	cin >> n;
	for(int i = 0; i < n; ++i){
		int m;
		cin >> m;
		cout << "Case #" << i + 1 << ": ";
		if(m == 0) cout << "INSOMNIA" << endl;
		else{
			set<int> falten;
			for(int j = 0; j < 10; ++j) falten.insert(j);
			uint contador = 0;
			while(falten.size() > 0){
				contador += m;
				int aux = contador;
				while(aux > 0){
					falten.erase(aux % 10);
					aux /= 10;
				}
			}
			cout << contador << endl;
		}
	}
}