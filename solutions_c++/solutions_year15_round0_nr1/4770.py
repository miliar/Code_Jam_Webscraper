
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

double solve(int S,string audience){
    //初期
    stringstream ss;
    ss.clear();
    ss.str("");
    int au;
    ss << audience.substr(0,1);
    ss >> au;
    int cnt=au;
    int ans=0;
    
    for(int i=1;i<=S;i++){
        if(cnt<i){
            ans=ans+(i-cnt);
            cnt=i;
        }
        ss.clear();
        ss.str("");
        ss << audience.substr(i,1);
        ss >> au;
        cnt=cnt+au;
        
    }
    
    return ans;
}


int main(int argc, const char * argv[])
{
    
    std::ifstream ifs( "a.txt" );
    
    int T;
    ifs >> T;
    int t=1;
    
    while(t<=T){
        int S;
        string audience;
        ifs >> S >> audience;
        int ret = solve(S,audience);
        std::cout << "Case #" << t << ": " << ret << std::endl;
        t++;
    }
    return 0;
    
}