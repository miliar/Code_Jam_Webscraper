#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair
#define SZ(v) ((int)((v).size()))
#define LE(s) ((int)((s).length()))

string arr[10] = {
		"ZERO",
		"ONE",
		"TWO",
		"THREE",
		"FOUR",
		"FIVE",
		"SIX",
		"SEVEN",
		"EIGHT",
		"NINE"
};

int nb[10][26] = {{0}};
int present[26] = {0};
int cnt[10] = {0};
int T;
string str;

void init(){
	cin.sync_with_stdio(false);
	for (int i=0; i<10; i++){
		for (char e : arr[i]){
			nb[i][e - 'A']++;
		}
		/*for (int j=0; j<26; j++){
			if (nb[i][j] != 0){
				cout << "(" << (char)(j + 'A') << ", " << nb[i][j]<<")  ";
			}
		}
		cout << endl;*/
	}
	cin >> T;
}

void actualise(int number, char letter){
	cnt[number] = present[letter - 'A'];
	//cout << "discovered " << cnt[number] << "times digit  " <<number <<endl; 
	for (int i=0; i<26; i++){
		present[i] -= nb[number][i] * cnt[number];
	}
}
void show(){
	cout << endl << "-----------------------------------" << endl;
	for (int i=0; i<26; i++){
		if (present[i] != 0)
			cout << "\t" << (char)(i + 'A') << "  :  " << present[i] << endl;
	}
}

void res(){
	for (int i=0; i<26; i++){
		present[i] = 0;
	}
	for (int i=0; i<10; i++){
		cnt[i] = 0;
	}
	for (char e : str){
		present[e - 'A']++;
	}
	//show();
	actualise(0, 'Z');
	//show();
	actualise(2, 'W');
	//show();
	actualise(6, 'X');
	//show();
	actualise(8, 'G');
	//show();
	actualise(7, 'S');
	//show();
	actualise(5, 'V');
	//show();
	actualise(4, 'U');
	//show();
	actualise(3, 'R');
	//show();
	actualise(1, 'O');
	//show();
	actualise(9, 'I');
	//show();
	for (int i=0; i<10; i++){
		for (int j=0; j<cnt[i]; j++){
			cout << i;
		}
	}
}
	

int main(){
	init();
	for (int i=1; i<=T; i++){
		cin >> str;
		cout << "Case #"<<i<<": ";
		res();
		cout << endl;
	}
}	
