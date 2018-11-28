#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <limits.h>
#include <iterator>

using namespace std;

typedef int ttyp;
#define forz(n) for(int i=0;i<n;i++)
#define forzo(j,n) for(int j=0;j<n;j++)
#define MP make_pair
#define sz(v) v.size()

long long mystoll(string s){
    long long ret;
    istringstream is(s);
    is>>ret;
    return ret;
}
vector<long long> conv(vector<string> vs){
    vector<long long> ret;
    forz(vs.size()){
        ret.push_back(mystoll(vs[i].substr(2)));
    }
    return ret;
}
int orig(vector<long long> va, vector<long long> vb){
    vector<bool> taken(1001,false);
    bool found;
    int ret=0;
    forz(va.size()){
        found=false;
        for(int j=0;j<vb.size() && !found;j++){
            if(!taken[j] && vb[j]>va[i]){
                taken[j]=true;
                found = true;
            }
        }
        if(!found){
            ret++;
        }
    }
    return ret;
}
int decp(vector<long long> va, vector<long long> vb){
    int ret = 0, ixa =0, ixb = vb.size()-1, n, iya;
    n = va.size();
    while(ixa<va.size() && va[ixa]<vb[0]){
        ixa++;
    }
    while(ixb>=0 && vb[ixb]>va[n-1]){
        ixb--;
    }
    iya = n - 1;
    while(iya>=ixa && ixb>=0){
        if(va[iya]>vb[ixb]){
            ret++;
            iya--;
        }
        ixb--;

    }
    return ret;
}

void doit(){
    int n, maxs=0, t;
    vector<string> va, vb;
    vector <long long> ia, ib;
    cin>>n;
    va.resize(n);
    vb.resize(n);
    forz(n){
        cin>>va[i];
        t = va[i].size();
        maxs = max(maxs, t);
    }
    forz(n){
        cin>>vb[i];
        t = vb[i].size();
        maxs = max(maxs, t);
    }
    forz(n){
        while(va[i].size()<maxs)
            va[i] = va[i] + '0';
        while(vb[i].size()<maxs)
            vb[i] = vb[i] + '0';
    }
    ia = conv(va);
    ib = conv(vb);
    sort(ia.begin(),ia.end());
    sort(ib.begin(),ib.end());
    cout<<decp(ia,ib)<<" ";
    cout<<orig(ia,ib)<<endl;
    return;
}
int main(){
    int tc;
    cin>>tc;
    for(int i=1;i<=tc;i++){
      cout<<"Case #"<<i<<": ";
      doit();
    }
    return 0;
}

