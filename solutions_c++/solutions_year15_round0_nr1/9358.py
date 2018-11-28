//
//  main.cpp
//  codejam
//
//  Created by blade on 3/2/15.
//  Copyright (c) 2015 blade. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <unordered_set>

using namespace std;


int main(int argc, const char * argv[]) {
    // insert code here...
    
    fstream fin("/Users/blade/Documents/xcode/codejam/StandingOvation/A-small-attempt0.in.txt",fstream::in);//
    fstream fout("/Users/blade/Documents/xcode/codejam/StandingOvation/A-small-attempt0.out.txt",fstream::out);
    int T;
    
    fin>>T;
    cout<<T<<endl;
    for(int t=1; t<=T; ++t){
        int N;
        fin>>N;
        string levels;
        fin>>levels;
        vector<int> sl(N+1,0);
        for(int i=0; i<levels.size(); ++i){
            sl[i] = levels[i]-'0';
        }
        if(N == 0){
            fout<<"Case #"<<t<<": "<<0<<endl;
            cout<<"Case #"<<t<<": "<<0<<endl;
        }
        else{
            int tot = sl[0];
            int res = 0;
            for(int i=1; i<sl.size(); ++i){
                if(tot<i){
                    res += i-tot;
                    tot = i;
                }
                tot += sl[i];
                //cout<<tot<<endl;
            }
            fout<<"Case #"<<t<<": "<<res<<endl;
            cout<<"Case #"<<t<<": "<<res<<endl;
        }
    }
    //  fout<<"Case #"<<t<<": "<<res<<endl;
    //cout<<"Case #"<<t<<": "<<res<<endl;
    
    
    fin.close();
    fout.close();
    cout<<"done"<<endl;
    return 0;
}
