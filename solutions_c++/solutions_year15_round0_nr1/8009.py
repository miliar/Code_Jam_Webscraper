#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include <limits.h>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<cassert>
using namespace std;
#define FOR(i,a,b) for(i= a ; i < b ; ++i)
#define rep(i,n) FOR(i,0,n)
#define INF INT_MAX
#define pb push_back
#define mp make_pair
//#define min(a,b) ((a)<(b)?(a):(b))
#define si3(m,n,o) scanf("%d%d%d",&m,&n,&o);
#define si(n) scanf("%d",&n)
#define si2(m,n) scanf("%d%d",&m,&n);
#define pin(n) printf("%d\n",n)
#define sl(n) scanf("%lld",&n)
#define scan(v,n) vector<int> v;rep(i,n){ int j;si(j);v.pb(j);}
#define mod (int)(1e9 + 7)
#define ll long long int
#define F first
#define S second
#include<fstream>

int main(){
    ifstream input("input.txt");
    ofstream output("output.txt");
    int t,n,ans,temp;
    string s;
    input>>t;
    int index=1;
    while(t--){
            temp=ans=0;
        input>>n>>s;
    for(int i=0;i<=n;i++){
        if(s[i]-'0'!=0){
            if(i>temp) {ans+=i-temp; temp=i;}
              temp+=s[i]-'0';
        }
    }
    output<<"Case #"<<index++<<": "<<ans<<endl;
    }
        return 0;
    }
