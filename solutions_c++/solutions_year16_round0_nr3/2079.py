#include<iostream>
#include<list>
#include<math.h>
#define MAX1 100001
#define BREAK_PRIME 200
using namespace std;
bool isPrime[MAX1] = {true};
list<int> primes;

void cache(){
	for(int i=0; i<MAX1; i++){
		isPrime[i] = true;
	}
	for(int i= 2; i< MAX1; i++){
		if(isPrime[i]){
			for(int j = 2 ; i*j < MAX1; j++){
				isPrime[i*j] = false;
			}	
		}
		
	}
	
	for(int i=2; i< MAX1; i++){
		if(isPrime[i]){
			primes.push_back(i);
			//cout << i << " ";
		}
	}
}
int findRemainder(string& notation, int base, int devisor){
	int remainder = 0;
	int size = notation.size();
	int value = 1;
	for(int i=0; i<size; i++){
		if(notation[size-1-i] == '1'){
			remainder = (remainder + value)% devisor;
		}
		value = (value * base) % devisor;
	}
	return remainder;
}
int findFirstDevisor(string& notation, int base){
	int i=0;
	for (list<int>::iterator it = primes.begin(); it != primes.end(); it++){
		i++;
		int primeNumber = *it;
		//cout << primeNumber << endl;
		if(findRemainder(notation, base, primeNumber) == 0){
			return primeNumber;
		}
		if(i == BREAK_PRIME){
			break;
		}
	}
	return -1;
}
string getRequiredNumberOfSomeBits(int N, int num){
	string str = "1";
	string numBit = "";
	while(num > 0){
		int rem = num % 2;
		numBit = rem == 1 ? "1" + numBit : "0" + numBit;
		num = num /2;
	}
	int numBitSize = numBit.size();
	for(int i=0; i < N-2-numBitSize; i++){
		numBit = "0" + numBit;
	}
	
	str = str + numBit;
	
	str = str + "1";
	return str;
}
int main(){
	int T, N, J;
	cache();
	//cout << endl << "size: " << primes.size() << endl;
	//cout << getRequiredNumberOfSomeBits(6, 0) << endl;
	//string notation = getRequiredNumberOfSomeBits(4, 0);
	//cout << endl << findRemainder(notation, 10, 11) << endl;
	
	/*cout << findFirstDevisor(notation, 2);
	cout << findFirstDevisor(notation, 3);
	cout << findFirstDevisor(notation, 4);
	cout << findFirstDevisor(notation, 5);
	cout << findFirstDevisor(notation, 6);
	cout << findFirstDevisor(notation, 7);
	cout << findFirstDevisor(notation, 8);
	cout << findFirstDevisor(notation, 9);
	cout << findFirstDevisor(notation, 10);*/
	
	//cout << getRequiredNumberOfSomeBits(4, 1) << endl;
	//cout << getRequiredNumberOfSomeBits(4, 2) << endl;
	//cout << getRequiredNumberOfSomeBits(4, 3) << endl;	
	cin >> T;
	list<int> devisorList;
	
	int primeFlag = 0;
	for(int i=1; i<=T; i++){
		cin >> N >> J;
		int foundJams = 0;
		cout << "Case #" << i <<": " << endl;
		for(int y=0; y<pow(2,N-2); y++){
			devisorList.clear();
			primeFlag = 0;
			string notation = getRequiredNumberOfSomeBits(N, y);
			
			for(int base=2; base<=10; base++){
				int firstDevisor = findFirstDevisor(notation,base);
				if(firstDevisor == -1){	
					//its a prime no need to print it.
					primeFlag = 1;
					break;
				}else{
					devisorList.push_back(firstDevisor);
				}
			}
			if(!primeFlag){
				foundJams++;
				cout << notation << " ";
				for (list<int>::iterator it = devisorList.begin(); it != devisorList.end(); it++){
					cout << *it << " ";
				}
				cout << endl;
					
			}
			if(foundJams == J){
				break;
			}
			
		}
	}
	return 0;
}
