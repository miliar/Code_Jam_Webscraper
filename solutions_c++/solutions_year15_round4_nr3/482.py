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

map<string,int> M;
int pocet=0;
vector<int> P;

void veta(int ktora) {
    string s;
    getline(cin,s);
    s+=" ";
    string p="";
    For(i,s.length()) {
        if(s[i]!=' ') p+=s[i];
        else {
            if(M.find(p)==M.end()) {M[p]=pocet++; P.push_back(0);}
            P[M[p]]|=(1<<ktora);
            p="";
        }
    }
}

void solve() {
    M.clear();
    P.clear();
    pocet=0;
    int n;
    scanf("%d ",&n);
    For(i,n) veta(i);
    int vsetky=P.size();
    int res=vsetky;
    For(i,1<<(n-2)) {
        int k=4*i+2;
        int ki=0;
        For(j,n) if(!(k&(1<<j))) ki+=(1<<j);
        int rataj=0;
        For(j,P.size()) {
            if(vsetky-rataj-(P.size()-j)>res) break;
            if((k|P[j])==k || (ki|P[j])==ki) rataj++;
        }
        res=min(res,vsetky-rataj);
    }
    printf("%d\n",res);
}

int main() {
    int t;
    scanf("%d",&t);
    For(i,t) {
        printf("Case #%d: ",i+1);
        solve();
    }
}
