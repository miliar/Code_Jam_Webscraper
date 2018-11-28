//
//  main.cpp
//  d
//
//  Created by Zhou Sun on 5/31/14.
//  Copyright (c) 2014 Zhou Sun. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

int ts,m,n,mx,mt;
string s[1000];
int f[1000];
int common(string& a, string& b){
    int k=0;
    while (k<a.size()&& k<b.size()&&a[k]==b[k]) {
        k++;
    }
    return k;
}
int solve(){
    int sum=0;
    for(int i=0;i<n;i++){
        vector<string> ss;
        for (int j=0; j<m;j++) {
            if (f[j]==i) {
                ss.push_back(s[j]);
            }
        }
        sort(ss.begin(), ss.end());
        if(ss.size())sum+=ss[0].size()+1;
        for (int i=1; i<ss.size(); i++) {
            sum+=ss[i].size()-common(ss[i-1],ss[i]);
        }
    }
    return sum;
}
void dfs(int k){
    if (k==m) {
        int s=solve();
        if (s==mx) {
            mt++;
        }
        if (s>mx) {
            mx=s;
            mt=1;
        }
        return;
    }
    for (int i=0; i<n; i++) {
        f[k]=i;
        dfs(k+1);
    }
}
int main(int argc, const char * argv[])
{
    cin>>ts;
    for (int tt=1; tt<=ts; tt++) {
        cin>>m>>n;
        for(int i=0;i<m;i++)
            cin>>s[i];
        mt=0;
        mx=0;
        dfs(0);
        cout<<"Case #"<<tt<<": "<<mx<<' '<<mt<<endl;
    }
    return 0;
}

