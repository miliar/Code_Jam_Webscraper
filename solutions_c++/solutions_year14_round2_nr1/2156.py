//
//  main.cpp
//  1B_A
//
//  Created by Zulkarnine on 5/4/14.
//  Copyright (c) 2014 Zulkarnine Mahmud. All rights reserved.
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


using namespace std;

typedef int int_type;

int maxLimit;


class info {
    public:
    string s;
    vector<char> chars;
    vector<int> count;
    
    info(){
        
    }
    
    info(string s){
        this->s=s;
        
        for (int i=0; i<s.length(); i++) {
            if (chars.empty()) {
                chars.push_back(s[i]);
                count.push_back(1);
            }else{
                if (s[i]==chars.back()) {
                    count.back()++;
                }else{
                    chars.push_back(s[i]);
                    count.push_back(1);
                }
            }
            
        }
    }
};


void printImpossible(){
     cout<<"Fegla Won\n";
    
}

void solveCase(vector<info> allInfos){
    bool flag=true;
    int size=allInfos[0].chars.size();
    for (int i=0; i<allInfos.size(); i++) {
        if (allInfos[i].chars.size()!=size) {
            printImpossible();
            return;
        }
    }
    
    for (int i=1; i<allInfos.size(); i++) {
        for (int j=0; j<allInfos[0].chars.size(); j++) {
            if (allInfos[i].chars[j]!=allInfos[0].chars[j]) {
                printImpossible();
                return;
            }
        }
    }
    
    vector<int> average;
    for (int i=0; i<allInfos[0].chars.size(); i++) {
        int count=0;
        for (int j=0; j<allInfos.size(); j++) {
            count+=allInfos[j].count[i];
        }
        average.push_back(count/allInfos.size());
    }
    
    int totalCount=0;
    for (int i=0; i<allInfos[0].chars.size(); i++) {
        int count=0;
        for (int j=0; j<allInfos.size(); j++) {
            count+=abs(average[i]-allInfos[j].count[i]);
        }
        totalCount+=count;
    }
    
    cout<<totalCount<<"\n";
   
}

int main(int argc, const char * argv[])
{
    int T;
    int cas=0;
    //==============FINAL OUT================
        freopen("A-small-attempt0.in.txt", "r", stdin);
        freopen("test_a.out", "w", stdout);
    
    
    //================TEST==================
//    freopen("/Users/rezan_mahmud/Desktop/A-small-attempt0.in.txt", "r", stdin);
//    freopen("/Users/rezan_mahmud/Desktop/test_a.out", "w", stdout);
    
    
    cin>>T;
    vector<long long> allInput;
    
    while (T--) {
        int N;
        cin>>N;
        
        vector<info> allStrings;
        
        for (int i=0; i<N; i++) {
            string s;
            cin>>s;
            allStrings.push_back(info(s));
        }
        
        printf("Case #%d: ",++cas);
        solveCase(allStrings);
    }
    
    return 0;
}

