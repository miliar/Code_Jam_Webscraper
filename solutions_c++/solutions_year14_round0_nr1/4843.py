#include <iostream>
#include <map>

using namespace std;


int main(){
	ios::sync_with_stdio(false);

	int testcases,answer,counter=1,aux,choosencard=-1;
	map<int,char> result;

	cin >> testcases;
	while(testcases-- > 0){
		cin >> answer;
		for(int i = 0 ; i < 4; i++){
			for(int j = 0 ; j < 4 ; j++){
				cin >> aux;
				if(i == answer-1){
					// may be the card
					result[aux] = 'm';
				}
			}
		}

		cin >> answer;
		for(int i = 0 ; i < 4; i++){
			for(int j = 0 ; j < 4 ; j++){
				cin >> aux;
				if(i == answer-1 && result[aux] == 'm'){
					// is the card
					result[aux] = 'y';
				}
			}
		}



		choosencard = -1;
		for(map<int,char>::iterator it = result.begin() ; it != result.end() ; it++){
			if(it->second == 'y' && choosencard == -1){
				choosencard = it->first;
			}else if(it->second == 'y' && choosencard != -1){
				choosencard = -2;
				break;
			}
		}

		cout << "Case #" << counter++ << ": ";
		if(choosencard == -2){
			cout << "Bad magician!\n";
		}else if(choosencard == -1){
			cout << "Volunteer cheated!\n";
		}else{
			cout << choosencard << endl;
		}

		result.clear();
	}



	return 0;
}