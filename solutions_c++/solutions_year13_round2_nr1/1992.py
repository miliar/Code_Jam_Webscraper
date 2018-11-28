#include<iostream>
#include<stdlib.h>
#include<cmath>
#include<string>
#include<algorithm>
#include<vector>
#include<stdio.h>

using namespace std;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef long long ll;
#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(), (c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i!=(c).end();i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())

void solve(int i);
int work(ll a, ll count, int len, vll & motes, int j);
int cao(ll a, ll b);

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    cin >> t;
    int i = 0;
    for(i=0;i<t;i++){
        solve(i);
    }
}
void solve(int i){
    ll a, n;
    cin >> a >> n;
    vll motes;
    int j = 0;
    for(j=0;j<n;j++){
        int temp;
        cin >> temp;
        motes.pb(temp);
    }
    sort(motes.begin(),motes.end());
    int count;
    if(a==1){
        count = n;
    }
    else{
    count = work(a,0,n,motes,0);
    }
    cout << "Case #"<<i+1<<": "<<count<<endl;
}

int work(ll a, ll count, int len, vll & motes, int j){
    if(j==len){
        return count;
        }
    else if(a > motes[j]){
        return work(a+motes[j],count,len,motes,j+1);
    }
    else if(2*a-1>motes[j]){
        return work(2*a+motes[j]-1,count+1,len,motes,j+1);
    }
    else{
        int co = cao(a,motes[j]);
        int count1 = work(pow(2,co)*a-pow(2,co)+1+motes[j],count+co,len,motes,j+1);
        int count2 = work(a,count+1,len,motes,j+1);
        return min(count1,count2);
    }
}
int cao(ll a, ll b){
    ll co = 0;
    while(a<=b){
        a = 2*a -1;
        co++;
    }
    return co;
}
