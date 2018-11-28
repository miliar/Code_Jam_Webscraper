//
//  main.cpp
//  Infinite house of pancakes
//
//  Created by Shreyas Sinha on 11/04/15.
//  Copyright (c) 2015 Shreyas Sinha. All rights reserved.
//


#include <iostream>
#include <fstream>
#include <set>
using namespace std;
multiset<int> s,s2;
multiset<int>::iterator r;
void relieve(int * a,int b){
    if ((*a)>b) {
        *a=b;
    }
}
int main() {
    int t,a,d,ans,num,special;
    ofstream outfile;
    ifstream infile;
    infile.open("B-small-attempt1.in");
    outfile.open("output.in");
    infile>>t;
    for (int k=1; k<=t; k++) {
        infile>>d;
        for (int i=0; i<d; i++) {
            infile>>a;
            s.insert(a);
            s2.insert(a);
        }
        r=s.end();
        r--;
        ans=(*r);
        special=0;
        while (special<ans) {
            num=(*r);
            special++;
            s.erase(r);
            s.insert(num/2);
            s.insert(num-(num/2));
            r=s.end();
            r--;
            relieve(&ans,special+(*r));
        }
        r=s2.end();
        r--;
        num=(*r);
        s2.erase(r);
        s2.insert(num/3);
        num-=(num/3);
        s2.insert(num/2);
        s2.insert(num-(num/2));
        special=2;
        r=s2.end();
        r--;
        relieve(&ans,special+(*r));
        while (special<ans) {
            num=(*r);
            special++;
            s2.erase(r);
            s2.insert(num/2);
            s2.insert(num-(num/2));
            r=s2.end();
            r--;
            relieve(&ans,special+(*r));
        }

        outfile<<"Case #"<<k<<": "<<ans<<"\n";
        s.clear();
        s2.clear();
        
    }
    outfile.close();
    infile.close();
    return 0;
}
