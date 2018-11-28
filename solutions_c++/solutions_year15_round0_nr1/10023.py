#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include<string>
#include<fstream>
#include<cstdio>
#include<map>
#include <cctype>
#include <sstream>
#include<cmath>
#include<math.h>
#include<stdlib.h>
#include<stdio.h>
#include<string.h>

using namespace std;

class standing {
    public:
        int getStart();
        int readFile();
        int clapping();
        int writeFile();
    private:
        vector<vector<int> > shyness;
        vector<int> answer;
        int test_count;

};

int standing::getStart() {
    test_count=0;
    readFile();
    clapping();
    writeFile();
}

int standing::readFile() {
    ifstream inputFile("A-small-attempt0.in",ios::in);
    if ( !inputFile ) {
        cerr << "File couldn't be opened." << endl;
        exit(1);
    }

    string input;

    inputFile >> test_count;

    shyness.resize(test_count);
    answer.resize(test_count);
    int each_size=0;
    for(int i=0; i<test_count; i++) {
        inputFile >> each_size;
        each_size++;
        shyness[i].resize(each_size);

        int whole_int;
        inputFile >> whole_int;
        for(int j=each_size-1; j>=0; j--) {
            shyness[i][j]=whole_int%10;
            whole_int=whole_int/10;
        }
    }

}

int standing::clapping() {
    for(int i=0; i<test_count; i++) {
        int need_count=0;
        int stand=shyness[i][0];

        for(int j=1; j<shyness[i].size(); j++) {
            if(j>stand) {
                need_count+=(j-stand);
                stand=j;
            }
            stand+=shyness[i][j];
        }
        answer[i]=need_count;
    }
}

int standing::writeFile() {
    ofstream outputFile("Output.txt",ios::out);
    if ( !outputFile ) {
        cerr << "File couldn't be opened." << endl;
        exit(1);
    }

    for(int i=0; i<test_count; i++) {
        outputFile << "Case #" << i+1 << ": " << answer[i];
        outputFile << endl;
    }

}

int main()
{
    standing each;
    each.getStart();

   return 0;
}
