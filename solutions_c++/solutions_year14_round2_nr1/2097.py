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
        out.str("");
        cout << "\nBegin with Case #" << case_ << ": \n";
        ifile >> size;
        getline(ifile,line);
        
        string s1;
        getline(ifile,s1);
        string s2;
        getline(ifile,s2);
        
        int pos1 = 0;
        int pos2 = 0;
        int count = 0;
        
        
        
        while(true) {
            
            if(s1[pos1] != s2[pos2]) {
                out << "Fegla Won";
                break;
            }
            
            int tpos1 = pos1;
            while(pos1 < s1.size() && s1[tpos1] == s1[pos1] ) {
                pos1++;
            }
            int tpos2 = pos2;
            while(pos2 < s2.size() && s2[tpos2] == s2[pos2] ) {
                pos2++;
            }
            
            count += abs(pos1 - tpos1 - pos2 + tpos2);
            
            if(pos1 == s1.size() || pos2 == s2.size()) {
                if(pos1 == s1.size() && pos2 == s2.size()) {
                    out << count;
                }else {
                    out << "Fegla Won";
                }
                break;
            }
            
            
            
            
        }

        
        
        
        
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






