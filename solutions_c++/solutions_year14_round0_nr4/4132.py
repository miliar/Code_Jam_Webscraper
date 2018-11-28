#include <iostream>
#include <fstream>
#include <string>
#include <vector>
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

int kenStrategie (const vector<string> & vect, const string & naomiChosen) {
    int pos = getMax(vect), i, size = vect . size ();
    int testMaxSup = getMax (vect);
    if (vect[testMaxSup] . compare (naomiChosen) < 0) {
        pos = getMin (vect);
    }
    else {
        for (i = 0; i < size; ++i) {
            if (vect[i] . compare (vect[pos]) < 0 && vect[i] . compare (naomiChosen) > 0) {
                pos = i;
            }
        }
    }
    return pos;
}

void testCheatString (string & cheat, vector<string> & cheatPool) {
    int i, size = cheatPool . size ();
    for (i = 0; i < size; ++i) {
        if (cheat == cheatPool[i]) {
            cheat += '1';
        }
    }
    cheatPool . push_back (cheat);
}

string naomiStrategie (const vector<string> & vect, bool nMinSupMinK, vector<string> & cheatPool) {
    string result;
    if (nMinSupMinK) {
        int firstMax = getMax (vect);

        result = vect[firstMax];
        result += "000001";
    }
    else {
        vector<string> aux = vect;
        int firstMax = getMax (aux);
        aux . erase (aux . begin() + firstMax);
        if (aux . size () == 0) {
            result = "0";
        }
        else {
            int secondMax = getMax (aux);

            result = aux[secondMax];
            result += "000001";
        }   
    }

    testCheatString (result, cheatPool);

    return result;
}

int war (const vector<string> & vect1, const vector<string> & vect2) {
    vector<string> naomi = vect1;
    vector<string> ken = vect2;

    int size = naomi . size (), i;
    int pointNaomie = 0;

    for (i = 0; i < size; ++i) {
        int n = getMin (naomi);
        string naomiChosen = naomi[n];
        naomi . erase (naomi . begin () + n);

        int k = kenStrategie (ken, naomiChosen);
        string kenChosen = ken[k];
        ken . erase (ken . begin () + k);

        if (naomiChosen . compare (kenChosen) > 0) {
            ++pointNaomie;
        }
    }
    return pointNaomie;
}

int deceitfulWar (const vector<string> & vect1, const vector<string> & vect2) {
    vector<string> naomi = vect1;
    vector<string> ken = vect2;

    int size = naomi . size (), i;
    int pointNaomie = 0;
    vector<string> cheatPool;

    for (i = 0; i < size; ++i) {

        int n = getMin (naomi);
        int minK = getMin (ken);

        bool test = naomi[n] . compare (ken[minK]) > 0;
        string naomiChosen = naomiStrategie (ken, test, cheatPool);
        naomi . erase (naomi . begin () + n);

        int k = kenStrategie (ken, naomiChosen);
        string kenChosen = ken[k];
        ken . erase (ken . begin () + k);

        if (naomiChosen . compare (kenChosen) > 0) {
            ++pointNaomie;
        }
    }
    return pointNaomie;
}

int main () {
	ifstream fin ("D-large.in.txt");
	ofstream fout ("output.txt");
    int nbCases = getInt (fin);
    int i;
    for (i = 0; i < nbCases; ++i) {
        int nbBlocks = getInt (fin);
        vector<string> naomiBlocks = parse (fin);
        vector<string> kenBlocks = parse (fin);

        fout << "Case #" << i+1 << ": ";

        if (naomiBlocks . size () == 1) {
            int resultWar = war (naomiBlocks, kenBlocks);
            fout << resultWar << " ";
            fout << resultWar << endl; 
        }
        else {
            fout << deceitfulWar (naomiBlocks, kenBlocks) << " ";
            fout << war (naomiBlocks, kenBlocks) << endl;
        }
    }
	fin . close ();
	fout . close ();
    return 0;
}
