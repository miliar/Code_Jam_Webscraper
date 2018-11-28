#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <complex>
#include <bitset>
#include <iomanip>
#include <utility>

#define xx first
#define yy second
#define ll long long
#define ull unsigned long long
#define pb push_back
#define pp pop_back
#define pii pair<int,int>
#define vi vector<int>
#define mp make_pair
using namespace std;
const int maxn=10000+10;
int t;
int n,x;
int a[maxn];
int ans;
int main(){
    ifstream cin("1.in");
    ofstream cout("1.out");
    cin>>t;
    for(int l=1;l<=t;l++){
        memset(a,0,sizeof(a));
        ans=0;
        cin>>n>>x;
        for(int i=1;i<=n;i++)cin>>a[i];
        sort(a+1,a+1+n);
        int p=1;
        for(int i=n;i>=1;i--){
            if(i==p){
                ans++;
                break;
            }
            if(i<p)break;
            if(a[i]+a[p]<=x){
                ans++;
                p++;
            }
            else{
                ans++;
            }
        }
        cout<<"Case #"<<l<<": "<<ans<<endl;
    }
}
