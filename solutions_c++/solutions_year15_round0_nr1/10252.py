/* 
 * File:   main.cpp
 * Author: shankar
 *
 * Created on 11 April, 2015, 1:31 PM
 */

#include <bits/stdc++.h>
using namespace std;

int main() {
    //ios_base::sync_with_stdio(false);
    //cin.tie(0);
    int i,j,k,l,m,n,t;
    cin>>t;
    string a;
    vector<int> ans;
    for(i=1;i<=t;i++){
        cin>>n>>a;
        int s=0;
        m=0;
        for(j=0;j<a.size();j++){
            k=a[j]-'0';
            if(k){
                if(s<j){
                    m+=j-s;
                    s=s+(j-s);
                }
                s+=k;
            }
        }
        ans.push_back(m);
    }
    for(i=0;i<ans.size();i++){
        cout<<"Case #"<<i+1<<": "<<ans[i]<<"\n";
    }
    return 0;
}

