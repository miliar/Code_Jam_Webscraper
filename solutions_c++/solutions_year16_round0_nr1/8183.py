#include<iostream>
#include<vector>
#include<map>
using namespace std;

bool checkSheep(map<char,bool> sheeps){
	for(map<char,bool>::iterator it=sheeps.begin(); it!=sheeps.end(); ++it ){
		if(!it->second){	
			return false;
		}
	}
	return true;
}

void countsheep(int t, int n){
	if( n == 0 ){
		cout<< "Case #" + to_string(t+1) + ": INSOMNIA" <<endl;
		return;
	}

	map<char,bool> sheeps;
	for( int i=0; i<10; i++ ){
		sheeps[(char)(i+48)] = false;
	}

	int c=1;
	int nInt = n;
	string nStr = "";
	bool loop = false;
	do{
		nInt = n*c;
		c++;
		nStr = to_string(nInt);

		for(int j=0; j<nStr.length(); j++){
			if( !sheeps[nStr[j]] ){
				sheeps[nStr[j]] = true;
			}
		}

		//check
		loop = checkSheep(sheeps);

	} while(!loop);

	cout<< "Case #" + to_string(t+1) + ": " + to_string(nInt) <<endl;
}

int main(){
	int t;
	int n;

	cin >> t;
	for(int i=0; i<t; i++){
		cin >> n;
		countsheep(i, n);
	}

	return -1;
}


