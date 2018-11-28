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

vector<string> trains;
unsigned int size;
unsigned int mycount;
unsigned int numused;



bool test(vector<int>& order,vector<bool>& used,int k) {
    stringstream test;
    for(int i = 0; i < k; ++i) {
        test << trains[order[i]];
    }
    string trainstring = test.str();
    vector<bool> alphabet(26);
    for(int i = 0; i < trainstring.size(); ++i) {
        if(alphabet[(int) trainstring[i] - 48*2 - 1 ]) {
            return false;
            break;
        }
        alphabet[(int) trainstring[i] - 48*2 - 1 ] = true;
        char c = trainstring[i];
        while(i < trainstring.size() && c == trainstring[i]) {
            ++i;
        }
        --i;
    }
    int debug = (int) trainstring[trainstring.size()-1] - 48*2 - 1;
    alphabet[(int) trainstring[trainstring.size()-1] - 48*2 - 1] = false;
    for(int i = 0; i < used.size(); ++i) {
        if(!used[i]) {
            for(int j = 0; j < trains[i].size(); ++j) {
                if( alphabet[(int) trains[i][j] - 48*2 - 1]){
                    return false;
                }
            }
        }
    }
    
    return true;
    
}

void rec(int k, vector<int>& order, vector<bool>& used) {
    if(k < 1) {
        goto skip;
    }
    if(!test(order, used,k)) {
        return;
    }
skip:
    if(k == size-numused) {
        mycount++;
        return;
    }
    for(int i = 0; i < used.size(); ++i) {
        if(!used[i]) {
            used[i] = true;
            order[k] = i;
            rec(k+1,order,used);
            used[i] = false;
        }
    }
}

bool testtrain(int k) {
    vector<bool> alphabet(26);
    
    for(int i = 0; i < trains[k].size(); ++i) {
        alphabet[(int) trains[k][i] - 48*2 - 1 ] = true;
    }
    
    for(int i = 0; i < trains.size(); ++i) {
        if(true) {
            for(int j = 0; j < trains[i].size(); ++j) {
                if( alphabet[(int) trains[i][j] - 48*2 - 1]){
                    return false;
                }
            }
        }
    }
    return true;
}

inline int Factorial(int x) {
    return (x == 1 ? x : x * Factorial(x - 1));
}





int main(int argc, const char * argv[])
{
    string line;
    unsigned int cases;

    
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
        trains.clear();
        mycount = 0;
        
        string line;
        getline(ifile,line);
        stringstream tok(line);
        string read;
        while(tok >> read) {
            trains.push_back(read);
        }
        
        vector<bool> used(size);
        vector<int> order(size);
        
        numused = 0;
        for(int i = 0; i < trains.size(); ++i) {
            if(testtrain(i)) {
                numused++;
                used[i] = true;
            }
        }
        
        if(numused==size) {
            mycount = Factorial(size);
        }else{
            rec(0,order,used);
            int factor = Factorial(size)/Factorial(size-numused);
            mycount *= factor;
            mycount = mycount % 1000000007;
        }
        out << mycount;
        



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






