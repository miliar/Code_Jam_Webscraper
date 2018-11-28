//
//  main.cpp
//  hello1
//
//  Created by Marvin Teichmann on 12.04.14.
//  Copyright (c) 2014 mteichmann. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

bool init();

void readarray(vector<int>& v);
void readarray(vector<double>& v);

void printarray(vector<int>& v);
void printarray(vector<double>& v);
void print(int _case);


ifstream ifile;
ofstream ofile;

stringstream out;

int main(int argc, const char * argv[])
{
    string line;
    unsigned int cases;
    unsigned int size;
    
    if(!init() ) {
        cerr << "Error during initialization \n";
        return 1;
    }
    
    ifile>>cases;
    getline(ifile,line);
    for(int case_ = 1; case_ <= cases; ++case_){
        unsigned int A;
        unsigned int B;
        unsigned int K;
        out.str("");
        cout << "\nBegin with Case #" << case_ << ": \n";
        ifile >> A;
        ifile >> B;
        ifile >> K;
        getline(ifile,line);
        int count =0;
        for(unsigned int a = 0; a < A; ++a) {
            for(unsigned int b = 0; b < B; ++b) {
                unsigned int together = a&b;
                if(together < K) {
                    count++;
                }
            }
        }

        
        out << count;
        
        
        
        
        print(case_);
    }
    
    
    
    ifile.close();
    ofile.close();
    return 0;
}



bool init() {
    ifile.open("/Users/marvinteichmann/Dropbox/projekte/io/input");
    ofile.open("/Users/marvinteichmann/Dropbox/projekte/io/output");
    
    cout.precision(12);
    ofile.precision(12);
    out.precision(12);
    
    if(!ifile.is_open()) {
        
    }
    
    return true;
}

void readarray(vector<int>& v) {
    string line;
    getline(ifile,line);
    stringstream tok(line);
    int read;
    while(tok >> read) {
        v.push_back(read);
    }
}

void readarray(vector<double>& v) {
    string line;
    getline(ifile,line);
    stringstream tok(line);
    double read;
    while(tok >> read) {
        v.push_back(read);
    }
}

void print(int _case){
    string output = out.str();
    
    ofile << "Case #" << _case << ": " << output  << "\n";
    cout  << "Case #" << _case << ": " << output  << "\n";
    
    
}

void printarray(vector<int>& v) {
    for(size_t i = 0; i < v.size(); ++i) {
        cout << v[i] << " ";
    }
    cout << "\n";
}


void printarray(vector<double>& v) {
    for(size_t i = 0; i < v.size(); ++i) {
        cout << v[i] << " ";
    }
    cout << "\n";
}

struct comb {
    bool operator() (int i,int j) { return (i<j);}
    bool operator() (double i,double j) { return (i<j);}
    bool operator() (string i,string j) { return true;}
} mycomb;






