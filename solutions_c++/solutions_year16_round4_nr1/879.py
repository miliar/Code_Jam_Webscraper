#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <stack>
using namespace std;

#define For(i,n) for(int i=0; i<(n); i++)
#define mp(a,b) make_pair((a),(b))
typedef long long ll;
typedef pair<int,int> pii;

int n,p,r,s;
string N[3][20];

void najmensie() {
    N[0][1]="PR";
    N[1][1]="RS";
    N[2][1]="PS";
    for(int i=2; i<15; i++) {
        //P
        if(N[0][i-1]<N[1][i-1]) N[0][i]=N[0][i-1]+N[1][i-1];
        else N[0][i]=N[1][i-1]+N[0][i-1];
        //R
        if(N[1][i-1]<N[2][i-1]) N[1][i]=N[1][i-1]+N[2][i-1];
        else N[1][i]=N[2][i-1]+N[1][i-1];
        //S
        if(N[0][i-1]<N[2][i-1]) N[2][i]=N[0][i-1]+N[2][i-1];
        else N[2][i]=N[2][i-1]+N[0][i-1];
    }
}

string ries(string a) {
    string b="";
    For(i,n) {
        For(j,a.length()) {
            if(a[j]=='P') b+="PR";
            else if(a[j]=='S' && i>=n-2) b+="PS";
            else if(a[j]=='S') b+="SP";
            else if(a[j]=='R' && i==n-1) b+="RS";
            else b+="SR";
        }
        a=b; b="";
    }
    return a;
}

bool spocitaj(string a) {
    int p1=0,s1=0,r1=0;
    For(i,a.length()) {
        if(a[i]=='P') p1++;
        if(a[i]=='R') r1++;
        if(a[i]=='S') s1++;
    }
    if(p1==p && r1==r && s1==s) return true;
    return false;
}

void solve(int por) {
    scanf("%d %d %d %d",&n,&r,&p,&s);
    vector<string> res;
    string pom=ries("P");
    if(spocitaj(pom)) res.push_back(N[0][n]);
    pom=ries("R");
    if(spocitaj(pom)) res.push_back(N[1][n]);
    pom=ries("S");
    if(spocitaj(pom)) res.push_back(N[2][n]);
    //For(i,res.size()) printf("%s\n",res[i].c_str());
    sort(res.begin(),res.end());
    if(res.size()==0) res.push_back("IMPOSSIBLE");
    printf("Case #%d: %s\n",por,res[0].c_str());
}

int main() {
    najmensie();
    int t;
    scanf("%d",&t);
    For(i,t) solve(i+1);
}
