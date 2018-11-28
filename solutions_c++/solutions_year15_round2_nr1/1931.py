
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

int reverse(int a){
    int b=0;
    stringstream ss;
    ss.clear();
    ss.str("");
    ss << a;
    string tmp="";
    for(int i=0;i<ss.str().size();i++){
        tmp=tmp+ss.str().substr(ss.str().size()-i-1,1);
    }
    ss.clear();
    ss.str("");
    ss << tmp;
    ss >> b;
    return b;
}

bool keta(int a,int b){
    stringstream ss1;
    stringstream ss2;
    ss1.clear();
    ss1.str("");
    ss2.clear();
    ss2.str("");
    ss1 << a;
    ss2 << b;
    if(ss1.str().size()==ss2.str().size()){
        return true;
    }
    return false;
}

int solve1(int N){

    int num[1000000];
    num[0]=0;
    for(int i=1;i<=N;i++){
        int tmp=reverse(i);
        if(tmp<i && keta(i,tmp)){
            num[i]=num[tmp]+1;
        }else{
            num[i]=num[i-1]+1;
        }
    }
    
    return num[N];
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

        //if(t==4){
        int ret = solve1(N);
        
        std::cout << "Case #" << t << ": " << ret << std::endl;
        //}
        t++;
    }
    return 0;
    
}