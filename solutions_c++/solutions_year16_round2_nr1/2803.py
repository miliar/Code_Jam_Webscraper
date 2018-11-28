
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

    //0 z
    //2 w
    //4 u
    //6 x
    //8 g
    //5 4を除いたあとのf
    //7 6を除いたあとのs
    //3 0,4を除いたあとのr
    //1 0,2,4を除いたあとのo
    //9 1,7を除いたn
    sort(S.begin(),S.end());
    string ans="";
    int zz=0;
    int ww=0;
    int uu=0;
    int xx=0;
    int gg=0;
    int ff=0;
    int ss=0;
    int rr=0;
    int oo=0;
    int nn=0;
    for(int i=0;i<S.size();i++){

        if(S.substr(i,1)=="Z"){
            zz++;
            ans=ans+"0";
        }else if(S.substr(i,1)=="W"){
            ww++;
            ans=ans+"2";
        }else if(S.substr(i,1)=="U"){
            uu++;
            ans=ans+"4";
        }else if(S.substr(i,1)=="X"){
            xx++;
            ans=ans+"6";
        }else if(S.substr(i,1)=="G"){
            gg++;
            ans=ans+"8";
        }else if(S.substr(i,1)=="F"){
            ff++;
        }else if(S.substr(i,1)=="S"){
            ss++;
        }else if(S.substr(i,1)=="R"){
            rr++;
        }else if(S.substr(i,1)=="O"){
            oo++;
        }else if(S.substr(i,1)=="N"){
            nn++;
        }
    }
    
    for(int i=0;i<(ff-uu);i++){
        ans=ans+"5";
    }
    for(int i=0;i<(ss-xx);i++){
        ans=ans+"7";
    }
    for(int i=0;i<(rr-zz-uu);i++){
        ans=ans+"3";
    }
    for(int i=0;i<(oo-zz-ww-uu);i++){
        ans=ans+"1";
    }
    for(int i=0;i<((nn-(oo-zz-ww-uu)-(ss-xx))/2);i++){
        ans=ans+"9";
    }
    sort(ans.begin(),ans.end());
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