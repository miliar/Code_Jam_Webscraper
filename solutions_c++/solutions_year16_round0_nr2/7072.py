#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <list>
#include <climits>
#include <fstream>

using namespace std;

const char sm = '-';
const char sp = '+';

void flipCharacters(string &s){

    for(int i = 0; i < s.size(); i++){
        if(s[i] == sm)
            s[i] = sp;
        else
            s[i] = sm;
    }
}

int findFirstAlternationIndex(const string &s){

    int idx = string::npos;

    char prev = s[0];
    for(int i = 0; i < s.size(); i++){

        if(s[i] != prev){

            idx = i;
            break;
        }
    }

    return idx;
}

void maneuver(string &s){

    // find the fai ( first alternation index )

    int idx = findFirstAlternationIndex(s);

    if(idx == string::npos){

        flipCharacters(s);
        return;
    }

    string left = s.substr(0,idx);
    string right = s.substr(idx);
    if(s[0] == sm)
        flipCharacters(left);

    s = right + left;
}

int isReady(string &s){

    if(s.find('-') == string::npos)
        return 1;

    return 0;
}

int calculateManeuvers(string &s){

    int count = 0;

    while(!isReady(s)){

        maneuver(s);

        count++;
    }

    return count;
}

void getInput(vector<string> &nv){

    string line;
    int T = 0;
    int counter = 0;

    while ( std::getline(std::cin, line) && !line.empty() ){

        if(!T){ // read the T

            T = std::stoi(line);

        }else{

            if(counter < T){

                nv.push_back(line);

                counter++;
            }
        }
    }
}

int main(){

    vector<string> tc;

    getInput(tc);

    std::ofstream out("RevengeofthePancakes.out");
    std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

    for(int i = 0; i < tc.size(); i++){

        int num = calculateManeuvers(tc[i]);

        cout << "Case #" << i+1 << ": " << num << endl;
    }

    return 0;
}
