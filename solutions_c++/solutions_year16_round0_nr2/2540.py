#include<iostream>
#include<string>
using namespace std;
void flip(string& s, int lastIndex){
	for(int i=0; i<= lastIndex/2; i++){
		swap(s[i], s[lastIndex-i]);
	}
	for(int i=0; i <= lastIndex; i++){
		if(s[i] =='+'){
			s[i] = '-';
		}else if(s[i] == '-'){
			s[i] = '+';
		}
		
	}
}
void swap(char& ch1, char& ch2){
	char temp;
	temp = ch1;
	ch1 = ch2;
	ch2 = temp;
}
int findFirstOccurenceFromBehind(string& s, char ch){
	for(int i=s.size(); i >= 0 ; i--){
		if(s[i] == ch){
			return i;
		}
	}
	return -1;
}
int findLastIndexOfConsecutivePlus(string &s){
	for(int i=0; i < s.size(); i++){
		if(s[i] == '-')
			return i-1;
	}
	return s.size()-1;
}
int main(){
	string S; int T, noOfFlips;
	cin >> T;
	for(int i=1; i<=T; i++){
		cin >> S;
		noOfFlips = 0;
		int lastMinusIndex = findFirstOccurenceFromBehind(S, '-');
		while(lastMinusIndex != -1){
			if(S[0] == '-'){
				noOfFlips +=1;
				flip(S, lastMinusIndex);
			}else if(S[0] == '+'){
				//we need to first make the first character as -
				//to do it efficently get all the ++++ in beginning and make them flip ----. these all minuses will become ++++ in the next flip
				int lastIndexOfConsecutivePlus = findLastIndexOfConsecutivePlus(S);
				noOfFlips += 1;
				flip(S, lastIndexOfConsecutivePlus);
				noOfFlips += 1;
				flip(S, lastMinusIndex);
			}
			
			lastMinusIndex = findFirstOccurenceFromBehind(S, '-');
		}
		cout << "Case #" << i << ": " << noOfFlips << endl;
		//cout << S << endl;
		
	}
	return 0;
}


