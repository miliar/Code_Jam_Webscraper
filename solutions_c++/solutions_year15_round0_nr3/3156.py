
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

string multiDijkstra(string p, string q){
    
    if(p=="1"){
        return q;
    }else if(p=="i"){
        if(q=="1"){
            return "i";
        }else if(q=="i"){
            return "-1";
        }else if(q=="j"){
            return "k";
        }else if(q=="k"){
            return "-j";
        }
    }else if(p=="j"){
        if(q=="1"){
            return "j";
        }else if(q=="i"){
            return "-k";
        }else if(q=="j"){
            return "-1";
        }else if(q=="k"){
            return "i";
        }
    }else if(p=="k"){
        if(q=="1"){
            return "k";
        }else if(q=="i"){
            return "j";
        }else if(q=="j"){
            return "-i";
        }else if(q=="k"){
            return "-1";
        }
    }
    return "error";
}

string solve(int L,int X, string dijk){
    string ans;
    int sgn=1;
    int flagi=0;
    int flagj=0;
    int flagk=0;

    ans="1";
    for(int n=0;n<X;n++){
    for(int i=0;i<L;i++){
        string tmp;
        tmp=dijk[i];
        if(ans=="i" && flagi==0 && flagj==0 && flagk==0){
            ans="1";
            sgn=1;
            flagi=1;
        }else if(ans=="j" && flagi==1 && flagj==0 && flagk==0){
            ans="1";
            sgn=1;
            flagj=1;
        }else if(ans=="k" && flagi==1 && flagj==1 && flagk==0){
            ans="1";
            sgn=1;
            flagk=1;
        }
        ans=multiDijkstra(ans,tmp);
        if(ans.size()==2){
            sgn=sgn*(-1);
            ans=ans[1];
        }
    }
    }
    //std::cout << ans;
    
    if(flagi==1 && flagj==1 && flagk==1 && ans=="1" && sgn==1){
        return "YES";
    }else if(flagi==1 && flagj==1 && ans=="k" && sgn==1){
        return "YES";
    }else{
        return "NO";
    }
}


int main(int argc, const char * argv[])
{
    
    std::ifstream ifs( "a.txt" );
    
    int T;
    ifs >> T;
    int t=1;
    
    while(t<=T){
        
        int L;
        int X;
        string dijk;
        ifs >> L >> X;
        ifs >> dijk;
        string ret = solve(L,X,dijk);
        std::cout << "Case #" << t << ": " << ret << std::endl;
        t++;
    }
    return 0;
    
}