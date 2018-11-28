//
//  main.cpp
//  c
//
//  Created by Zhou Sun on 6/14/14.
//  Copyright (c) 2014 Zhou Sun. All rights reserved.
//

#include <iostream>
#include <map>
using namespace std;
int ts,n;
string s[100];
int d[100];
map<int,int> id;
int mi;
void dfs(int t){
    if (t==n) {
        int sum=0;
        for (auto it=id.begin(); it!=id.end(); it++) {
            if (it->second==1) {
                sum++;
            }
            
        } 
        if(mi>sum)mi=sum;
        return;
    }
    if (d[t]) {
        if (s[t]=="E") {
            if (id[d[t]]==1) {
                return;
            }
            else{
                int temp=id[d[t]];
                id[d[t]]=1;
                dfs(t+1);
                id[d[t]]=temp;

                return;
            }
        }
        if (id[d[t]]==0) {
            return;
        }
        else{
            int temp=id[d[t]];
            id[d[t]]=0;
            dfs(t+1);
            id[d[t]]=temp;
            return;
        }
    }
    for (auto it= id.begin(); it!=id.end(); it++) {
        if (it->first>1001 && id[it->first-1]==-1) {
            break;
        }
        if (s[t]=="E") {
            if (it->second==1) {
                continue;
            }
            else{
                int temp=it->second;
                it->second=1;
                dfs(t+1);
                it->second=temp;
                continue;
            }
        }
        if (it->second==0) {
            continue;
        }
        else{
            int temp=it->second;
            it->second=0;
            dfs(t+1);
            it->second=temp;
            continue;

        }

    }
    
}
int main(int argc, const char * argv[])
{
    cin>>ts;
    for (int tt=1; tt<=ts; tt++) {
        cin>>n;
        int m=0;
        id.clear();
        for (int i=0; i<n; i++) {
            cin>>s[i]>>d[i];
            if (d[i]==0) {
                m++;
                id[1000+m]=-1;
            }
            else{
                id[d[i]]=-1;
            }
                
        }
        mi=100000;
        dfs(0);
        cout<<"Case #"<<tt<<": ";
        if (mi==100000) {
            cout<<"CRIME TIME\n";
        }
        else{
            cout<<mi<<endl;
        }
    }

    return 0;
}

