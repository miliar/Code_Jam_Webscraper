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

int getNbTest (ifstream & fin) {
    string line;
    getline (fin, line);
    int i, size = line . length (), result = line[0] - '0';
    for (i = 1; i < size; ++i) {
        result += (line[i] - '0');
        result *= 10;
    }
    return result;
}

double stringToDouble (string src) {
    return atof (src.c_str());
}

int main () {
	  ifstream fin ("B-large.in.txt");
	  ofstream fout ("output.txt");
    int nbCases = getNbTest (fin);
    int i;
    for (i = 0; i < nbCases; ++i) {
        vector<string> line = parse (fin);
        double C = stringToDouble (line[0]);
        double F = stringToDouble (line[1]);
        double X = stringToDouble (line[2]);
        double cookPerSecond = 2.0;
        double totalTime = 0.0;
        if (C / 2.0 < X / 2.0) {
            totalTime = 0.0;
            while ((X / cookPerSecond) > (C / cookPerSecond + X / (cookPerSecond+F))) {
                totalTime += (C / cookPerSecond);
                cookPerSecond += F;
            }
            totalTime += X / cookPerSecond;
        }
        else {
            totalTime = X / 2.0;
        }
        char aux[15];
        sprintf (aux, "%.7f", totalTime);
        fout << "Case #" << i+1 << ": " << aux << endl;
    }
	  fin . close ();
	  fout . close ();
    return 0;
}
