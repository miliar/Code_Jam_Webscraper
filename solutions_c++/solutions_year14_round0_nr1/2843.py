#include <cstdio>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;



int counter = 0;
ifstream inFile("C:/tmp/file.in");
ofstream outFile("C:/tmp/file.out");
void make() {

    string str;
    int pos, n;
    vector<int> v1,v2;


    inFile >> pos; inFile.ignore();
    for(int i = 1; i < pos; i++)
        getline(inFile, str);

    for(int i = 0; i < 4; i++) {
        inFile >> n;
        v1.push_back(n);
    }
    inFile.ignore();

    for(int i = pos; i < 4; i++)
        getline(inFile, str);

    inFile >> pos; inFile.ignore();
    for(int i = 1; i < pos; i++)
        getline(inFile, str);

    for(int i = 0; i < 4; i++) {
        inFile >> n;
        if(find(v1.begin(), v1.end(), n) != v1.end())
            v2.push_back(n);
    }
    inFile.ignore();

    for(int i = pos; i < 4; i++)
        getline(inFile, str);


    outFile  << "Case #" << ++counter << ": ";
    if(v2.empty())
        outFile << "Volunteer cheated!";
    else if(v2.size() != 1)
        outFile << "Bad magician!";
    else
        outFile << v2.at(0);
    outFile << endl;
    return;
}

int main() {

    int t; inFile >> t;
    inFile.ignore();
    while(t--) {
        make();
    }
    return 0;
}
