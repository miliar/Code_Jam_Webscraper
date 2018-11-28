
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

int solve(int N,int J){
    
    vector<long long> ans;
    ans.clear();
    int counter=0;
    
    for(int i=0;i<(1<<(N-1));i++){
        
        
        long long kai2=0;
        long long kai3=0;
        long long kai4=0;
        long long kai5=0;
        long long kai6=0;
        long long kai7=0;
        long long kai8=0;
        long long kai9=0;
        long long kai10=0;
        
        for(int j=1;j<N;j++){
            if((i>>j & 1) == 1){
                kai2=kai2+pow(2,j);
                kai3=kai3+pow(3,j);
                kai4=kai4+pow(4,j);
                kai5=kai5+pow(5,j);
                kai6=kai6+pow(6,j);
                kai7=kai7+pow(7,j);
                kai8=kai8+pow(8,j);
                kai9=kai9+pow(9,j);
                kai10=kai10+pow(10,j);
                
            }
        }
        kai2=kai2+pow(2,N-1)+1;
        kai3=kai3+pow(3,N-1)+1;
        kai4=kai4+pow(4,N-1)+1;
        kai5=kai5+pow(5,N-1)+1;
        kai6=kai6+pow(6,N-1)+1;
        kai7=kai7+pow(7,N-1)+1;
        kai8=kai8+pow(8,N-1)+1;
        kai9=kai9+pow(9,N-1)+1;
        kai10=kai10+pow(10,N-1)+1;
        long long tmp2=isPrim(kai2);
        if(tmp2==1) continue;
        
        long long tmp3=isPrim(kai3);
        if(tmp3==1) continue;
        
        long long tmp4=isPrim(kai4);
        if(tmp4==1) continue;
        
        long long tmp5=isPrim(kai5);
        if(tmp5==1) continue;
        
        long long tmp6=isPrim(kai6);
        if(tmp6==1) continue;
        
        long long tmp7=isPrim(kai7);
        if(tmp7==1) continue;
        
        long long tmp8=isPrim(kai8);
        if(tmp8==1) continue;
        
        long long tmp9=isPrim(kai9);
        if(tmp9==1) continue;
        
        long long tmp10=isPrim(kai10);
        if(tmp10==1) continue;
        
        
        if(ans.end()!=find(ans.begin(), ans.end(), kai10)){
            continue;
        }else{
            ans.push_back(kai10);
        }
        
        cout << kai10 << " " <<
                tmp2 << " " << tmp3 << " " << tmp4 << " " << tmp5 << " " <<
                tmp6 << " " << tmp7 << " " << tmp8 << " " << tmp9 << " " <<tmp10 <<endl;
        
        //cout << kai2 << ":" << kai3<<":" << kai4<<":" << kai5<<":" <<
        //                    kai6<<":" << kai7<<":" << kai8<<":" << kai9<<":" << kai10<<endl;
        //stringstream ss;
        //ss << static_cast<std::bitset<16>>(i);
        //cout <<  ss.str() << endl;
        
        counter++;
        if(counter>=J){
            break;
        }
    }

    
    return 0;
}


int main(int argc, const char * argv[])
{
    
    ifstream ifs( "a.txt" );
    int T;
    ifs >> T;
    int t=1;
    
    while(t<=T){
        int N,J;
        ifs >> N >> J;

        cout << "Case #" << t << ": " << endl;
        
        int ret = solve(N,J);
        
        //cout << "Case #" << t << ": " << ret << endl;
        
        t++;
    }
    return 0;
    
}