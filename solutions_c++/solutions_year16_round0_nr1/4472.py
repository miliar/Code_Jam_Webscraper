#include <iostream>
#include <utility>
#include <math.h>

using namespace std;

pair<int, int> getDivisor(pair<int, int> S){
	int N = S.first;
	int divisor = S.second;
	
	while(N % 10 == 0) {
		divisor++;
		N/=10;
	}
	S.first = N;
	S.second = divisor;
	
	return S;
}

int getDigits(int N, int tracker) {
	int LSB;
	
	while(N != 0) {
		LSB = N % 10;
		//cout << N << " " << LSB << endl;
		//We check if that bit is set in tracker
		if(tracker/((int)pow(10, LSB))%10 == 0) {
			tracker += pow(10, LSB);
		}
	//cout << LSB << " " << (int)pow(10,LSB) << " " << tracker << endl;
		N/=10;
	}
	return tracker;
}

int checkZero(int divisor, int tracker) {
	return (divisor > 0 && tracker %10 == 0)?1:0;
}

int loop(int N) {
	int tracker = 0;
	
	pair<int, int> valDiv;
	valDiv.first = N; //N
	valDiv.second = 0; //Divisor
	
	tracker += getDigits(N, tracker);
	tracker += checkZero(valDiv.second, tracker);
	
	//valDiv = getDivisor(valDiv);
	int compN = valDiv.first;
	// At this point we have the 'compressed' N and multiplier stored.
	// This was done because 200 has the same 'sequence' as 20, or 2.
	// However, we note that this removes the 0 from our tracker...
	//  so we just add this here...
	
	while(tracker != 1111111111) {
		tracker = getDigits(valDiv.first, tracker);
	//cout << "TRACK " << tracker << " " << valDiv.first << " " << valDiv.second << " " << valDiv.first*valDiv.second << endl;
		
		//We do a quick update...
		if(tracker != 1111111111) {
			valDiv.first = valDiv.first + compN;
			//valDiv = getDivisor(valDiv);
		}
		tracker += checkZero(valDiv.second, tracker);
	}
	
	if(valDiv.second > 0) {
		return valDiv.first * (10*valDiv.second);
	} else {
		return valDiv.first;
	}
}

int main() {
	int T;
	int N;
	int result;
	
	cin >> T;
	
	for(int i = 0; i < T; i++) {
		cin >> N;
		
		if(N > 0) {
			cout <<	"Case #" << i+1 << ": " << loop(N) << endl;
		} else {
		  cout <<	"Case #" << i+1 << ": INSOMNIA" << endl;
		}
		
		//loop(N);
		//result = loop(N);
		//cout << result;
		//cout <<	"Case #" << i+1 << ": " << result << endl;
	}
}