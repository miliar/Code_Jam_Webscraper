#include <iostream>
#include <string>
using namespace std;

int main(int argc, char ** argv){
	int n;
	string list;
	char prev;
	int count;
	cin >> n;
	getline(cin, list);
	for(int i = 0; i < n; i++){
		getline(cin, list);
		//cerr << ":" << list << endl;
		count = 0;
		prev = list[0];
		if(list[list.size()-1] == '-') count++;
		for(int j = 0; j < list.size(); j++){
			//cerr << "Reading " << list[j] << endl;
			if(prev != list[j]){
				count++;
				prev = list[j];
			}
		}

		
		cout << "Case #" << i+1 << ": " << count << endl;
	}
}
