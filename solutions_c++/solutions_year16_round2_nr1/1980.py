#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <string>
#include <algorithm>
#include <iostream>
#include <math.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int main(){
	int TC;
	cin >> TC;
	for(int c = 1; c <= TC; c++){
		string str;
		cin >> str;
		map<char,int> tabla;
		vector<int> vec;
	
		for(int i = 'A'; i <= 'Z'; i++){
			tabla[i] = 0;
		}

		for(int i = 0; i < str.size(); i++){
			if(tabla.find(str[i]) == tabla.end())
				tabla[str[i]] = 1;
			else
				tabla[str[i]]++;
		}
		
		// 0 ZERO
		if(tabla.find('Z') != tabla.end() && tabla['Z'] > 0){
			tabla['E'] -= tabla['Z'];
			tabla['R'] -= tabla['Z'];
			tabla['O'] -= tabla['Z'];
			for(int i = 0; i < tabla['Z'] ; i++) vec.push_back(0);
			tabla['Z'] = 0;
		}

		// 2 TWO
		if(tabla.find('W') != tabla.end() && tabla['W'] > 0){
			tabla['T'] -= tabla['W'];
			tabla['O'] -= tabla['W'];
			for(int i = 0; i < tabla['W'] ; i++) vec.push_back(2);
			tabla['W'] = 0;
		}

		// 6 SIX
		if(tabla.find('X') != tabla.end() && tabla['X'] > 0){
			tabla['S'] -= tabla['X'];
			tabla['I'] -= tabla['X'];
			for(int i = 0; i < tabla['X'] ; i++) vec.push_back(6);
			tabla['X'] = 0;
		}

		// 7 SEVEN
		if(tabla.find('S') != tabla.end() && tabla['S'] > 0){
			tabla['E'] -= tabla['S'];
			tabla['V'] -= tabla['S'];
			tabla['N'] -= tabla['S'];
			for(int i = 0; i < tabla['S'] ; i++) vec.push_back(7);
			tabla['S'] = 0;
		}

		// 5 FIVE
		if(tabla.find('V') != tabla.end() && tabla['V'] > 0){
			tabla['F'] -= tabla['V'];
			tabla['I'] -= tabla['V'];
			tabla['E'] -= tabla['V'];
			for(int i = 0; i < tabla['V'] ; i++) vec.push_back(5);
			tabla['V'] = 0;
		}

		// 4 FOUR
		if(tabla.find('F') != tabla.end() && tabla['F'] > 0){
			tabla['O'] -= tabla['F'];
			tabla['U'] -= tabla['F'];
			tabla['R'] -= tabla['F'];
			for(int i = 0; i < tabla['F']; i++) vec.push_back(4);
			tabla['F'] = 0;
		}

		// 3 THREE
		if(tabla.find('R') != tabla.end() && tabla['R'] > 0){
			tabla['T'] -= tabla['R'];
			tabla['H'] -= tabla['R'];
			tabla['E'] -= tabla['R'];
			for(int i = 0; i < tabla['R']; i++) vec.push_back(3);
			tabla['R'] = 0;
		}

		// 8 EIGHT
		if(tabla.find('H') != tabla.end() && tabla['H'] > 0){
			tabla['E'] -= tabla['H'];
			tabla['I'] -= tabla['H'];
			tabla['G'] -= tabla['H'];
			tabla['T'] -= tabla['H'];
			for(int i = 0; i < tabla['H']; i++) vec.push_back(8);
			tabla['H'] = 0;
		}

		// 1 ONE
		if(tabla.find('O') != tabla.end() && tabla['O'] > 0){
			tabla['N'] -= tabla['O'];
			tabla['E'] -= tabla['O'];
			for(int i = 0; i < tabla['O'] ; i++) vec.push_back(1);
			tabla['O'] = 0;
		}

		for(int i = 0; i < tabla['N']/2 ; i++) vec.push_back(9);

		sort(vec.begin(), vec.end());
		string q = "";
		for(int i = 0; i < vec.size(); i++) q += ('0' + vec[i]);
		cout << "Case #" << c << ": " << q << endl;

	}
}
