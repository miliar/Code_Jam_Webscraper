#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
#include <iterator>

using namespace std;

ifstream infile("B-large.in");
ofstream outfile("Boutlarge.out");

vector<bool> fill_vector(string str ){
    vector<bool> v(str.size(), false);
    
    for( int i = 0 ; i < str.size() ; ++i ){
        if( str[i] == '+' ){
            v[i] = true;
        }
    }
    
    return v;
}

void print(vector<bool> v ){
    for( int i = 0 ; i < v.size() ; ++i ){
        cout<<v[i]<<" ";
    }
    cout<<endl;
}

void flipstack(vector<bool> &v, int pos ){
    vector<bool> swap(pos+1, false);
    for( int i = 0 ; i <= pos ; ++i ){
        swap[i] = !v[i];
    }
    
    for( int i = 0 ; i <= pos ; ++i ){
        v[i] = swap[pos-i];
    }
}

int flipalgo( vector<bool> v){
    bool current = v[0];
    int flips = 0;
    
    for( int i = 1 ; i < v.size() ; ++i ){
        if( current == v[i] ) continue;
        flips++;
        current = v[i];
    }
    
    if( current == false ) flips++;
    
    return flips;
}

int main(){
    int T;
    string str;
    infile>>T;
    getline(infile, str);
    
    for(int t = 1 ; t <= T ; ++t ){
        cout<<"Case  "<<t<<endl;
        getline(infile, str);
        vector<bool> v = fill_vector(str);

        int flips1 = flipalgo(v);
        
        outfile<<"Case #"<<t<<": "<<flips1<<endl;
    }
}