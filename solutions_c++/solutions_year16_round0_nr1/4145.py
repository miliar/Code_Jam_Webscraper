
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

long long solve(long long N){
    
    int ans=0;
    int mat=0;
    vector<int> digit;
    int i=1;
    long long number=0;
    while(mat!=1023){
        digit.clear();
        number=N*i;
        
        stringstream ss;
        ss.clear();
        ss.str("");
        ss<<number;
        for(int p=0;p<ss.str().size();p++){
            digit.push_back(atoi(ss.str().substr(p,1).c_str()));
        }
        for(int p=0;p<digit.size();p++){
            mat=mat | 1<<digit[p];
        }

        ans++;
        i++;
    }
    
    return number;
}


int main(int argc, const char * argv[])
{
    
    ifstream ifs( "a.txt" );
    int T;
    ifs >> T;
    int t=1;
    
    while(t<=T){
        long long N;
        ifs >> N;

        if(N==0){
            cout << "Case #" << t << ": " << "INSOMNIA" << endl;
            t++;
            continue;
        }
        long long ret = solve(N);
        
        cout << "Case #" << t << ": " << ret << endl;
        //cout << t << endl;
        
        t++;
    }
    return 0;
    
}