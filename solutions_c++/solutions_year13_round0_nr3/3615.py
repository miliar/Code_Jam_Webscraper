#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<cmath>
using namespace std;
vector<long long> pals;
bool isp(int n) {
    stringstream ss;
    int i,j;
    string str;
    ss<<n;
    str=ss.str();
    i=0;
    j=str.size()-1;
    while(i<j) {
        if(str[i]!=str[j]) return 0;
        i++;
        j--;
    }
    return 1;
}
void generatePals(long long n) {
    long long start,i;
    if(pals.size()==0) {
        start=1;
    } else {
        start=pals[pals.size()-1]+1;
    }
    for(i=start; i<=n; i++) {
        if(isp(i) && isp(i*i)) pals.push_back(i);
    }
}
long long solve(long long A, long long B) {
    long long aroot, broot, aind=-1, bind=-1, i,sz;
    aroot=(long long)sqrt(A);
    if(aroot*aroot<A) aroot++;
    broot=(long long)sqrt(B);
    sz=pals.size();
    if(pals[0]>=aroot) aind=0;
    else {
        for(i=0; i<sz-1; i++) {
            if(pals[i]<aroot && pals[i+1]>=aroot) {
                aind=i+1;
                break;
            }
        }
    }
    if(aind==-1) {
        aind=sz;
    }
    i=(aind>0)?aind-1:0;
    for(; i<sz-1; i++) {
        if(pals[i]<=broot && pals[i+1]>broot) {
            bind=i;
            break;
        }
    }
    if(bind==-1) bind=sz-1;
    return bind-aind+1;    
}
int main() {
    int T,i;
    long long A,B,s;
    cin>>T;
    for(i=1; i<=T; i++) {
        cin>>A>>B;
        s=(long long)sqrt(B);
        if(pals.size()==0 || s>pals[pals.size()-1]) {
            generatePals(s);
        }
        cout<<"Case #"<<i<<": "<<solve(A,B)<<endl;
    }
    return 0;
}
    
