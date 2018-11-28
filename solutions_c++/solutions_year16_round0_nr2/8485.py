//
//  main.cpp
//  GCJ2016
//
//  Created by Ningchen Ying on 4/9/16.
//  Copyright (c) 2016 Ningchen Ying. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
using namespace std;

int ans[2000];
int final;

vector<string> Q;
vector<int> Qn;

int tonum(string s){
    int res=0;
    for(int i=0;i<s.length();i++){
        if(s[i]=='-'){
            res=res*2+1;
        }else{
            res*=2;
        }
    }
    return res;
}

int bfs(string s){
    int cnt = 0;
    int l;
    l = s.length();
    Q.clear();
    Qn.clear();
    Q.push_back(s);
    Qn.push_back(0);
    int res=-1;
    if(tonum(s)==0) return 0;
    while(cnt<Q.size()){
        int p = Qn[cnt];
        string ss = Q[cnt];
        p++;
        for(int i = 1;i<=l;i++){
            string nows = "";
            string net;
            for(int j=0;j<i;j++){
                if(ss[j]=='+')
                    nows+='-';
                else nows+='+';
                net = nows;
                reverse(net.begin(), net.end());
            }
            for(int j=i;j<l;j++){
                net+=ss[j];
            }
            
            //cout<<net<<endl;
            int hh = tonum(net);
            if(hh==0){
                res = p;
                break;
            }
            if(ans[hh]>p){
                ans[hh]=p;
                Q.push_back(net);
                Qn.push_back(p);
            }
            if(res!=-1) break;
        }
        cnt++;
    }
    return res;
}

int main(int argc, const char * argv[]) {
    
    int T;
    freopen("/Users/YNingC/Documents/CodeForces/GCJ2016/GCJ2016/B-small-attempt0.in","r",stdin);
    freopen("/Users/YNingC/Documents/CodeForces/GCJ2016/GCJ2016/B-small-attempt0.out","w",stdout);
    cin>>T;
    string s;
    for(int icase = 1;icase<=T;icase++){
        cin>>s;
        int k;
        k = s.length();
        for(int i=0;i<=1100;i++){
            ans[i]=10000000;
        }
        int res = bfs(s);
        printf("Case #%d: ",icase);
        cout<<res<<endl;
    }
        
    return 0;
}
