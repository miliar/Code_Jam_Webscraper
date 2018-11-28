#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<string>
#include<queue>
#include<stack>
#include<cctype>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef map<int,int> mii;
typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef vector<char> vc;
typedef vector<bool> vb;
typedef vector<string> vs;

#define rep(i,n) for(int i=0;i<n;i++)
#define forup(i,a,b) for(int i=a;i<=b;i++)
#define fordn(i,a,b) for(int i=a;i>=b;i--)
#define all(x) x.begin(),x.end()
#define permute(x) next_permutation(all(x))
#define pb push_back

#define debug if(printf("JJ "))

int s1(vector<double> v1, vector<double> v2,int n){
    sort(all(v1),greater<int>());
    sort(all(v2));
    int ans=0;
    rep(i,n){
        vector<double>::iterator it = upper_bound(all(v2),v1[i]);
        if(it == v2.end()) it = v2.begin();
        if(v1[i] >= *it) ans++;
        v2.erase(it);
    }
    return ans;
}
int s2(vector<double> v1, vector<double> v2,int n){
    sort(all(v1));
    sort(all(v2));
    int i=0,j=0;
    while(i<n && j<n){
        if(v1[i] > v2[j])
            j++;
        i++;
    }
    return j;
}
int main(){
    int t,n;    
    scanf("%d",&t);
    forup(z,1,t){
        scanf("%d",&n);
        vector<double> v1(n),v2(n);
        rep(i,n)scanf("%lf",&v1[i]);
        rep(i,n)scanf("%lf",&v2[i]);
        printf("Case #%d: %d %d\n",z,s2(v1,v2,n),s1(v1,v2,n));
    }
}
