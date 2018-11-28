/*
*	Nick: Varaquilex
*	Name: Volkan İlbeyli
*	Mail: volkan@ilbeyli.info
*/


#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <list>

using namespace std;

/// STL typedefs ///
//1D vectors
typedef vector<int> vi;
typedef vector<double> vd;
//iterators
typedef vector<int>::iterator viit;
typedef vector<double>::iterator vdit;

//STL macros
#define Iterate(it,c) for(__typeof(c.begin()) it = c.begin() ; it != c.end() ; it++)
#define whole(v) v.begin(), v.end()

bool checkPalin(int);

int main(int argc, char** argv) {

//    if (argc != 1) { //program input error check
//        cout << "Invalid argument count." << endl;
//        cout << "Example: ./a.out **FORMAT**" << endl;
//        cout << "Returning from main()..." << endl;
//        return -1;
//    }
    FILE* fp, *out;
    
    fp = fopen("c-small.in","r");
    if(fp == NULL){
        cout << "error opening file: " << endl;
        return -1;
    }
    
    int n;
    fscanf(fp, "%d\n", &n);
    
    out = fopen("c-small.out","w");
    if(out == NULL){
        cout << "error opening file: " << endl;
        return -1;
    }
    
    for(int i=0 ; i<n ; i++){
        int a,b; //intervals
        unsigned int count = 0;
        fscanf(fp,"%d %d\n", &a, &b);
        
        for(int j=a ; j<=b ; j++){   //check palind.
            //cout << "checking " << j << " and its sqrt " << sqrt(j) << endl; 
            if(checkPalin(j) == true){
                if(ceil(sqrt(j)) == sqrt(j) && checkPalin(sqrt(j)) == true)
                    count++;
            }
        }
        cout << "Case #" << i+1 << ": " << count << endl;
        fprintf(out,"Case #%d: %d\n", i+1, count);
    }
    fclose(out);
    fclose(fp);
    return 0;
}

bool checkPalin(int n){
    stringstream ss;
    ss << n;
    string s = ss.str();
    
    if(s.size() == 1)
        return true;
    else if(s.size()%2 == 0){
        string half1 = s.substr(0, s.length()/2);
        string half2 = s.substr(s.length()/2, s.length());
        reverse(whole(half1));
        if(half1 == half2){
            //cout << s << endl;
            return true;
        }
    }
    else if(s.size()%2 == 1){
        string half1 = s.substr(0, s.length()/2);
        string half2 = s.substr(s.length()/2+1, s.length());
        reverse(whole(half1));
        if(half1 == half2){
            //cout << s << endl;
            return true;
        }
    }
  
    return false;
}