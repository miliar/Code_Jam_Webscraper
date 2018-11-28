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
#include <assert.h>

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

long long int size;
long long int reps;
string ex;

typedef pair<int,int> quadr;

std::vector<std::vector<int>> values = {
    {0, 1, 2, 3},
    {1, 0, 3, 2},
    {2, 3, 0, 1},
    {3, 2, 1, 0},
};

std::vector<std::vector<int>> signes = {
    {1, 1, 1, 1},
    {1, -1, 1, -1},
    {1, -1, -1, 1},
    {1, 1, -1, -1},
};


quadr quard_mult(quadr a, int b) {
    int tmp = a.second;
    return {a.first * signes[tmp][b],values[tmp][b]};
}

bool test_k(long long i_, long long j_) {
    quadr current = {1,0};
    for(long long i = i_; i < reps; ++i) {
        for(long long j = j_; j < ex.size(); ++j) {
            current = quard_mult(current,ex[j]-104);
        }
        j_ = 0;
    }
    return current == (quadr) {1,3};
}

bool test_jk(long long i_, long long j_) {
    quadr current = {1,0};
    for(long long i = i_; i < min(reps, i_ + 5); ++i) {
        for(long long j = j_; j < ex.size(); ++j) {
            current = quard_mult(current,ex[j]-104);
               if(current == (quadr) {1,2}){
                    return true;
                }
        }
        j_ = 0;
    }
    return false;
}

bool test_ijk() {
        quadr current = {1,0};
        for(int i = 0; i < min(reps,(long long) 5); ++i) {
            for(int j = 0; j < ex.size(); ++j) {
                current = quard_mult(current,ex[j]-104);
                if(current == (quadr) {1,1}){
                    return test_jk(i,j+1);
                }
            }
        }
        return false;
}

bool test_possibility() {
    if(ex.size() == 1) {
        return false;
    }
    quadr current = {1,0};
    for(int j = 0; j < ex.size(); ++j) {
           current = quard_mult(current,ex[j]-104);
   }
   if(current.first == -1 && reps % 2 == 0) {
        current.first = 1;
   }
   if(current.second == 0) {
        return current == (quadr) {-1,0};
   }
   if(reps % 2 != 0) {
     return false;
   }
   if(reps % 4 == 2) {
        current.first = current.first * -1;
   }
   return current.first == -1;

}





int main(int argc, const char * argv[])
{
    string line;
    int cases;
    int size;
    
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
        ifile >> reps;
        ifile >> ex;

        //if(ex.size() == 1) {
        //    out << "NO";
        //}
        //
        //
        //
        
        if(!test_possibility()){
            out << "NO";
            print(case_);
            continue;
        }


        if(test_ijk()) {
            out << "YES";
        }else{
            out << "NO";
        }



        print(case_);
    }
    
        
    
    ifile.close();
    ofile.close();
    return 0;
}




bool init() {
    ifile.open("../input.in");
    ofile.open("../output");
    
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