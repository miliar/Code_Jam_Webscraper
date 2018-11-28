
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <iostream>
#include <iomanip>
using namespace std;

int max(int a,int b){
    return a < b ? b : a;
}
int min(int a,int b){
    return a > b ? b : a;
}



string solve(vector<string> str){
    
    char mojiretu[101][101];
    int  mojisuu[101][101];
    for(int i=0;i<101;i++){
        for(int j=0;j<101;j++){
            mojisuu[i][j]=0;
            mojiretu[i][j]='A';
        }
    }
    for(int i=0;i<str.size();i++){
        char tmp[2]="A";
        int k=-1;
        for(int j=0;j<str[i].size();j++){
            if(strncmp(tmp,&str[i].at(j),1)!=0){
                strncpy(tmp,&str[i].at(j),1);
                k++;
                mojiretu[i][k]=str[i].at(j);
                mojisuu[i][k]++;
            }else{
                mojisuu[i][k]++;
            }
        }
    }
    
    for(int i=0;i<101;i++){
        for(int j=0;j<str.size();j++){
            if(strncmp(&mojiretu[0][i],&mojiretu[j][i],1)!=0){
                return "Fegla Won";
            }
        }
    }
    
    int resultcnt=0;
    for(int i=0;i<101;i++){
        double sum=0;
        double cnt=0;
        for(int j=0;j<str.size();j++){
            sum=sum+mojisuu[j][i];
            cnt++;
        }
        int mid=0;
        if((int)sum/cnt+0.5>sum/cnt){
            mid=(int)sum/cnt;
        }else{
            mid=(int)sum/cnt+1;
        }
        for(int j=0;j<str.size();j++){
            if(mojisuu[j][i]-mid<0){
                resultcnt=resultcnt-(mojisuu[j][i]-mid);
            }else{
                resultcnt=resultcnt+(mojisuu[j][i]-mid);
            }
        }
    }
    
    stringstream ss;
    ss.clear();
    ss << resultcnt;
    return ss.str();
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
        
        vector<string> str;
        for(int i=0;i<N;i++){
            string tmp;
            ifs >> tmp;
            str.push_back(tmp);
        }
        
        string ret = solve(str);
        std::cout << "Case #" << t << ": " << ret << std::endl;
        
        
        t++;
    }
    return 0;
    
}