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
#define ForEach(it, i) for(typeof i.begin() it = i.begin(); it!=i.end(); ++it)
#define INF 1023456789
#define eps 1e-9

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int m,n;
char buf[107];
vector<string> S;

class Trie{
    vector<vi> syni;
public:
    void clear(){
        syni.clear();
        syni.push_back(vi(26,0));
    }
    int size(){
        return syni.size();
    }
    int novy(){
        syni.push_back(vi(26,0));
        return int(syni.size())-1;
    }
    void push(string s){
        int node = 0;
        For(i, s.size()){
            int c = s[i]-'A';
            if(syni[node][c]==0){
                syni[node][c] = novy();
            }
            node = syni[node][c];
        }
    }
};

Trie trie;

int pocet(){
    trie.clear();
    For(i, m) trie.push(S[i]);
    return trie.size()-1;
}

int extra(){
    scanf("%d%d",&m,&n);
    S.clear();
    For(i, m){
        scanf("%s", buf+1);
        buf[0] = 'A';
        S.push_back(string(buf));
    }
    int poc = 1;
    int naj = 0, kolko = 0;
    For(i, m) poc*=n;
    For(rozd, poc){
        int roz = rozd;
        For(i, m) {
            S[i][0] = 'A'+(roz%n);
            roz/=n;
        }
        int teraz = pocet();
        if (naj<teraz) {
            naj = teraz;
            kolko = 0;
        }
        if (naj == teraz){
            kolko++;
        }
    }
    printf("%d %d\n", naj, kolko);
}

int main(){
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
