#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string.h>
#include <string>
#include <stdio.h>
#include <fstream>
using namespace std;

double w,h,d,n,t;string s;
int a[1010];
vector<pair<double, double>>an;
int max(int a,int b){
    if(a>b)return a;
    return b;
}
int main() {
    
    ifstream in;
    ofstream out;
    in.open("/Users/apple/Desktop/testcpp/A-large.in");
    out.open("/Users/apple/Desktop/testcpp/a.txt");
    in>>t;
    int _=1;
    while(t--){
        in>>n>>s;
        memset(a,0,sizeof((a)));
        
        for(int i=1;i<(int)s.length();++i)
            a[i]=a[i-1]+s[i-1]-'0';
        w=0;h=0;
        for(int i=(int)s.length()-1;i;--i)
            if(s[i]!='0')
            {
                w+=max(0,i-a[i]-h);
                h+=max(0,i-a[i]-h);
            }
        out<<"Case #"<<_++<<": "<<w<<endl;
    }
        
    return 0;
}
