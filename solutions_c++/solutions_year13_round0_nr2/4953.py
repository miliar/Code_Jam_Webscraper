/* 
 * File:   main.cpp
 * Author: Tivi
 *
 * Created on 13. huhtikuuta 2013, 22:56
 */

#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    //ifstream in("test.txt");
    //ifstream in("B-small-attempt0.in");
    ifstream in("B-large.in");
    //ostream& out = cout;
    ofstream out("out.txt");
    
    int cases;
    in>>cases;
    //cout << cases << endl;
    //string a;
    //getline(in, a); //blanko
    
    int map[100][100];
    bool clear[100][100];
    
    for( int ca=1; ca<=cases; ca++ ) {
        int w=0, h=0;
        in >> h;
        in >> w;
        //cout << w << " " << h << endl;
        for( int j=0; j<h; j++ ) {
            //getline(in,a);
            for( int i=0;i<w; i++ ) {
                in >> map[i][j];
                clear[i][j] = false;
            }
        }
        for( int j=0; j<h; j++ ) {
            //for( int i=0;i<w; i++ )
                //cout << map[i][j];
            //cout << endl;
        }
        
        for( int j=0; j<h; j++ ) {
            int minh=10000;
            int maxh=0;
            for( int i=0;i<w; i++ ) {
                if( minh>map[i][j])
                    minh=map[i][j];
                if( maxh<map[i][j])
                    maxh=map[i][j];
            }
            //cout << "!! " << minh << endl;
            for( int i=0;i<w; i++ )
                if( map[i][j] == maxh )
                    clear[i][j] = true;
        }
        for( int i=0; i<w; i++ ) {
            int minh=10000;
            int maxh=0;
            for( int j=0;j<h; j++ ) {
                if( minh>map[i][j])
                    minh=map[i][j];
                if( maxh<map[i][j])
                    maxh=map[i][j];
            }
            for( int j=0;j<h; j++ )
                if( map[i][j] == maxh )
                    clear[i][j] = true;
        }
        bool yes=true;
        for( int j=0; j<h; j++ )
            for( int i=0;i<w; i++ )
                if( !clear[i][j] ) yes=false;
            
        out << "Case #" << ca << ": ";
        if( yes ) out << "YES";
        else out << "NO";
        out << endl;
        
    }
    //for( int i=0; )
    return 0;
}

