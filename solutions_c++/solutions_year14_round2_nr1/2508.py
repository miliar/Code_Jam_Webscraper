//
//  aa.cpp
//  LeetCode
//
//  Created by chushumo on 5/3/14.
//  Copyright (c) 2014 Chu Shumo. All rights reserved.
//

#include <iostream>
#include <vector>
#include <stack>
#include <cstdlib>

using namespace std;

int repeat(vector<vector<int> > & v){
    vector<vector<int> > transform(v[0].size());
    int result = 0;
    for (int i=0; i<v[0].size();i++) {
        for (int j=0; j<v.size(); j++) {
            transform[i].push_back(v[j][i]);
        }
    }
    
    for (int i=0; i<transform.size(); i++) {
        sort(transform[i].begin(), transform[i].end());
        int n = (int)transform[i].size();
        int median = transform[i][n/2];
        for (int j=0; j<transform[i].size(); j++) {
            result += abs(transform[i][j]-median);
        }
    }
    return result;
}

int main(){
    int num_case;
    cin>>num_case;
    for (int i=0;i<num_case; ++i) {
        int num;
        cin>>num;
        vector<char> first;
        vector<vector<int> > cv(num);
        bool noanswer = false;
        for (int j=0; j<num; ++j) {
            if (num == 1) {
                break;
            }
            string str;
            cin>>str;
            if(j==0){
                char last = str[0];
                int counter = 0;
                for (int k=0; k<str.length(); ++k) {
                    char cur = str[k];
                    if(cur!=last){
                        first.push_back(last);
                        cv[0].push_back(counter);
                        counter = 1;
                        last = cur;
                    }
                    else{
                        counter++;
                    }
                    if (k==str.length()-1) {
                        cv[0].push_back(counter);
                        first.push_back(cur);
                    }
                }
            }
            else{
                int k = 0;
                int dc = 0;
                int pos = 0;
                char last = str[0];
                if(last != first[0]){
                    noanswer = true;
                    break;
                }
                while(k<str.length()){
                    if(str[k]==last){
                        dc++;
                    }
                    else{
                        pos ++;
                        cv[j].push_back(dc);
                        dc=1;
                        if(pos>=first.size() || str[k]!=first[pos]){
                            noanswer = true;
                            break;
                        }
                        last = str[k];
                    }
                    if(k == str.length()-1){
                        cv[j].push_back(dc);
                    }
                    k++;
                }
                if(cv[j].size()!=cv[0].size()){
                    noanswer = true;
                }
                
                if (noanswer) {
                    break;
                }
            }
        }
        
        cout<<"Case #"<<i+1<<": ";
        if (num ==1) {
            cout<<"0"<<endl;
        }
        else if (noanswer) {
            cout<<"Fegla Won"<<endl;
        }
        else{
            
            cout<<repeat(cv)<<endl;
        }
        /*
        if (i==79) {
        
         for (int j=0; j<cv.size(); ++j) {
         for (int k=0; k<cv[j].size(); ++k) {
         cout<<cv[j][k]<<" ";
         }
         cout<<endl;
         }
        }
         */
        
    }
}