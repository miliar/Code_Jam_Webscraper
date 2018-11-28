#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;
int peopleNeeded(string input){
    string shynessList=input.substr(2);
    vector<int> everybody;
    int largestGap=0;
    int counter=0;
    for(int i=0; i<shynessList.length();i++){
        for(int q=0; q<shynessList[i]-'0'; q++){
            if(i-counter > largestGap){
                largestGap=i-counter;
            }
            counter++;
        }
    }
    return largestGap;
}

int main(int argv, char* arguements[])
{
    fstream input;
    input.open(arguements[1]);
    int lines;
    input >> lines;
    string throwAway;
    getline(input, throwAway);
    for(int i=0; i<lines; i++){
        string data;
        getline(input, data);
        cout << "Case #" << i+1 << ": " << peopleNeeded(data) << endl;
    }
    return 0;
}
