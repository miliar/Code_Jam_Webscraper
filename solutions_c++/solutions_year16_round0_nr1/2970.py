#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

ifstream infile("A-large-sheep.in");
ofstream outfile("out.out");

vector<bool> seen;
int aantalseen = 0;

void parse_digits(long long number){
    while( number > 0 ){
        int digit = number % 10;
        if( seen[digit] ==  false ){
            seen[digit] = true;
            aantalseen++;
        }
        number = (number - digit)/10;
    }
}

void print(vector<bool> v ){
    for( int i = 0 ; i < v.size() ; ++i ){
        cout<<v[i]<<" ";
    }
    cout<<endl;
}
int main(){
    int T;
    seen.resize(10, false);
    infile>>T;

    for( int t = 1 ; t <= T ; ++t ){
        cout<<"Case "<<t<<endl;
        long long n  = 0;
        infile>>n;
        
        if( n == 0 ){
            outfile<<"Case #"<<t<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        
        fill(seen.begin(), seen.end(), false);
        aantalseen = 0;
        long long number = 0;

        while( aantalseen < 10 ){
            number += n;
            parse_digits(number);
        }
            
        outfile<<"Case #"<<t<<": "<<number<<endl;
    }

    return 0;
}