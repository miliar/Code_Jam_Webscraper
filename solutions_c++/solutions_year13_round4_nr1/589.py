//
//  main.cpp
//  a
//
//  Created by zhou on 13-6-1.
//  Copyright (c) 2013年 zhou. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <map>
#include <deque>
using namespace std;
int main(int argc, const char * argv[])
{
    ifstream in("in.txt");
    ofstream out("out.txt");
    int ts,n,m,o,e,p;


    in>>ts;
    for (int t=0; t<ts; t++) {
        in>>n>>m;
        map<int, int> op;
        map<int, int> ep;
        map<int, int> pp;
        deque<int>d;
    deque<int>dp;
        long long re=0;
        long long re1=0;
        for(int i=0;i<m;i++){
            in>>o>>e>>p;
            int k=e-o;
            re+=p*(n+n-k+1)*k/2;
            op[o]+=p;
            ep[o]+=0;
            ep[e]+=p;
            op[e]+=0;
            pp[o]=1;
            pp[e]=1;
        }
        map<int, int>::iterator it;
        for (it=pp.begin(); it!=pp.end(); it++) {
            int k=it->first;
            cout<<k<<' '<<op[k]<<' '<<ep[k]<<endl;
            if (op[k]>ep[k]){
                op[k]-=ep[k];
                ep[k]=0;
            }
            if (op[k]<ep[k]){
                ep[k]-=op[k];
                op[k]=0;
            }
            if (op[k]) {
                d.push_back(k);
                dp.push_back(op[k]);
            }
            if (ep[k]) {
                int t=ep[k];
                while (t>dp.back()) {
                    int tem=k-d.back();
                    re1+=dp.back()*(n+n-tem+1)*tem/2;
                    t-=dp.back();
                    d.pop_back();
                    dp.pop_back();
                }
                int tem=k-d.back();
                re1+=t*(n+n-tem+1)*tem/2;
                dp.back()-=t;
                cout<<re1<<' '<<re<<endl;
            }
            
        }
        out<<"Case #"<<t+1<<": "<<re-re1<<endl;
        
    }
    // insert code here...
    return 0;
}

