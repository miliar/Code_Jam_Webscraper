#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <iterator>
#include <cmath>
#include <queue>
#include <algorithm>

using namespace std;

bool ispal(long long val){
    stringstream ss; 
    ss << val;
    string tmp;
    ss >> tmp;
    for (int i=0;i<tmp.size()/2;i++){
        if (tmp[i]!=tmp[tmp.size()-i-1]) return false;
    }
    return true;
}

long long calc(long long a){
    long long cnt=0;
    for (long long i=1;;i++){
        stringstream ss;
        ss << i;
        string tmp="",s="";
        ss >> tmp;
        for (int j=0;j<tmp.size();j++)
            s+=tmp[j];
        for (int j=0;j<tmp.size();j++)
            s+=tmp[tmp.size()-j-1];
        ss.clear();
        ss << s;
        long long val=0;
        ss >> val;
        if (val*val>a) break;
        if (ispal(val*val)) {
            cnt++;
        }
    }
    for (long long i=1;;i++){
        stringstream ss;
        ss << i;
        string tmp="",s="";
        ss >> tmp;
        for (int j=0;j<tmp.size();j++)
            s+=tmp[j];
        for (int j=1;j<tmp.size();j++)
            s+=tmp[tmp.size()-j-1];
        ss.clear();
        ss << s;
        long long val=0;
        ss >> val;
        
        if (val*val>a) break;
        if (ispal(val*val)) {
            cnt++;
        }
    }
    return cnt;
}

int main(){
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int T;
    cin >> T;
    for (int rt=1;rt<=T;rt++){
        long long A,B;
        cin >> A >> B;
        printf("Case #%d: %I64d\n" ,rt,calc(B)-calc(A-1));
    }
}
