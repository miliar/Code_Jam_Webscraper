#include <iostream>
#include <fstream>
#include <cstring>
#include <sstream>
#include <algorithm>
using namespace std;

bool fair(long x){
	string n;
	stringstream ss(n);

	ss << x;
	n = ss.str();

	for(int i=0; i<n.length(); i++){
		if(n[i] != n[n.length()-1-i]){
			return false;
		}
	}
	
	return true;
}

long fairSquare(){
	long A,B;
	cin >> A >> B;

	long s = sqrt((long double)A);
	if(sqrt((long double)A) - s > 0){
		s++;
	}
	long e = sqrt((long double)B);

	long count = 0;
	for(long i=s; i<=e; i++){
		if(fair(i)){
			if(fair(i*i)){
				count++;
			}
		}
	}

	return count;
}

int main(){
	ifstream input("C-small-attempt0.in");
	cin.rdbuf(input.rdbuf());

	ofstream output("small.txt");
	cout.rdbuf(output.rdbuf());
	
	int T;
	cin >> T;

	for(int i=0; i<T; i++){
		cout << "Case #" << i+1 << ": " << fairSquare() << endl;
	}
	
	return 0;
}