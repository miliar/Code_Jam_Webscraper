#include <fstream>
#include <string>
#include <cstring>
#include <iostream>
using namespace std;


std::ifstream in;
std::ofstream out;

void complement(string &s,int first_minus){
    for(int i=0;i<=first_minus;++i){
        if(s[i]=='-'){
            s[i]='+';
        }else{
            s[i]='-';
        }
    }
    int j=s.length()-1;
    for(;j>=0;j--){
        if(s[j]=='-'){
            break;
        }
    }
}


int solve(string &s){
    int j=s.length()-1;
    for(;j>=0;j--){
        if(s[j]=='-'){
            break;
        }
    }
    int first_minus=j;
    if(first_minus!=-1){
        complement(s,first_minus);
        return 1+solve(s);
    }else{
        return 0;
    }
}

int main(){
    in.open("in");
    out.open("out");
    int T;
    in>>T;
    for(int i=1;i<=T;++i){
        string current;
        in>>current;
        int ans = solve(current);
        out<<"Case #"<<i<<": "<<ans<<endl;
    }
}
