//
//  main.cpp
//  fairsquare
//
//  Created by YankeTealeaf on 4/13/13.
//  Copyright (c) 2013 Teaelaf. All rights reserved.
//

#include <iostream>


#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <math.h>

using namespace std;

class FileReader : public ifstream
{
public:
    FileReader( const string& filename ) { open( filename.c_str(), ios_base::in ); }
    int readInt() { int x; *this >> x; return x; }
    vector<int> readInts( int n ) { vector<int> v(n); for ( int i = 0; i < n; i++ ) v[i] = readInt(); return v; }
    string readLine() { char buf[20000]; getline( buf, sizeof(buf) ); return buf; }
    //vector<string> readLines( int n ) { vector<string> v; for ( int i = 0; i < n; i++ ) v.push_back( readLine() ); return v; }
    string readString() { string x; *this >> x; return x; }
    vector<string> readStrings( int n ) { vector<string> v; for ( int i = 0; i < n; i++ ) v.push_back( readString() ); return v; }
    
};

class FileWriter : public ofstream
{
public:
    FileWriter( const string& filename ) { open( filename.c_str(), ios_base::out ); }
    //int writeInt() { int x; *this << x; return x; }
    //int writeString( const string& str ) { *this << str; }
};



bool isHuiwen(int a){
    
    int bi = log10(a);
    
    int aa[10] ;
    
    for(int i=bi; i >=0; i--){
        aa[i] = a%10;
        a /= 10;
    }
    
    for(int j = 0 ; j < (bi + 1)/2; j++){
        if(aa[j] != aa[bi - j])
            return false;
    }
    
    return true;
}
 


int doit(FileReader & fin){
    
    int A = fin.readInt();
    int B = fin.readInt();
    
    int hi = log10(B);
    cout<<hi<<endl;
    
    int sum = 0;
    
    for(int i = A ; i <= B ; i++){
        double d = sqrt(i);
        if( isHuiwen(i) && d == floor(d) && isHuiwen(d) )
            sum ++;
             
    }
    
    return sum;
}

int main(int argc, const char * argv[])
{

    FileReader fin("input.txt");
    FileWriter fout("output.txt");
    
    int T = fin.readInt();
    cout<<T<<endl;
    
    fin.readLine();
    
    for(int i = 0 ; i < T ; i++){
        stringstream ss;
        ss <<"Case #"<<(i+1)<<": "<<doit(fin)<<endl;
        fout<<ss.str().c_str();
    }
    
    
    
    return 0;
}

