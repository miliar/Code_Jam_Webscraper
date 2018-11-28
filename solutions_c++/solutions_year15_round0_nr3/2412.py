//
//  main.cpp
//  CodeJamProbC
//
//  Created by Mihai Visuian on 11/04/2015.
//  Copyright (c) 2015 Mihai Visuian. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>

using namespace std;

ifstream fin("f.in");
ofstream fout("f.out");

typedef pair<int,int> Symbol;
long long t,l,x;
string s;
char letters[] = {'1','i','j','k'};

int getIndex(char c) {
    for(int i = 0; i < 4; i++ ) {
        if(c==letters[i])
            return i;
    }
    return -1;
}

Symbol multiply(Symbol a, Symbol b) {
    
    int sign = a.first * b.first;
    if(a.second == 0) {
        return make_pair(sign, b.second);
    }
    if(b.second == 0) {
        return make_pair(sign, a.second);
    }
    if(a.second == b.second) {
        return make_pair(-sign, 0);
    }
    if(a.second == 1) {
        if(b.second == 2)
            return make_pair(sign, 3);
        if(b.second == 3)
            return make_pair(-sign, 2);
    }
    if(a.second == 2) {
        if(b.second == 1)
            return make_pair(-sign, 3);
        if(b.second == 3)
            return make_pair(sign, 1);
    }
    if(a.second == 3) {
        if(b.second == 1)
            return make_pair(sign, 2);
        if(b.second == 2)
            return make_pair(-sign, 1);
    }
    return make_pair(1,0);
}

int main(int argc, const char * argv[]) {

    fin>>t;
    for (int i=1; i<=t; i++) {
        fin>>l>>x;
        x = min(x,20+x%4);
        fin>>s;
        string st=s;
        while (--x) {
            s+=st;
        }
        Symbol result = make_pair(1,0);
        int pos1=0;
        for(int k = 0; k < s.length(); k++ ) {
            result = multiply(result, make_pair(1,getIndex(s[k])));
            if(result == make_pair(1,getIndex('i')) && !pos1) {
                pos1 = k;
            }
        }

        Symbol result2 = make_pair(1,0);
        int pos2=-1;
        for(int k = (int)s.length()-1; k >= 0; k--) {
            result2 = multiply(make_pair(1, getIndex(s[k])), result2);
            if(result2 == make_pair(1, getIndex('k')) && pos2==-1) {
                pos2=k;
            }
        }
        
        //cout<<result.first<<' '<<result.second<<' '<<pos1<<' '<<pos2<<'\n';
        
        if(result != make_pair(-1,0) ) {
            fout << "Case #"<<i<<": NO\n";
            continue;
        }
        
        if(pos1 > pos2) {
            fout << "Case #"<<i<<": NO\n";
            continue;
        }
        
        if(pos1 < pos2 && result == make_pair(-1, 0) && result2 == make_pair(-1, 0)) {
            fout << "Case #"<<i<<": YES\n";
            continue;
        }
    }
    
    fin.close();
    fout.close();
    return 0;
}
