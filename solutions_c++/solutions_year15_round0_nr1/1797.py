//
//  main.cpp
//  Ovation
//
//  Created by Loc Ngo on 4/10/15.
//  Copyright (c) 2015 Loc Ngo. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;
ifstream fin("/Users/locngo/Documents/Codejam/Ovation/A-large.in");
bool B[1001];
void process(int t){
    fill(B,B+1001,false);
    int n;
    fin>>n;
    string s;
    fin>>s;
    int m = s[0]-'0';
    int ret = 0;
    while(true){
        bool found = false;
        for(int i=1;i<=n;i++){
            if(s[i]!='0'&&i<=m&&!B[i]){
                B[i] = true;
                m+=s[i]-'0';
                found = true;
                break;
            }
        }
        if(!found){
            int minv = 1000000000;
            int index = -1;
            for(int i=1;i<=n;i++){
                if(s[i]!='0'&&!B[i]&&minv>(i-m)){
                    minv = i-m;
                    index = i;
                }
            }
            if(index==-1)
                break;
            B[index] = true;
            m+=s[index]-'0'+minv;
            ret+=minv;
        }
    }
    cout<<"Case #"<<t<<": "<<ret<<endl;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int T;
    fin>>T;
    for(int i=1;i<=T;i++)
        process(i);
    return 0;
}
