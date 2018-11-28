/*
  Author     :  Akash Roy
*/
//============================================================
#include <iostream>
#include <map>
#include <sstream>
#include <cstdio>
#include <cstring>

using namespace std;

void updateKeys(long long int n,map<char,int> &keyMaps){
     while(n!=0){
         keyMaps[(char)('0'+(n%10))]=1;
         n/=10;
     }
}

bool checkKeys(map<char,int> &keyMaps){
     for(char c='0';c<='9';c++)
         if(keyMaps[c]==0)return false;
     return true;
}

int main(){
    FILE *fin = freopen("A-large.in", "r", stdin);
    FILE *fout = freopen("A-large.out", "w", stdout);
    int T,C;
    cin>>T;
    C=T;
    while(T--){
        long long int N,val=0;
        bool tag=false;
        map<char,int> keyMaps;
        cin>>N;           
        if(N!=0){
            for(long long int i=1;i<=1000;i++){
                val=i*N;
                updateKeys(val,keyMaps);
                if(checkKeys(keyMaps)==false)continue;
                else{
                    tag=true;
                    break;
                }
            }
        }
        if(tag==true)cout<<"Case #"<<C-T<<": "<<val<<endl;
        else cout<<"Case #"<<C-T<<": "<<"INSOMNIA"<<endl;
        
    }
    getchar();
    return 0;
}

