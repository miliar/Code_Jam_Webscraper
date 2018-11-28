#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <iomanip>
#include<cstring>
using namespace std;
#define rep(i,n) for(int i = 0; i < n; ++i)
#define pii pair<int,int>


void tobs(string s, bool bs[],int &count){
    rep(i,s.size()){
        if(s[i]=='-'){
            bs[i]=true;
            count++;
        }
    }
}

int solve(int n,int &count,bool s[]){
    if(count==0) return n;
    bool col=s[0];
    int i=0;
    while(col==s[i]){i++;}
    rep(j,i){
        s[j]=!s[j];
        if(s[j]) count++;
        else count--;
    }

    return solve(n+1,count,s);
}

int main(){
    int M;
    cin>>M;
    rep(i,M){
        string s;
        cin>>s;

        bool bs[101]={};
        int count=0;
        tobs(s,bs,count);
        //cout<<":"<<count<<endl;

        cout<<"Case #"<<i+1<<": "<<solve(0,count,bs)<<endl;
    }

    return 0;
}
