
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <iostream>
#include <iomanip>
using namespace std;

int max(int a,int b){
    return a < b ? b : a;
}
int min(int a,int b){
    return a > b ? b : a;
}



int solve(int A,int B,int K){
    int cnt=0;
    for(int i=0;i<A;i++){
        for(int j=0;j<B;j++){
            if((i & j)<K){
                cnt++;
            }
        }
    }
    return cnt;
}


int main(int argc, const char * argv[])
{

    std::ifstream ifs( "a.txt" );
    
    int T;
    ifs >> T;
    int t=1;
    while(t<=T){
        int A,B,K;
        ifs >> A >> B >> K;
        
        int ret = solve(A,B,K);
        std::cout << "Case #" << t << ": " << ret << std::endl;
        
        
        t++;
    }
    return 0;
    
}