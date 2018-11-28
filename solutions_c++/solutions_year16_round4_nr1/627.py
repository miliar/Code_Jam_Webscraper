//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>
#include<iostream>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<cstring>

using namespace std;

#define For(i, n) for(int i = 0; i<(n); ++i)
#define INF 1023456789
#define eps 1e-9

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

string app[256];
int n, p,r,s;

string transform(const string& from) {
    string res = "";
    for(auto c : from) res += app[c];
    return res;
}

string gen(string str, int n) {
    For(i, n) {
        str = transform(str);
    }
    if (std::count(str.begin(), str.end(), 'P') != p) return "";
    if (std::count(str.begin(), str.end(), 'R') != r) return "";
    if (std::count(str.begin(), str.end(), 'S') != s) return "";

    int N = (1<<n);
    int skok = 1;
    while(skok < N) {
        for(int i = 0; i<N; i+=skok*2) {
            For(j, skok) {
                if (str[i+j] < str[i+skok+j]) break;
                if (str[i+j] > str[i+skok+j]) {
                    For(k, skok) swap(str[i+k], str[i+skok+k]);
                    break;
                }
            }
        }
        skok *= 2;
    }
    
    return str;
}

int extra() { 
    app['P'] = "PR";
    app['R'] = "SR";
    app['S'] = "SP";
    scanf("%d%d%d%d",&n,&r,&p,&s);
    string best = "IMPOSSIBLE";
    string X;

    X = gen("P",n); 
    if (X.size()) best = X;
    
    X = gen("R",n); 
    if (X.size()) best = X;
    
    X = gen("S",n); 
    if (X.size()) best = X;
    
    printf("%s\n", best.c_str());
}

int main() {
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
