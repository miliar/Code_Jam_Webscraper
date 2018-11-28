#include <iostream>
#include <string>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <utility>
using namespace std;

int length = 0;
int total = 0;
char *buffer;

typedef pair<int, pair<char, pair<char, bool> > > key;

map<key, bool> memoire;



void compute(const char first, const char second, char &out, bool &negatif);
bool search(int position, int positionG, char searched, char last, bool negatif);

bool searchMap(int position, int positionG, char searched, char last, bool negatif) {

	key k = make_pair(positionG, make_pair(searched, make_pair(last, negatif)));
	map<key, bool>::iterator it = memoire.find(k);

	if (it == memoire.end()) {
		bool retour = search(position,positionG,searched,last, negatif);
		memoire[k] = retour;
		return retour;
	} else {
		return memoire[k];
	}
}

bool search(int position, int positionG, char searched, char last, bool negatif) {

	if (positionG >= total) {
		return false;
	}

	if (position >= length) {
		position = 0;
	}

	char current;

	/* Pas de caractere avant ou utiliser pour multiplication*/
	if (last == 0) {
		current = buffer[position];
		//cout << "(";
	} else {
		compute(last, buffer[position], current, negatif);
		/*cout << "(";
		if (negatif) cout << "-";
		cout << last << " * " << buffer[position] << " = ";*/
	}


	/*if (negatif) cout << "-";
	cout << current << " )";
	cout << endl;*/

	// Traitement
	bool retour = false;
	position++;
	positionG++;

	if(current == searched && !negatif) {
		switch(current) {
			case 'i':
				retour = searchMap(position, positionG, 'j', 0, false);
				break;
			case 'j':
				retour = searchMap(position, positionG, 'k', 0, false);
				break;
			case 'k':
				//cout << " Trouver " << positionG << " / " << total << endl;
				retour = (positionG == total);
				break;
		}

		
	} 
	
	retour = retour || searchMap(position, positionG, searched, current, negatif);
	

	

	return retour;
}


bool solve() {
	int repeat;

    cin >> length >> repeat;
    total = length * repeat;

   	buffer = (char*)malloc(10000 * sizeof(char));
    scanf("%s", buffer);

    memoire.clear();

    //cout << "read : " << length << endl;
    bool res = search(0, 0, 'i', 0, false);
    //cout << endl;

    free(buffer);

    return res;
}


int main () {

	int t = 0;
    cin >> t;

    bool res;

    for (int i = 0; i < t; ++i) {
        res = solve();
        cout << "Case #" << (i+1) << ": "; 
        if (res) cout << "YES" << '\n';
        else cout << "NO" << '\n';         
    }

}

void compute(const char first, const char second, char &out, bool &negatif) {
 

   	if (first == second) {
   		out = '1';
   		negatif = !negatif;
   		return;
   	} else if (first == '1') {
   		out = second;
   		return;
   	} else if (second == '1') {
   		out = first;
   		return;
   	}

   	switch(first) {
   		case 'i':
   			switch(second) {
   				case 'j':
   					out = 'k';
   					break;
				case 'k':
					out = 'j';
					negatif = !negatif;
					break;
				default:
					break;
   			}
   			break;
		case 'j':
			switch(second) {
   				case 'i':
   					out = 'k';
   					negatif = !negatif;
   					break;
				case 'k':
					out = 'i';
					break;
				default:
					break;
   			}
			break;
		case 'k':
			switch(second) {
   				case 'i':
   					out = 'j';
   					break;
				case 'j':
					out = 'i';
					negatif = !negatif;
					break;
				default:
					break;
   			}
			break;
   	}

    
}