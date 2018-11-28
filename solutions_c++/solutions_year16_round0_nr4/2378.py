#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

ifstream infile("D-small-attempt0.in");
ofstream outfile("Dout.out");

int main(){
    int T;
    infile>>T;
    
    for( int t = 1 ; t <= T ; ++t ){
        int K, C, S;
        infile>>K>>C>>S;
        
        outfile<<"Case #"<<t<<":";
        
        if( ( C > 1 && S < K-1) || ( C == 1 && S < K ) ){
            outfile<<" IMPOSSIBLE"<<endl;
            continue;
        }
        
        for( int i = 1 ; i <= K ; ++i ){
            outfile<<" "<<i;
        }
        outfile<<endl;
    }
    
    return 0;
}