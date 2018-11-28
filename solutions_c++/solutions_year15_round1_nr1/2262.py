
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

long max(long a,long b){
    return a < b ? b : a;
}
long min(long a,long b){
    return a > b ? b : a;
}

int ret2=0;

int solve1(vector<int> tensec){

    int ret1=0;
    int max=0;
    for(int i=0;i<tensec.size()-1;i++){
        if(tensec[i]>tensec[i+1]){
            if(max<tensec[i]-tensec[i+1]){
                max=tensec[i]-tensec[i+1];
            }
            ret1=ret1+tensec[i]-tensec[i+1];
        }
    }
    //std::cout << max;
    ret2=0;
    for(int i=0;i<tensec.size()-1;i++){
        if(max>tensec[i]){
            ret2=ret2+tensec[i];
        }else{
            ret2=ret2+max;
        }
    }
    //std::cout << ret2;
    
    return ret1;
}


int main(int argc, const char * argv[])
{
    
    std::ifstream ifs( "a.txt" );
    
    int T;
    ifs >> T;
    int t=1;
    
    while(t<=T){
        
        int N;
        ifs >> N;
        vector<int>tensec;
        tensec.clear();
        
        for(int i=0;i<N;i++){
            int tmp=0;
            ifs >> tmp;
            tensec.push_back(tmp);
        }

        //if(t==32){
        int ret1 = solve1(tensec);
        
        std::cout << "Case #" << t << ": " << ret1 << " " << ret2 << std::endl;
        //}
        t++;
    }
    return 0;
    
}