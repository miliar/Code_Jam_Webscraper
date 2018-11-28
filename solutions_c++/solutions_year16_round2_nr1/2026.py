#include <iostream>

using namespace std;

int used[26];
int count[10];

void reset(){
	for (int i = 0; i < 26; i++)
		used[i] = 0;
	for (int i = 0; i < 10; i++){
		count[i] = 0;
	}
}

void removeLetter(char L){
	used[L-'A']--;
}

void removeZero(){ // gets rid of Z
	used['Z'-'A']--;
	used['E'-'A']--;
	used['R'-'A']--;
	used['O'-'A']--;
	count[0]++;
}
void removeEight(){ // gets rid of G
	used['E'-'A']--;
	used['I'-'A']--;
	removeLetter('G');
	removeLetter('H');
	removeLetter('T');
	count[8]++;
}

void removeThree(){ // based off H after Eight is fully removed
	removeLetter('T');
	removeLetter('H');
	removeLetter('R');
	removeLetter('E');
	removeLetter('E');
	count[3]++;
}
void removeSix(){ // gets rid of X
	removeLetter('S');
	removeLetter('I');
	removeLetter('X');
	count[6]++;
}

void removeSeven(){ // based on S after removeSix
	removeLetter('S');
	removeLetter('E');
	removeLetter('V');
	removeLetter('E');
	removeLetter('N');
	count[7]++;
}

void removeTwo(){ // gets rid of W
	removeLetter('T');
	removeLetter('W');
	removeLetter('O');
	count[2]++;
}

void removeFour(){ // gets rid based off U
	removeLetter('F');
	removeLetter('O');
	removeLetter('U');
	removeLetter('R');
	count[4]++;
}

void removeFive() {// gets rid based off F after removeFour
	removeLetter('F');
	removeLetter('I');
	removeLetter('V');
	removeLetter('E');
	count[5]++;
}

void removeOne() { // based off of O after removeTwo
	removeLetter('O');
	removeLetter('N');
	removeLetter('E');
	count[1]++;
}

void removeNine(){ // based off N after one and seven are done
	removeLetter('N');
	removeLetter('I');
	removeLetter('N');
	removeLetter('E');
	count[9]++;
}

void fillUsed(string S){
	for (int i = 0; i < S.length(); i++){
		used[S[i]-'A']++;
	}
}

int main(){
int cases;
cin >> cases; 
    string S;
    for (int i = 0; i < cases; i++){
    	reset();
    	cin >> S;
    	fillUsed(S);
    	while(used['Z'-'A'])removeZero();
    	while(used['G'-'A'])removeEight();
    	while(used['X'-'A'])removeSix();
    	while(used['H'-'A'])removeThree();
    	while(used['S'-'A'])removeSeven();
    	while(used['W'-'A'])removeTwo();
    	while(used['U'-'A'])removeFour();
    	while(used['F'-'A'])removeFive();
    	while(used['O'-'A'])removeOne();
    	while(used['N'-'A'])removeNine();

    	cout << "Case #" << i+1 << ": ";
    	for (int i = 0; i < 10; i++){
    		while(count[i]--) cout << i;
    	}
    	cout << endl;

    }


}
