#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <functional>
#include <algorithm>
#include <cmath>

using namespace std;

vector<string> parse (ifstream & fin) {
    string line, aux;
    getline (fin, line);
    vector<string> result;
    int i, size = line . length ();
    for (i = 0; i < size; ++i) {
        if (line[i] == ' ') {
            result . push_back (aux);
            aux = "";
            continue;
        }
        aux += line [i];
    }
    result . push_back (aux);
    return result;
}

int getInt (ifstream & fin) {
    string line;
    getline (fin, line);
    int result = atoi(line.c_str());
    return result;
}

int stringToInt (string s) {
    return (atoi(s.c_str()));
}

double stringToDouble (string src) {
    return atof (src.c_str());
}

int getMax (const vector<string> & vect) {
    int pos = 0, i, size = vect . size ();
    for (i = 0; i < size; ++i) {
        if (vect[i] . compare (vect[pos]) > 0) {
            pos = i;
        }
    }
    return pos;
}

int getMin (const vector<string> & vect) {
    int pos = 0, i, size = vect . size ();
    for (i = 0; i < size; ++i) {
        if (vect[i] . compare (vect[pos]) < 0) {
            pos = i;
        }
    }
    return pos;
}

int main () {
	  ifstream fin ("B-small-attempt0.in.txt");
	  ofstream fout ("output.txt");
    int nbCases = getInt (fin);
    int i;
    for (i = 0; i < nbCases; ++i) {
        fout << "Case #" << i+1 << ": ";
        vector<string> aux = parse (fin);
        int A = stringToInt (aux[0]);
        int B = stringToInt (aux[1]);
        int K = stringToInt (aux[2]);

        int result = 0;

        int j, k;
        for (j = 0; j < A; ++j) {
            for (k = 0; k < B; ++k) {
                if ((j&k) < K) {
                  ++result;
                }
            }
        }
        fout << result << endl;
    }
	  fin . close ();
	  fout . close ();
    return 0;
}
