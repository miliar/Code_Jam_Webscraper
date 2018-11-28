#include <iostream>
#include <fstream>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <math.h>
#include <queue>
//#include <utility>
using namespace std;

long long consonants(){
	string name;
	int n;
	cin >> name;
	cin >> n;
	//n = name[name.length()-1] - '0';
	//name[name.length()-2] = '\0';
	//name.erase(name.length()-2,string::npos);

	char v[] = {'a','e','i','o','u'};
	long long *isc = new long long[name.length()];
	for(int i=0; i<name.length(); i++){
		isc[i] = 1;
		for(int j=0; j<5; j++){
			if(name[i] == v[j]){
				isc[i] = 0;
			}
		}
	}

	long long count = 0;
	long long value = 0;
	for(int i=0; i<name.length()-n+1; i++){
		count = 0;
		for(int j=i; j<name.length(); j++){
			if(isc[j]){
				count++;
			}else{
				count = 0;
			}
			if(count >= n){
				value += name.length()-j;
				break;
			}
		}
	}
	
	return value;
}

int main(){
	ifstream input("A-small-attempt0.in");
	cin.rdbuf(input.rdbuf());

	ofstream output("small.txt");
	cout.rdbuf(output.rdbuf());
	
	int T;
	cin >> T;
	string nouse;
	getline(cin,nouse);

	for(int i=0; i<T; i++){
		cout << "Case #" << i+1 << ": " << consonants() << endl;
	}
	
	return 0;
}