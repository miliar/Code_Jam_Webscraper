#include <iostream>
#include <utility>
#include <math.h>
#include <bitset>
#include <vector>
#include <cstring>
#include <stdio.h>

using namespace std;

vector<int> sieve;

void generateSieve(int64_t upperBound) {
      int64_t upperBoundSquareRoot = (int64_t)sqrt((double)upperBound);
      bool *isComposite = new bool[upperBound + 1];
      memset(isComposite, 0, sizeof(bool) * (upperBound + 1));
      for (int64_t m = 2; m <= upperBoundSquareRoot; m++) {
            if (!isComposite[m]) {
                  //cout << m << " ";
                  for (int64_t k = m * m; k <= upperBound; k += m)
                        isComposite[k] = true;
            }
      }
      for (int64_t m = upperBoundSquareRoot; m <= upperBound; m++)
            if (!isComposite[m])
                  sieve.push_back(m);
      delete [] isComposite;
}



int64_t intRepFromBase(vector<int> &current, int base) {
	int64_t count = 0;
	for(int i = 0; i < current.size(); i++) {
	
		count += current[current.size() - 1 - i]*pow(base, i);
	
	}
	return count;
}

int64_t isPrime(int64_t check) {
	int64_t output = 1;
	
	//cout << check << endl;
	for(int64_t i = 2; i <= sqrt(check); i++) {
		if(check % i == 0) {
			output = i;
			return i;
		}	
	}
	return 0;
}

bool calculateFactors(vector<int> &current, int64_t* ARR) {
	//Do prime check in here
	int notPrime = 0;
	int64_t T_result [9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
	
	/*for(int j = 0; j < current.size(); j++) {
		cout << current[j];
	} cout << endl;
	*/
	for(int i = 0; i < 9; i++) {
		notPrime = isPrime(ARR[i]);
		
		
		T_result[i] = notPrime;
		if(notPrime == 0) { //Then it is prime and we move on
			return false;
		}
		
	} 
	
	
	
	for(int i = 0; i < current.size(); i++) {
			cout << current[i] << "";
	}	cout << " ";
	
	for(int i = 0; i < 9; i++) {
		//cout << ARR[i] << ":" << T_result[i] << " ";
		//cout << ARR[i]/T_result[i];
		cout << T_result[i];
		//printf("%1.2f", ARR[i]/T_result[i]);
		//cout << ARR[i] << ":" << T_result[i];
		//cout << ARR[i] << ":" << ARR[i]/T_result[i];
			if(i < 8) { cout << " "; }
		//cout << ARR[i] << " "; 
	} //cout << endl; 
	
	return true;
}

bool checkCoin(vector<int> &current) {
	int T_base [9] = {2, 3, 4, 5, 6, 7, 8, 9, 10};
	int64_t intRep = 0;
	int64_t *p;
	int64_t T_result [9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
	p = T_result;
	
	for(int i = 0; i < 9; i++) {
		intRep = intRepFromBase(current, T_base[i]);
		if(intRep == 0 || intRep == 1) { return false; }
		T_result[i] = intRep;
		//cout << intRep << endl;
//		if(isPrime(intRep) == true) { return false; }
		//cout << i << endl;
	}	
	return calculateFactors(current, p);
	//It must have passed to make it to this point
}

bool incrementBin(vector<int> &current) {
	int remainder = 1;
	int position = current.size()-1;
	while(remainder > 0) {
		if(current[position-1] == 0) {
			current[position-1] = 1;
			remainder = 0;
		} else if (position > 1 && current[position-1] == 1) {
			current[position-1] = 0;
			position--;
		} else if (position == 1) {
			cout << "\nMaximum reached, even though was guaranteed" << endl;
			//cout << "Everything is broken..." << endl;
			return false;
			break;
		}
	}
	return true;
}

int findNextCoin(vector<int> &current) {
	bool notEOI = true;

	while(checkCoin(current) == false && notEOI == true) {		
		notEOI = incrementBin(current);
			//cout << "done" << endl;
	}
	return 1;
}

int main() {
	int T;
	int N;
	int J;
	
	cin >> T;
	cin >> N; //Length
	cin >> J; //The number we want to find
	
	//cout << current_coin[1] << endl;
	
	//int size = 6;
	vector<int> current_coin (N, 0);
	current_coin.front() = 1;
	current_coin.back() = 1;
	
	//generateSieve(pow(10,6));
	/*for(int i = 0; i < sieve.size(); i++) {
			cout << sieve[i] << " ";
		}*/
	
	/*for(int i = 0; i < current_coin.size(); i++) {
			cout << current_coin[i] << " ";
		}	
		cout << endl;
	*/
	//return 1;
	
	int coinsFound = 0;
	//current_coin = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
	int next_coin = 0;
	
	//for(int i = 0; i < 10; ++i) {
	//incrementBin(current_coin);
	/*for(int j = 0; j < current_coin.size(); j++) {
		cout << current_coin[j] << " ";
	}*/
	/*}
	cout << endl;
	}*/
	
	cout << "Case #1:";	
	while(coinsFound < J) {
	cout << endl;
	/*for(int j = 0; j < current_coin.size(); j++) {
			cout << current_coin[j] << "";
	}	cout << endl;*/	
		next_coin = findNextCoin(current_coin);
		incrementBin(current_coin);
		coinsFound += next_coin;
	}
}