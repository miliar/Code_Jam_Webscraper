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
vector<int> f;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("aout.txt","w",stdout);
    int C;
    cin>>C;
    int cas = 1;
    while(C--){
        cout<<"Case #"<<cas<<": ";
        cin>>n>>x;
        int l = 0, r = n - 1;
        f.resize(n);
        for(int i = 0; i < n; i ++)
            cin>>f[i];
        sort(f.begin(),f.end());
        int ans = 0;
        while(l <= r){
            if(l == r){
                ans ++;break;
            }else if(l > r){
                break;
            }else{
                if(f[l] + f[r] > x){
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
