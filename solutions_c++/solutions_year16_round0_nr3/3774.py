#include <iostream>
#include <cstdio>
#include <fstream>
#include <vector>
#include <string>
using namespace std;
vector<string> ans;
int n,k;
int t;
void func(string s){
    int len=s.length();
    
    if(len==n){
        t=len/2;
        while(t--){
            if(s[len-1-t]!=s[t]){
                return;
            }
        }
        if(s[len-1]=='1'&&s[0]=='1'){
            ans.push_back(s);
            
        }
        return;
       
    }
    func(s+"0");
    func(s+"1");
}

int main(){
    ofstream fout;
    
    fout.open("C.out");
    int testCase;
    ifstream fcin;
    fcin.open("C-small-attempt3.in");
    fcin>>testCase;
    
    for(int t=0;t<testCase;t++){
        fcin>>n>>k;
        
        func("");
    }
    fout<<"Case #1:"<<endl;
    for(int i=0;i<k;i++){
        fout<<ans[i]<<' ';
        
        for(int i=3;i<=10;i++)
            fout<<i<<' ';
        fout<<11<<endl;
    }
    return 0;
}