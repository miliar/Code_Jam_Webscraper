#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <vector>
#define LL long long
using namespace std;

vector<LL> hui;

bool isPa(LL num) {
    stringstream ss;
    ss<<num;
    string str;
    ss>>str;
    int sz=str.size();
    for(int i=0;i<sz/2;i++) {
        if(str[i]!=str[sz-1-i]) return false;
    }
    return true;
}

int main() {
    //freopen("p.txt","r",stdin);
    //freopen("s.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<11000000;i++) {
        if(isPa(i)) hui.push_back(i);
    }
    for(int cs=1;cs<=t;cs++) {
        LL a,b;
        cin>>a>>b;
        LL res=0;
        for(LL j=0;j<hui.size();j++) {
            LL i=hui[j];
            LL sq=i*i;
            if(sq<a) continue;
            if(sq>b) break;
            if(!isPa(i)) continue;
            if(!isPa(sq)) continue;
            res++;
        }
        cout<<"Case #"<<cs<<": "<<res<<endl;
    }
    return 0;
}
