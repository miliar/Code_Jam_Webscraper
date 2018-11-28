#include<iostream>
#include<string>
#include<sstream>
#include<list>
#include<math.h>
#include<limits.h>
#include<list>
#include<vector>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<algorithm>
#define MAX1 100001
#define BREAK_PRIME 200
using namespace std;
string num[10]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
int strCount[26];
bool isPrime[MAX1] = {true};
list<int> primes;
bool isPrimeNum(long num){
	long sqroot = sqrt(num);
	for(int i=2; i<=sqroot; i++){
		if(num %i == 0)
			return false;
	}
	return true;
}
void cachePrimes(){
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
void printTestCaseOutput(int i){
	cout << "Case #" << i <<": " << endl;
}

int countNumInStr(int number){
	string numStr = num[number];
	int count=0;
	bool flag = true;
	while(flag){
		for(int i=0; i<numStr.length();i++){
			if(strCount[numStr[i]-'A']-1 < 0){
				flag = false;
			}
		}
		if(flag){
			for(int i=0; i<numStr.length();i++){
				strCount[numStr[i]-'A']--;
			}
			count ++;
		}	
	}
	return count;
}
int main(){
	int T;
	int a[10];
	
	cin >> T;
	
	
	string str;
	for(int i=1; i<=T; i++){
		for(int j=0; j<10; j++){
			a[j] = 0;
		}
		for(int j=0; j<26; j++){
			strCount[j] = 0;
		}	
		cin >> str;
		//find the mmost lengthy ones first
		for(int j=0; j<str.length(); j++){
			strCount[str[j]-'A']++;
		}
		a[0] = countNumInStr(0);
		a[2] = countNumInStr(2);
		a[6] = countNumInStr(6);
		a[4] = countNumInStr(4);
		a[8] = countNumInStr(8);
		a[7] = countNumInStr(7);	
		a[3] = countNumInStr(3);
		a[5] = countNumInStr(5);
		a[9] = countNumInStr(9);
		a[1] = countNumInStr(1);
		
		string mb = "";
		for(int k=0; k<10; k++){
			if(a[k] > 0){
				for(int z=0; z<a[k]; z++){
					stringstream ss;
					ss << k;
					string kStr = ss.str();
					mb = mb + kStr; 
				}
			}
		}
		
		cout << "Case #" << i << ": " << mb << endl;
		
	}
	
	return 0;
}
