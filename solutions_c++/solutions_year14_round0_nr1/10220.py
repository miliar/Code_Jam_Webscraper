#include <iostream>
#include <vector>
#include <fstream>
#include <boost/algorithm/string.hpp>
#include <boost/lexical_cast.hpp>

using namespace std;
using namespace boost;

bool isFound = false;
string yourCard = "";
int counter = 0;

vector<string> returnVector(ifstream &file, const int &choice){
    vector<string> v;
    string str;
    for(int j = 1; j <= 4; j++){
        getline(file, str);
        if(j == choice)
            split(v, str, is_any_of(" "));

    }
    return v;
}

void findCard(vector<string> &original, vector<string> &shuffled, int &choice1, int &choice2, bool &isFound){
    for(int i = 0; i < original.size(); i++){
        for(int j = 0; j < shuffled.size(); j++){
            if(lexical_cast<int>(original[i]) == lexical_cast<int>(shuffled[j])){
                isFound = true;
                yourCard = original[i];
                counter++;
            }
        }
    }
}

int main(){
    string line = "";
    int cases = 0;
    vector<string> original;
    vector<string> shuffled;
    ifstream file("A-small-attempt2.in");
    ofstream file2("ASmallOutput.in");
    getline(file, line);
    cases = lexical_cast<int>(line);
    if(cases > 100 || cases < 1)
        return 0;
    for(int i = 1; i <= cases; i++){
        int choice1 = 0;
        int choice2 = 0;
        getline(file, line);
        choice1 = lexical_cast<int>(line);
        original = returnVector(file, choice1);
        getline(file, line);
        choice2 = lexical_cast<int>(line);
        shuffled = returnVector(file, choice2);
        findCard(original, shuffled, choice1, choice2, isFound);

        if(isFound == true && counter == 1)
            file2<<"Case #"<<i<<": "<<yourCard<<endl;
        else if (isFound == true && counter > 1)
            file2<<"Case #"<<i<<": Bad magician!"<<endl;
        else
            file2<<"Case #"<<i<<": Volunteer cheated!"<<endl;

        counter = 0;
    }
    return 0;
}
