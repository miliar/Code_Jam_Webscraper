using namespace std;

#include <iostream>
#include <fstream>
#include <vector>
#include <climits>

const int maxSize = 100;

vector<bool> convertSeq(char* seq) {
    int i=0;
    vector<bool> ret;
    while (seq[i] != '\0'){
        if (seq[i] == '+') {
            ret.push_back(true);
        } else {
            ret.push_back(false);
        }

        i++;
    }
    return ret;
}

int allTrue(vector<bool>& v) {
    for (int i = 0; i<v.size(); i++) {
        if (!v[i]) {
            return false;
        }
    }
    return true;
}

void turnI(vector<bool>& v, int till) {
    for (int i=0; i<=till; i++) {
        v[i] = !v[i];
    }
}

int best(vector<bool>& v) {
    int res = 0;

    for (int i=0; i<v.size()-1; i++) {
        if (v[i] != v[i+1]) {
            turnI(v, i);
            res++;
            i=0;
        }
    }

    if (v[0] == 0){
        return res+1;
    } else {
        return res;
    }

}

int main(int argc, char* argv[]) {

    fstream in;
    in.open(argv[1], fstream::in);
    fstream out;
    out.open("output.txt", fstream::out);
    int nTests;
    in >> nTests;

    for (int i=0; i<nTests; i++) {
        char seq[maxSize+1];
        in >> seq;
        vector<bool> v = convertSeq(seq);
        out << "Case #" << i+1 << ": " << best(v) << endl;
    }
    return 0;
}
