#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
using namespace std;
bool np[(int)1e8+1];
int ans;
vector<int> prms;
void sieve(){
    np[0]=np[1]=1;
    for(int i=2; i*i<=1e8; i++){
        if(!np[i])
        for(int j=i*i; j<=1e8; j+=i){
            np[j]=1;
        }
    }
    prms.push_back(2);
    for(int i=3; i<=1e8; i+=2) if(!np[i]) prms.push_back(i);
}
long long tobaseX(string s, int base){
    long long ret=0,tmp=1;
    for(int i=(int)s.size()-1; i>=0; i--){
        ret+=(s[i]-'0')*tmp;
        tmp*=base;
    }
    return ret;
}
void f(string s, int n){
    if(!ans) return;
    if(!n) {
        if(s[s.size()-1]=='0') return;
        vector<int> vec;
        for(int i=2; i<=10; i++){
            long long tmp=tobaseX(s, i);
            bool flag=0;
            for(int i=0; i<prms.size(); i++){
                if(tmp!=prms[i] && tmp%prms[i]==0){
                    flag=1;
                    vec.push_back(prms[i]);
                    break;
                }
            }
            if(!flag) return;
        }
        cout<<s;
        for(int i=0; i<9; i++) {
            cout<<' '<<vec[i];
        }
        cout<<endl;
        ans--;
        return;
    }
    f(s+'0',n-1);
    f(s+'1',n-1);
}
int main(){
    //freopen("B-large.txt","r",stdin);
    freopen("outCG.txt","w",stdout);
    sieve();
    int t;
    cin>>t;
    for(int tc=1; tc<=t; tc++){
        int n,j;
        cin>>n>>j;
        ans=j;
        cout<<"Case #"<<tc<<":\n";
        f("1",n-1);
    }
}