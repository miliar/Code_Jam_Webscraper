
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <iostream>
using namespace std;

int max(int a,int b){
    return a < b ? b : a;
}
int min(int a,int b){
    return a > b ? b : a;
}


string solve(int N1,int N2,vector<int> vstr1,vector<int> vstr2){
    int ans=0;
    string ansstr;
    for(int i=0;i<4;i++) {
        for(int j=0;j<4;j++){
            if(vstr1[(N1-1)*4+i]==vstr2[(N2-1)*4+j]){
                ans++;
                ansstr=to_string(vstr1[(N1-1)*4+i]);
            }
        }
    }
    
    if(ans==0){
        ansstr="Volunteer cheated!";
    }else if(ans>1){
        ansstr="Bad magician!";
    }
    
    return ansstr;
}


int main(int argc, const char * argv[])
{
    //CodeJam *codejam;
    
    std::ifstream ifs( "a.txt" );
    
    int T;
    ifs >> T;
    int t=1;
    while(t<=T){
        int N1,N2;
        vector<int> vstr1,vstr2;
        
        ifs >> N1;
        for(int i=0;i<4;i++){
            int tmp1,tmp2,tmp3,tmp4;
            ifs >> tmp1 >> tmp2 >> tmp3 >> tmp4;
            vstr1.push_back(tmp1);
            vstr1.push_back(tmp2);
            vstr1.push_back(tmp3);
            vstr1.push_back(tmp4);
        }
        ifs >> N2;
        for(int i=0;i<4;i++){
            int tmp1,tmp2,tmp3,tmp4;
            ifs >> tmp1 >> tmp2 >> tmp3 >> tmp4;
            vstr2.push_back(tmp1);
            vstr2.push_back(tmp2);
            vstr2.push_back(tmp3);
            vstr2.push_back(tmp4);
        }
        
        string ret = solve(N1,N2,vstr1,vstr2);
        
        std::cout << "Case #" << t << ": " << ret << std::endl;
        t++;
        vstr1.clear();
        
    }
    return 0;
    
}