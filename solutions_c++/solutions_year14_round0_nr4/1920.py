#include<iostream>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<iomanip>

#define sd(x) scanf("%lld",&x)
#define MP make_pair
#define PB push_back
#define MOD 100000007
#define INF 100000007
#define M 1000000
#define F first
#define S second
#define ll long long
#define LL long long

using namespace std;
int n;
long double a[10000], b[10000];
int find(){
    int j, i = 0, ans = 0;;
    for(j = 0; j < n; j++){
        while( i < n && b[i] < a[j]){
            i++;
        }

        if(i >= n){
            break;
        }
        if(b[i] > a[j]){
            ans++;
            i++;
        }
    }
    return n-ans;
}
int find1(){
    int j, i = 0, ans = 0;;
    for(j = 0; j < n; j++){
        while( i < n && a[i] < b[j]){
            i++;
        }

        if(i >= n){
            break;
        }
        if(a[i] > b[j]){
            ans++;
            i++;
        }
    }
    return ans;
}
int solve(){
    int  i;
    cin>>n;
    for(i = 0; i < n; i++){
        cin>>a[i];
    }
    for(i = 0; i < n; i++){
        cin>>b[i];
    }
    sort(a , a + n);
    sort(b , b + n);
    int ans1 = find1();
    int ans2 = find();
    cout<<ans1<<" "<<ans2<<endl;
}
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int test, op = 1;
    cin>>test;
    while(test--){
        cout<<"Case #"<<op<<": ";
        solve();
        op = op + 1;
    }
    return 0;
}
