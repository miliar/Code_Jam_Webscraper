#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

vector<int> convert(string audience){
    vector<int> vals;

    for (int i = 0; i < audience.size(); i++){
        if (audience[i] == '0')
            vals.push_back(0);
        else if (audience[i] == '1')
            vals.push_back(1);
        else if (audience[i] == '2')
            vals.push_back(2);
        else if (audience[i] == '3')
            vals.push_back(3);
        else if (audience[i] == '4')
            vals.push_back(4);
        else if (audience[i] == '5')
            vals.push_back(5);
        else if (audience[i] == '6')
            vals.push_back(6);
        else if (audience[i] == '7')
            vals.push_back(7);
        else if (audience[i] == '8')
            vals.push_back(8);
        else if (audience[i] == '9')
            vals.push_back(9);
    }

    return vals;
}


int solve(vector<int> vals){
    int friends;
    int standing;
    int people;
    friends = 0;
    standing = 0;
    people = 0;
    for (int i = 0; i < vals.size(); i++){
        people += vals[i];
    }

    standing += vals[0];

    for (int i = 1; i < vals.size(); i++){
        if (standing >= i){
            standing += vals[i];
        }

        else {
            friends += (i - standing);
            standing += (i-standing);
            standing += vals[i];
        }
    }

    return friends;
}

int main(void){
    int cases;
    string a;
    vector<int> vals;
    int s_max;
    ifstream fin("A-large.in");
    ofstream fout("A.out");
    fin >> cases;

    for (int i = 0; i < cases; i++){
        fin >> s_max;
        fin >> a;
        vals = convert(a);
        fout << "Case #" << i + 1 << ": ";
        fout << solve(vals) << endl;
    }

    return 0;
}
