#include <fstream>
#include <string>
#include <cstring>
#include <iostream>
using namespace std;


std::ifstream in;
std::ofstream out;
long long ans[1000001]={0};


int count_values(long long n, bool count[]){
    int current=0;
    std::string s = std::to_string(n);
    for(int i=0;i<s.length();i++){
        if(count[s[i]-'0']==0){
            current++;
            count[s[i]-'0']++;
        }
    }
    return current;
}


long long calculate(long long n){
    int i=1;
    int current =0;
    bool count[10]={0};
    while(current != 10){
        current+=count_values(n*i,count);
        i++;
    }
    return n*(i-1);
}

int main(){
    ans[0]=-1;
    for(int i=1;i<=1000005;++i){
        ans[i]=calculate(i);
    }
    in.open("in");
    out.open("out");
    int T;
    in>>T;
    for(int i=1;i<=T;++i){
        int current;
        in>>current;
        if(current!=0){
            out<<"Case #"<<i<<": "<<ans[current]<<endl;
        }else{
            out<<"Case #"<<i<<": INSOMNIA"<<endl;
        }
    }
}
