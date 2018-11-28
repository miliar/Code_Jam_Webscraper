#include<iostream>
#include<stdio.h>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<vector>
#include<stack>
#include<queue>
#include<iomanip>
#include<stdlib.h>
#include<set>
#include<map>
#include<fstream>
using namespace std;
int main() {
    ifstream in;
    ofstream out;
    in.open("B-large.in");
    out.open("resultBLARGE.txt");
    int t,kase=1;
    in >> t;
    string s;
    while(t--) {
        in >> s;
        int r = 0;
        int i=0;
        while(i < s.size()) {
            if(s[i] == '-') {
                r += 2;
                while(i < s.size() && s[i] == '-') i++;
            }
            else
                i++;
        }
        if(s[0] == '-')
            r--;
        out << "Case #" << kase << ": " << r <<endl;
        kase++;
        
    }
}