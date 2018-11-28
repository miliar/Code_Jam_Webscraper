#include <iostream>
#include <string>
using namespace std;

int main(){
	int n;
	cin >> n;
	for(int i = 0; i < n; ++i){
		string ordre;
		cin >> ordre;
		char anterior = ordre[0];
		int canvis = 0;
		for(int j = 1; j < ordre.size();++j){
			if(anterior != ordre[j]){
				anterior = ordre[j];
				++canvis;
			}
		}
		if(ordre[ordre.size()-1] == '-') ++canvis;
		cout << "Case #" << i + 1 << ": " << canvis << endl;
	}
}