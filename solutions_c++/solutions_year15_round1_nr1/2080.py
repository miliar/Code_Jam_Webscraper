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
#include <limits.h>
#define fir(i,n,m) for(int i=n;i<m;i++)
#define fdr(i,n,m) for(int i=n;i>=m;i--)
#define pb push_back
#define vi vector<int>
#define vs vector<string>
#define vll vector<long long>
#define sz(v) (int)v.size()
#define all(v) v.begin(),v.end()
using namespace std;

int main(){
    int t;
    cin>>t;
    int nCases=1;
    while(t--){
        int n;
        cin>>n;
        vll m;
        fir(i,0,n){
            long long x;
            cin>>x;
            m.pb(x);
        }
        long long ma=0,mi=0, mr=0;
        fir(i,1,sz(m)){
            if(m[i]<m[i-1]){
                mr=max(mr, m[i-1]-m[i]);
            }
        }
        //cout<<"Max rate: "<<mr<<endl;
        fir(i,0,sz(m)-1){
            ma+=min(m[i],mr);
        }
        fir(i,0,sz(m)-1){
            if(m[i+1]<m[i]){
                mi += (m[i]-m[i+1]);
            }
        }
        cout<<"Case #"<<nCases<<": "<<mi<<" "<<ma<<endl;
        nCases++;
    }
}
