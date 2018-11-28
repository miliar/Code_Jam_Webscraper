//
//  main.cpp
//  tic
//
//  Created by YankeTealeaf on 4/12/13.
//  Copyright (c) 2013 Teaelaf. All rights reserved.
//

#include <iostream>


#include <fstream>
#include <vector>
#include <string>
#include <sstream>

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

string doit(FileReader & fin){
        
    char tic[4][4];
    
    for(int j = 0 ; j < 4 ; j++ ){
        string s = fin.readLine();
            for(int i = 0 ; i < s.length() ; i++){
                tic[j][i] = s[i];
            }
    }
    
    fin.readLine();
    
    
    for(int i = 0 ; i < 4 ; i++ ){
        cout<<" "<<endl;
        for(int j = 0 ; j < 4 ; j++){
            cout<<tic[i][j];
        }
    }

    cout<<endl;
        
    for(int i = 0 ; i < 4 ; i++){
        if( (tic[i][0] == tic[i][1] || tic[i][0] == 'T' || tic[i][1] == 'T')
           && (tic[i][0] == tic[i][2] || tic[i][2] == 'T' ) && (tic[i][0] == tic[i][3] || tic[i][3] == 'T') ){
            if(tic[i][0] == 'X' || tic[i][1] == 'X')
                return "X won";
            else if(tic[i][0] == 'O' || tic[i][1] == 'O')
                return "O won";
        }
        
        
        if( (tic[0][i] == tic[1][i] || tic[0][i] == 'T' || tic[1][i] == 'T')
           && (tic[0][i] == tic[2][i] || tic[2][i] == 'T' ) && (tic[0][i] == tic[3][i] || tic[3][i] == 'T') ){
            if(tic[0][i] == 'X' || tic[1][i] == 'X')
                return "X won";
            else if(tic[0][i] == 'O' || tic[1][i] == 'O')
                return "O won";
        }
        
    }
    
    
    if( (tic[0][0] == tic[1][1] || tic[0][0] == 'T' || tic[1][1] == 'T')
       && (tic[0][0] == tic[2][2] || tic[2][2] == 'T' ) && (tic[0][0] == tic[3][3] || tic[3][3] == 'T') ){
        if(tic[0][0] == 'X' || tic[1][1] == 'X')
            return "X won";
        else if(tic[0][0] == 'O' || tic[1][1] == 'O')
            return "O won";
    }
    
    
    if( (tic[0][3] == tic[1][2] || tic[0][3] == 'T' || tic[1][2] == 'T')
       && (tic[0][3] == tic[2][1] || tic[2][1] == 'T' ) && (tic[0][3] == tic[3][0] || tic[3][0] == 'T') ){
        if(tic[0][3] == 'X' || tic[1][2] == 'X')
            return "X won";
        else if(tic[0][3] == 'O' || tic[1][2] == 'O')
            return "O won";
    }
    
    for(int i = 0 ; i < 4 ; i++){
        for(int j = 0 ; j < 4 ; j++){
            if (tic[i][j] == '.' )
                return "Game has not completed";
        }
    }
    
    
    return "Draw";
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

