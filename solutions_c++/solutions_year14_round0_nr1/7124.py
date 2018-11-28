#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <stdlib.h>
using namespace std;

vector<int> num_split(string line) {
    vector<int> out(0);
    string temp="";
    for(int i=0; i<line.size(); i++) {
        if(line[i]!= ' ') {
           temp=temp+line[i];
        } else {
            int aa=atoi(temp.c_str());
            out.push_back(aa);
            temp="";
        }
    }
    int aa=atoi(temp.c_str());
    out.push_back(aa);
    return out;
}

string func(vector<int> arrang1, vector<int> arrang2) {
    int matches=0;
    int number;
    for(int i=0; i<arrang1.size(); i++) {
        for(int j=0; j<arrang2.size(); j++) {
            if(arrang1[i]==arrang2[j]) {
                matches++;
                number=arrang1[i];
            }
        }
    }
    if(matches==1) {
        stringstream str;
        str<<number;
        return str.str();
    } else if(matches==0) {
        return "Volunteer cheated!";
    } else {
        return "Bad magician!";
    }
}

int main() {
    ofstream outputFile("output.txt");
    // outputFile << "writing to file";
    vector<string> out(0);
    std::ifstream myfile("A-small-attempt0.in");
    string line;
    getline(myfile, line);
    int cases=atoi(line.c_str());
    for(int ii=0; ii<cases; ii++) {
        getline(myfile, line);
        int line1=atoi(line.c_str());
        for(int i=0; i<line1;i++) {
            getline(myfile, line);
        }
        vector<int> arrang1=num_split(line);
        for(int i=line1; i<4;i++) {
            getline(myfile, line);
        }

        getline(myfile, line);
        int line2=atoi(line.c_str());
        for(int i=0; i<line2;i++) {
            getline(myfile, line);
        }
        vector<int> arrang2=num_split(line);
        for(int i=line2; i<4;i++) {
            getline(myfile, line);
        }

        out.push_back( func(arrang1, arrang2) );
    }
    for(int i=0; i<out.size(); i++) {
        outputFile<<"Case #"<<i+1<<": "<<out[i]<<endl;
    }
    return 0;
}
