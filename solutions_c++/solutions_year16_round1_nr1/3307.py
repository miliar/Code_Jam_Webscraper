
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
#include <queue>
using namespace std;

long max(long a,long b){
    return a < b ? b : a;
}
long min(long a,long b){
    return a > b ? b : a;
}


class LessInt {
public:
    bool operator()(const string& riLeft, const string& riRight) const {
        if(riLeft.length()!=riRight.length()){
            return riLeft.length() < riRight.length();
        }else{
            return riLeft<riRight;
        }
    }
};

long long isPrim(long long a){
    if(a==1){
        return 1;
    }
    lldiv_t l;
    l = lldiv(a+1,2);
    for(long long i=2;i<=l.quot;i++){
        l = lldiv(a,i);
        if(l.rem==0){
            return i;
        }
    }
    return 1;
}

string solve(string S){
    string ans="";
    ans=S.substr(0,1);
    for(int i=1;i<S.size();i++){
        if(ans.substr(0,1)>S.substr(i,1)){
            ans=ans+S.substr(i,1);
        }else{
            ans=S.substr(i,1)+ans;
        }
    }
    return ans;
}


int main(int argc, const char * argv[])
{
    
    ifstream ifs( "a.txt" );
    int T;
    ifs >> T;
    int t=1;
    
    while(t<=T){
        string S;
        ifs >> S;
        
        string ret = solve(S);
        
        cout << "Case #" << t << ": " << ret << endl;
        
        t++;
    }
    return 0;
    
}