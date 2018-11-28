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
#define sz(v) (int)v.size()
#define all(v) v.begin(),v.end()
using namespace std;

int main(){
    int t;
    int nCases=1;
    scanf("%d", &t);
    while(t--){
        int d;
        int mx=0;
        vi ps;
        scanf("%d", &d);
        for(int i=0;i<d;i++){
            int n;
            scanf("%d", &n);
            mx=max(n,mx);
            ps.pb(n);
        }
        if(mx==0){
            printf("Case #%d: 0\n",nCases);
            //cout<<"Case #"<<nCases<<": 0"<<endl;
            continue;
        }
        int res=mx;
        for(int i=1;i<=mx;i++){
            int st=0;
            for(int j=0;j<sz(ps);j++){
                if(ps[j]%i==0){
                    st+=((ps[j]/i)-1);
                }
                else{
                    st+=(ps[j]/i);
                }
            }
            res = min(st+i,res);
        }
        printf("Case #%d: %d\n",nCases, res);
        //cout<<"Case #"<<nCases<<": "<<res<<endl;
        nCases++;
    }
    return 0;
}
