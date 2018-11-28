#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <string>
#include <fstream>
#include <vector>
#include <cstdio>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
using namespace std;
#define INF 0x3f3f3f3f
const int N=105;
const int mod=1e9+7;

int main() {
    int t;
    ifstream ifile;
    ofstream ofile;
    ofile.open("/Users/lijiechen/Downloads/2.txt",ios::out);
    ifile.open("/Users/lijiechen/Downloads/A-large.in.txt",ios::out);
    ifile>>t;
    int kase=0;
    string s;
    int low[30];
    while (t--) {
        kase++;
        ifile>>s;
        memset(low, 0, sizeof(low));
        for (int i=0; i<s.length(); i++) {
            low[s[i]-'A']++;
        }
        ofile<<"Case #"<<kase<<": ";
        int sum[30];
        sum['Z'-'A']=low['Z'-'A'];
        low['Z'-'A']=0,low['E'-'A']-=sum['Z'-'A'],low['R'-'A']-=sum['Z'-'A'],low['O'-'A']-=sum['Z'-'A'];
        
        sum['W'-'A']=low['W'-'A'];
        low['T'-'A']-=sum['W'-'A'];low['W'-'A']-=sum['W'-'A'];low['O'-'A']-=sum['W'-'A'];
        
        sum['U'-'A']=low['U'-'A'];
        low['F'-'A']-=sum['U'-'A'];low['O'-'A']-=sum['U'-'A'];low['U'-'A']-=sum['U'-'A'];low['R'-'A']-=sum['U'-'A'];
        
        sum['X'-'A']=low['X'-'A'];
        low['S'-'A']-=sum['X'-'A'];low['I'-'A']-=sum['X'-'A'];low['X'-'A']-=sum['X'-'A'];
        
        sum['G'-'A']=low['G'-'A'];
        low['E'-'A']-=sum['G'-'A'];low['I'-'A']-=sum['G'-'A'];low['G'-'A']-=sum['G'-'A'];low['H'-'A']-=sum['G'-'A'];low['T'-'A']-=sum['G'-'A'];
    
        sum['O'-'A']=low['O'-'A'];
        low['O'-'A']-=sum['O'-'A'];low['N'-'A']-=sum['O'-'A'];low['E'-'A']-=sum['O'-'A'];
        
        sum['H'-'A']=low['H'-'A'];
        low['T'-'A']-=sum['H'-'A'];low['H'-'A']-=sum['H'-'A'];low['R'-'A']-=sum['H'-'A'];low['E'-'A']-=2*sum['H'-'A'];
        
        sum['F'-'A']=low['F'-'A'];
        low['F'-'A']-=sum['F'-'A'];low['I'-'A']-=sum['F'-'A'];low['V'-'A']-=sum['F'-'A'];low['E'-'A']-=sum['F'-'A'];
        
        sum['S'-'A']=low['S'-'A'];
        low['S'-'A']-=sum['S'-'A'];low['E'-'A']-=2*sum['S'-'A'];low['V'-'A']-=sum['S'-'A'];low['N'-'A']-=sum['S'-'A'];
        
        sum['I'-'A']=low['I'-'A'];
        
        for (int i=0; i<sum['Z'-'A']; i++) {
            ofile<<"0";
        }
        for (int i=0; i<sum['O'-'A']; i++) {
            ofile<<"1";
        }
        for (int i=0; i<sum['W'-'A']; i++) {
            ofile<<"2";
        }
        for (int i=0; i<sum['H'-'A']; i++) {
            ofile<<"3";
        }
        for (int i=0; i<sum['U'-'A']; i++) {
            ofile<<"4";
        }
        for (int i=0; i<sum['F'-'A']; i++) {
            ofile<<"5";
        }
        for (int i=0; i<sum['X'-'A']; i++) {
            ofile<<"6";
        }
        for (int i=0; i<sum['S'-'A']; i++) {
            ofile<<"7";
        }
        for (int i=0; i<sum['G'-'A']; i++) {
            ofile<<"8";
        }
        for (int i=0; i<sum['I'-'A']; i++) {
            ofile<<"9";
        }
        ofile<<endl;
    }
    return 0;
}