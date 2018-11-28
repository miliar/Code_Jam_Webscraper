//
//  main2016.cpp
//  Codejam2015
//
//  Created by stoness on 16/4/9.
//  Copyright © 2016年 sts. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <bitset>

using namespace std;

int p1()  {
    int a(0);
    int n(0);
    bitset<10> f;
    cin>>a;
    if (a==0) return -1;
    for (int i=1,n=a; i<10000; ++i,n+=a) {
        for (int j(n); j>0; j/=10) {
            f.set(j%10);
        }
        if (f.all()) {
            return n;
        }
    }
    return -1;
}

int p2()  {
    int res(0);
    string s;
    cin>>s;
    //cout<<s.length()<<' '<<s;
    if (s[0]=='-') ++res;
    for (int i(1); i<s.length(); ++i) {
        if (s[i-1]=='+' && s[i]=='-') res+=2;
    }
    return res;
}

int main(int argc, const char * argv[]) {
    int T(0);
    int r1(0);
    cin>>T;
    for (int i=0;i<T;++i) {
        r1=p2();
        cout<<"Case #"<<i+1<<": "<<r1<<endl;
    }
    return 0;
}