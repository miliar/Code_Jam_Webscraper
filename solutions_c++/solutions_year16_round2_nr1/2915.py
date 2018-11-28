#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main(){
	ifstream cin("A-large (2).in");
	ofstream cout("output.out");
	int t, a[26], i, o = 0;
	int numbers[10];
	string s;
	cin >> t;
	while (t--){
		o++;
		for (i = 0; i < 26; i++){
			a[i] = 0;
		}
		for (i = 0; i < 10; i++){
			numbers[i] = 0;
		}
		cin >> s;
		for (i = 0; i < s.length(); i++){
			a[s[i] - 'A']++;
		}
		numbers[0] = a['Z' - 'A'];
		a['E' - 'A'] -= a['Z' - 'A'];
		a['R' - 'A'] -= a['Z' - 'A'];
		a['O' - 'A'] -= a['Z' - 'A'];
		numbers[2] = a['W' - 'A'];
		a['T' - 'A'] -= a['W' - 'A'];
		a['O' - 'A'] -= a['W' - 'A'];
		numbers[4] = a['U' - 'A'];
		a['F' - 'A'] -= a['U' - 'A'];
		a['O' - 'A'] -= a['U' - 'A'];
		a['R' - 'A'] -= a['U' - 'A'];
		numbers[6] = a['X' - 'A'];
		a['S' - 'A'] -= a['X' - 'A'];
		a['I' - 'A'] -= a['X' - 'A'];
		numbers[8] = a['G' - 'A'];
		a['E' - 'A'] -= a['G' - 'A'];
		a['I' - 'A'] -= a['G' - 'A'];
		a['H' - 'A'] -= a['G' - 'A'];
		a['T' - 'A'] -= a['G' - 'A'];
		numbers[1] = a['O' - 'A'];
		a['N' - 'A'] -= a['O' - 'A'];
		a['E' - 'A'] -= a['O' - 'A'];
		numbers[3] = a['R' - 'A'];
		a['T' - 'A'] -= a['R' - 'A'];
		a['H' - 'A'] -= a['R' - 'A'];
		a['E' - 'A'] -= 2 * a['R' - 'A'];
		numbers[5] = a['F' - 'A'];
		a['I' - 'A'] -= a['F' - 'A'];
		a['V' - 'A'] -= a['F' - 'A'];
		a['E' - 'A'] -= a['F' - 'A'];
		numbers[7] = a['S' - 'A'];
		a['E' - 'A'] -= 2 * a['S' - 'A'];
		a['V' - 'A'] -= a['S' - 'A'];
		a['N' - 'A'] -= a['S' - 'A'];
		numbers[9] = a['I' - 'A'];
		cout << "Case #" << o << ": ";
		for (i = 0; i < 10; i++){
			while (numbers[i]--){
				cout << i;
			}
		}
		cout << endl;
	}
	return 0;
}