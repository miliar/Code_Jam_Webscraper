/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: Administrator
 *
 * Created on 2016년 4월 10일 (일), 오전 10:06
 */

#include <cstdlib>
#include <set>
#include <cstdio>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

struct node {
    string v;
    int res;
};

int calc(string str) {
    queue<struct node> q;
    struct node n;
    n.v = str;
    n.res = 0;
    
    q.push(n);
    
    set<string> visit;
        
    while(!q.empty()) {
        struct node cur = q.front();
        q.pop();
        
        string cur_str = cur.v;
        bool success = true;
        for(int i=0;i<cur_str.size();i++) {
            if(cur_str[i] == '-') {
                success = false;
                break;
            }
        }
        
        if(success) {
            return cur.res;
        }
        
        if(visit.find(cur.v) != visit.end()) {
            continue;
        }
        
        visit.insert(cur_str);
        
        for(int i=0;i<cur_str.size();i++) {
            string str1 = cur_str.substr(0, i+1);
            string str2 = cur_str.substr(i+1);
            
            for(int j=0;j<str1.size();j++){
                if(str1[j]=='-')
                    str1[j]='+';
                else
                    str1[j]='-';
            }
            
            struct node next;
            next.v = str1+str2;
            next.res = cur.res+1;
            
            q.push(next);
        }
    }
    
    return -1;
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int T;
    scanf("%d", &T);
    
    char str[101];
    for(int i=1; i<=T; i++) {
        scanf("%s", str);
        printf("Case #%d: %d\n",i, calc(str));
    }
    
    return 0;
}

