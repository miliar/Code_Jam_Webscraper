#include<bits/stdc++.h>

using namespace std;

int count(int n){
    bool Log[10];
    bool log;
    for(int i=0; i<10; i++)Log[i]=false;
    for(int i=1; ; i++){
        log=true;
        int tmp = i*n;
        while(tmp){
            Log[tmp%10]=true;
            tmp/=10;
        }
        for(int j=0; j<10; j++){
            if(!Log[j]){log=false;break;}
        }
        if(log)return n*i;
    }
}

int main(){
//    ifstream cin("A-large.in");
//    ofstream cout("data.txt");
    int t, n;
    cin>>t;
    for(int i=1; i<=t; i++){
        cin>>n;
        if(n==0)cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        else cout<<"Case #"<<i<<": "<<count(n)<<endl;
    }
}
