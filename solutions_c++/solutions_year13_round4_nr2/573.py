//
//  main.cpp
//  B
//
//  Created by zhou on 13-6-1.
//  Copyright (c) 2013年 zhou. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int n;
string s2;
int toBinary(string s){

    string r="";
    int l=s.size()-1;
    while (s[l]=='0') {
        l--;
    }
    s[l]--;
    for (int i=l+1; i<s.size(); i++) {
        s[i]='9';
    }
    cout<<s<<endl;
    int flag=1;
    while (flag) {
        int t=0;
        flag=0;
        for (int i=0; i<s.size(); i++) {
            t+=s[i]-48;
            s[i]=t/2+48;
            if(s[i]!='0')flag=1;
            t=(t%2)*10;
        }
        r=char(t/10+48)+r;
    }
    
  cout<<r<<' ';
    int t=0;
    if (r.size()<n) {
        return 1;
    }
  
    while (r[t]!='0'&&t<r.size()) {
        t++;
    }
    return t+1;
    
}
int toBinary1(string s){
    
    string r="";
    int l=s.size()-1;
    int flag=1;
    while (flag) {
        int t=0;
        flag=0;
        for (int i=0; i<s.size(); i++) {
            t+=s[i]-48;
            s[i]=t/2+48;
            if(s[i]!='0')flag=1;
            t=(t%2)*10;
        }
        r=char(t/10+48)+r;
    }
    int t=0;
    if (r.size()>n) {
        return 0;
    }
    while (r.size()<n) {
        r='0'+r;
    }
    for (int i=0; i<n; i++) {
        r[i]='0'+'1'-r[i];
    }
    while (r[t]!='0'&&t<r.size()) {
        t++;
    }
    return t+1;
    
}
string getS(int l){
    string s="1";
    if (l>n) {
        l=n;
        for (int i=0; i<l; i++) {
            int t=0;
            for (int k=s.size()-1; k>=0; k--) {
                t+=(s[k]-48)*2;
                s[k]=t%10+48;
                t=t/10;
            }
            if (t) {
                s=char(t+48)+s;
            }
        }
        s[s.size()-1]-=1;

        return s;

    }
    for (int i=0; i<l; i++) {
        int t=0;
        for (int k=s.size()-1; k>=0; k--) {
            t+=(s[k]-48)*2;
            s[k]=t%10+48;
            t=t/10;
        }
        if (t) {
            s=char(t+48)+s;
        }
    }
    s[s.size()-1]-=2;
    return s;
    
}
string getL(int l){
    cout<<l;
    string s="1";
        for (int i=0; i<n; i++) {
            int t=0;
            for (int k=s.size()-1; k>=0; k--) {
                t+=(s[k]-48)*2;
                s[k]=t%10+48;
                t=t/10;
            }
            if (t) {
                s=char(t+48)+s;
            }
        }
    string s1="1";
    for (int i=0; i<l; i++) {
        int t=0;
        for (int k=s1.size()-1; k>=0; k--) {
            t+=(s1[k]-48)*2;
            s1[k]=t%10+48;
            t=t/10;
        }
        if (t) {
            s1=char(t+48)+s1;
        }
    }
    cout<<s<<endl<<s1;
    while (s1.size()<s.size()) {
        s1='0'+s1;
    }
    int t=0;
    for (int i=s.size()-1; i>=0; i--) {
        t=10+s[i]-s1[i]+t;
        s[i]=t%10+48;
        if (t<10) {
            t=-1;
        }
        else
            t=0;
    }
    while (s[0]=='0'&&s.size()>1) {
        s.erase(s.begin());
    }
    return s;
    
}

int main(int argc, const char * argv[])
{
    ifstream in("in.txt");
    ofstream out("out.txt");
    int ts;
    string p;
    in>>ts;
    for (int t=0; t<ts; t++) {
        in>>n>>p;
        out<<"Case #"<<t+1<<": ";
        out<<getS(toBinary(p))<<' ';
        out<<getL(toBinary1(p))<<endl;
        
    }

    return 0;
}

