//
//  main.cpp
//  codejam 1B1
//
//  Created by Zulkarnine Mahmud on 5/4/13.
//  Copyright (c) 2013 Zulkarnine Mahmud. All rights reserved.
//

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <deque>
#include <list>
#include <ctime>

using namespace std;


void simulate(long long &M,long long &R,vector<long long> &given){
    long long virM1=M;
    long long virM2=M;
    long long result1=R;
    long long result2=R;
    vector<long long>all=given;
    vector<long long>all2=given;
    
        while (all.front()>virM1&&all.size()>0) {
            virM1+=(virM1-1);
            result1++;
        }
marker2:
    while (all.size()>0) {
        while ((all.front()<virM1)&&(all.size()>0)) {
            virM1+=all.front();
            all.erase(all.begin());
            
        }
        if (all.size()==0) {
            break;
        }
        if (all.front()<(virM1+virM1-1)) {
            virM1+=(virM1-1);
            result1++;
            goto marker2;
        }else{
            simulate(virM1,result1,all);
            
        }
        
    }
   
        while (all2.front()>virM2&&all2.size()>0) {
            all2.erase(all2.begin());
            result2++;
        }
    
    

marker3:
    while (all2.size()>0) {
        while ((all2.front()<virM2)&&(all2.size()>0)) {
            virM2+=all2.front();
            all.erase(all2.begin());
            
        }
        if (all2.size()==0) {
            break;
        }
        if (all2.front()<(virM2+virM2-1)) {
            virM2+=(virM2-1);
            R++;
            goto marker3;
        }else{
            simulate(virM2,result2,all2);
            
        }
        
    }
    
    
    M=(result1<result2? virM1:virM2);
    R=(result1<result2? result1:result2);
    given=(result1<result2? all:all2);
    
    
}


int main(int argc, const char * argv[])
{
    int T,cas=1;
    //test
    freopen("/Users/rezan_mahmud/Desktop/A-large.in", "r", stdin);
    freopen("/Users/rezan_mahmud/Desktop/test.out", "w", stdout);
    
//    //small input
//    freopen("small.in", "r", stdin);
//    freopen("small.out", "w", stdout);
//    
//    //large input
//    freopen("large.in", "r", stdin);
//    freopen("large.out", "w", stdout);

    cin>>T;
    while (T--) {
        //variables
        long long M,N;
        cin>>M>>N;
        vector<long long>all;
        long long temp;
        for (long long i=0; i<N; i++) {
            cin>>temp;
            all.push_back(temp);
        }
        
        //solving
        long long result=0;
        if (M==1) {
            result=N;
            goto exceptional;
        }
        sort(all.begin(), all.end());
    marker:
        while (all.size()>0) {
            while ((all.front()<M)&&(all.size()>0)) {
                M+=all.front();
                all.erase(all.begin());
                
            }
            if (all.size()==0) {
                break;
            }
            if ((all.front()<(M+M-1))) {
                M+=(M-1);
                result++;
                goto marker;
            }else if(all.front()>=M){
                
                simulate(M,result,all);
                
            }
            
        }
        
    exceptional:
        //output
        cout<<"Case #"<<cas++<<": "<<result<<endl;
        
        
    }
//    t=(clock()-t);
//    cout<<"it took total"<<float(t)/CLOCKS_PER_SEC<<"seconds";
    
    return 0;
}

