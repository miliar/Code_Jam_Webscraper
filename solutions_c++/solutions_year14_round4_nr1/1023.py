#include<iostream>
#include<string>
#include<cstdio>
#include<cstring>
#include<fstream>
#include<algorithm>
#include<map>
#include<climits>
#include<stdlib.h>
#include<vector>
#include<stack>
#include<queue>
#include<bitset>
#include<set>
#include<cmath>
#include<list>
using namespace std;
const int M = 103100;
const double eps = 1e-8;
const double dinf = 1e15;
const int inf = INT_MAX;

int n,x;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("aout.txt","w",stdout);
    int T;
    scanf("%d",&T);
    int cas = 1;
    while(T--){
        cout<<"Case #"<<cas<<": ";
        cin>>n>>x;
        vector<int> fl;
        fl.resize(n);
        for(int i = 0; i < n; i ++)
            cin>>fl[i];
        int l = 0, r = n - 1;
        sort(fl.begin(),fl.end());
        int ans = 0;
        while(l <= r){
            if(l == r){
                ans ++;break;
            }else if(l > r){
                break;
            }else{
                if(fl[l] + fl[r] > x){
                    r --;
                    ans ++;
                }else{
                    l ++;
                    r --;
                    ans ++;
                }
            }
        }
        cout<<ans<<endl;
        cas ++;
    }
    return 0;
}
