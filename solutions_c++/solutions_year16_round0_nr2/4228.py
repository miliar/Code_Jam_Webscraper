
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



int matchcnt(string x,string y){
    int ans=0;
    int l=(int)min(x.length(),y.length());
    for(int i=0;i<l;i++){
        if(x[i]==y[i]){
            ans++;
        }else{
            break;
        }
    }
    return ans;
}
/*int kyori[302][302];
for(int i=0;i<dict.size();i++){
    kyori[i][i]=1000000000;
    for(int j=i+1;j<dict.size();j++){
        int m=matchcnt(dict[i],dict[j]);
        if(m!=0){
            kyori[i][j]=(int)dict[i].length()-m+(int)dict[j].length()-m;
            kyori[j][i]=kyori[i][j];
        }else{
            kyori[i][j]=(int)dict[i].length()+(int)dict[j].length();
            kyori[j][i]=kyori[i][j];
        }
    }
}*/

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

class LessDouble {
public:
    bool operator()(const double& riLeft, const double& riRight) const {
        return riLeft < riRight;
    }
};

struct Vertex {
    int to;
    int capa;
    int cost;
    int rev;
};



/*vector<Vertex> G[MAXV];
void add_edge(int from, int to, int capa, int cost){
    G[from].push_back((Vertex){to,capa,cost,(int)G[to].size()});//rev:次にG[to]追加するものが逆辺
    G[to].push_back((Vertex){from,0,-cost,(int)G[from].size()-1});//rev:さっきG[from]追加したものが逆辺
}*/

string maneuver(string instr,int end){
    string ret="";
    for(int i=0;i<instr.size();i++){
        if(i<=end){
            if(instr.substr(end-i,1)=="-"){
                ret=ret+"+";
            }else{
                ret=ret+"-";
            }
        }else{
            ret=ret+instr.substr(i,1);
        }
    }
    return ret;
}

int solve(string S){
    
    int ans=0;
    
    int end=-1;
    int endsub=-1;
    string str=S;
    string tmpstr="";
    
    while(1){
        end=-1;
        endsub=-1;
        for(int i=(int)str.length();i>=0;i--){
            if(str.substr(i,1)=="-"){
                end=i;
                break;
            }
        }
        if(end==-1){
            break;
        }
        if(str.substr(0,1)=="+"){
            for(int i=0;i<(int)str.length();i++){
                if(str.substr(i,1)=="-"){
                    endsub=i-1;
                    break;
                }
            }
            tmpstr=maneuver(str,endsub);
            ans++;
        }else{
            tmpstr=str;
        }
        
        str=maneuver(tmpstr,end);
        ans++;
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

        int ret = solve(S);
        
        cout << "Case #" << t << ": " << ret << endl;
        
        t++;
    }
    return 0;
    
}