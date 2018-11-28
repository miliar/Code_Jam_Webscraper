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

int main(int argc, const char * argv[]) {
    int T(0);
    int r1(0);
    cin>>T;
    for (int i=0;i<T;++i) {
        r1=p1();
        cout<<"Case #"<<i+1<<": "<<((r1==-1)?"INSOMNIA":to_string(r1))<<endl;
    }
    return 0;
}