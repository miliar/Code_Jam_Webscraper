#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <cmath>
#include <string>
#include <climits>

using namespace std;

int check(string substring, int n) {
    int flag = 0;
    int count = 0;
    for (int i=0; i<(int)substring.size(); i++) {
        char c = tolower(substring[i]);
        
        if (flag == 0 && !(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') ) {
            flag = 1;
            count = 1;
            if (count >= n) return 1;
        } else if (flag == 1 && !(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') ) {
            count ++;
            if (count >= n) return 1;
        } else {
            flag = 0;
            count = 0;
        }
        
    }
    return 0;
}

int generate(string name, int n) {
    int count = 0;
    for (int i=0; i<(int)name.size(); i++) {
        if (i+n <= (int)name.size()) {
            for (int j = i+n-1 ; j<(int)name.size(); j++) {
                count += check(name.substr(i,j-i+1), n);
            }
        }
        
    }
    return count;
}


int main() {
    
    ifstream myReadFile;
    myReadFile.open("A-small-attempt1.in");
    
    ofstream myWriteFile;
    myWriteFile.open("output.out");
    
    int testCases;
    string buffer;
    
    
    if (myReadFile.is_open()) {
        
        getline(myReadFile , buffer);
        testCases = atoi(buffer.c_str());
        
        
        for (int i = 0; i<testCases; i++) {
            
            int n;
            string name;
            
            getline(myReadFile , buffer);
            istringstream stream(buffer);
            stream >> name >> n;
            
            myWriteFile<<"Case #"<<i+1<<": "<<generate(name, n)<<endl;
            
            
        }
        
    }
    
    
    myReadFile.close();
    myWriteFile.close();
    return 0;
}
