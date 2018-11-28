
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int max(int a,int b){
    return a < b ? b : a;
}
int min(int a,int b){
    return a > b ? b : a;
}



string solve(string str){
    int i=0;
    string tmp;
    while(str.compare(i,1,"/")!=0){
        tmp.append(str.substr(i,1));
        i++;
        if(i==str.size()){
            break;
        }
    }
    i++;//デリミタ分
    double P = atof(tmp.c_str());
    tmp.clear();
    while(i<str.size()){
        tmp.append(str.substr(i,1));
        i++;
    }
    double Q =atof(tmp.c_str());
    
    for(i=0;i<=40;i++){
        if(Q<pow(2.0,i)){
            int k=0;
            for(int j=0;j<=i;j++){
                if(fmod(Q,pow(2.0,j))==0){
                    k=j;
                }
            }
            if(k==0){
                return "impossible";
            }
            double tmp=Q/pow(2.0,k);
            if(fmod(P,tmp)!=0){
                return "impossible";
            }

        }else if(Q==pow(2.0,i)){
            break;
        }
    }
    
    int ans=0;
    for(i=0;i<=40;i++){
        if((pow(2.0,i)*P-Q)>=0){
            ans=i;
            break;
        }
    }
    
    stringstream ss;
    ss.clear();
    ss << ans;
    return ss.str();
}


int main(int argc, const char * argv[])
{
    
    std::ifstream ifs( "a.txt" );
    
    int T;
    ifs >> T;
    int t=1;
    while(t<=T){

        string tmp;
        ifs >> tmp;

        string ret = solve(tmp);
        std::cout << "Case #" << t << ": " << ret << std::endl;
        
        
        t++;
    }
    return 0;
    
}