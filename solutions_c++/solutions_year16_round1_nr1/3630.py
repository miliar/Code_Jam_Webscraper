#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

void printLastWord(int round, vector<char> v){

    cout << "Case #" << round << ": ";
    for(int i = 0; i < v.size(); i++){

        cout << v[i];
    }

    cout << endl;
}

void playRound(int round, vector<char> &v){

    vector<char> helper;
    helper.push_back(v[0]);

    for(int i = 1; i < v.size(); i++){

        char c = v[i];

        if(c <= helper[helper.size()-1])
            helper.push_back(c);
        else if (c < helper[0])
            helper.push_back(c);
        else
            helper.insert(helper.begin(),c);
    }

    printLastWord(round,helper);
}

void startPlay(vector<vector<char> > &v){


    for(int i = 0; i < v.size(); i++){

        vector<char> cv = v[i];

        playRound(i+1,cv);
    }
}

int getInput(vector<vector<char> > &v){

    string line;

    int a_size = 0;
//    unsigned int a_item = 0;

    while (true) {

        getline(cin, line);

        if (line.empty()) {

            break;
        }

        if(!a_size){

            a_size = stoi(line);

        }else{

            vector<char> cv;
            for(int i = 0; i < line.size(); i++){

                cv.push_back(line[i]);
            }

            v.push_back(cv);

            if(v.size()==a_size)
                break;
        }
    }

    return a_size;
}

int main() {

    vector<vector<char> > v;
    int a_size = getInput(v);

    std::ofstream out("The Last Word.out");
    std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

    if(a_size)
        startPlay(v);

    return 0;
}
