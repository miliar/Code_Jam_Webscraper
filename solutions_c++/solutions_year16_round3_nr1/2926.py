#include <iostream>
#include <vector>
#include <string>

using namespace std;

//Political parties whose names are letters of the alphabet
//remove 1 or 2 senators at a time
//While removing, avoid leaving inside the senate a majority of senators of a single party
//
vector<char> vec[1001];


int main(int argc, char *argv[]){
	int I, T, N, i, j, p, hi;
	char aux;
	cin >> T;
	
	for(I = 0; I < T; I++){
		hi = 0;
		cin >> N;
		for(i = 0; i < N; i++){
			cin >> p;
			if(hi < p) hi = p;
			vec[p].push_back(i);	//add 65 later
		}
		
		cout << "Case #" << I+1 << ": ";
		
		string mystr;

		for(i = hi; i > 0; i--){
			if(vec[i].size() == 0) continue; //There are no parties with 'hi' senators inside
			for(j = 0; j < vec[i].size(); j++){
				
				if(i == 1 && j == 0 && mystr.size() == 0){
					if(vec[i].size()%2 == 1){
						aux = (char) 65+vec[i][j];
						cout << aux << " ";
						continue;
					}
				}

				mystr.push_back((char) 65+vec[i][j]);
				vec[i-1].push_back(vec[i][j]);	//Passes current party to next size
				if(mystr.size() == 2){
					cout << mystr << " ";
					mystr.clear();
				}
			}
			vec[i].clear();
		}
		if(mystr.size() == 1) cout << mystr;
		cout << endl;
		vec[0].clear();
	}

	return 0;
}
