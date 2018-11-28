#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

typedef vector<char> ChVector;

char myshuffle(char c)
{
    if (c == '+') {
        return '-';
    } else {
        return '+';
    }
}

int getFlipCount(ChVector& v)
{
    int tcount = 0;

    while (count(v.begin(), v.end(), '+') != v.size()) {

        ChVector::iterator it = v.begin();
        while ((it != v.end()) && ((*it) != '-')) {
            it++;
        }
        if (distance(v.begin(), it) > 0) {
            transform(v.begin(), it, v.begin(), myshuffle);
            tcount++;
        }

        ChVector::reverse_iterator rit = v.rbegin();
        while((rit != v.rend()) && ((*rit) != '-')) {
            rit++;
        }
       
        //transform
        reverse(rit, v.rend());
        transform(rit, v.rend(), rit, myshuffle);
        tcount++;
    }
    return tcount;
}

int main()
{
    int T = 0;
    int rc = 0;
    vector <ChVector> inputs;

    cin >> T;
    cin.get();

    for (int i=0; i<T; i++) {
        string line, str;
        getline(cin, line);
        istringstream stream(line);
        stream >> str;
        ChVector v(str.begin(), str.end());
        inputs.push_back(v);
    }
 
    for (int j=0; j<T; j++) {
        rc = getFlipCount(inputs[j]);
        cout << "Case #" << j+1 << ": " << rc << endl;
    }

    return 0;
}
