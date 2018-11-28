#include<bits/stdc++.h>
using namespace std;

typedef long long int ll;
typedef pair<ll,ll> pii;
#define REP(i,n) for(ll i=0;i<n;i++)

#ifdef DEBUG
#define dbg(x) x
#define dbgp(x) cerr << x << endl;
#else
#define dbg(x) //x
#define dbgp(x) //cerr << x << endl;
#endif

string eng_rep[] = {
    "ZERO",
    "ONE",
    "TWO",
    "THREE",
    "FOUR",
    "FIVE",
    "SIX",
    "SEVEN",
    "EIGHT",
    "NINE"
};

map<char,int> rep_state[10];
map<map<char,int>, int> rep_state_map;

vector<int> answer;

void dbgRep(map<char,int> rep){
    for(pair<char, int> p: rep){
        cerr << p.first << ":" << p.second << " ";
    }
    cerr << endl;
}

set<pair<map<char,int>, int> > prune;

bool dp(map<char,int> rep, int prev){
    //dbgRep(rep);
    
    auto state = make_pair(rep, prev);

    int total = 0;
    for(pair<char, int> p: rep){
        total += p.second;
    }
    if(total == 0){
        return true;
    }

    for(int i=9;i>=0;i--){
        if(i>prev) continue;

        map<char,int> numrep = rep_state[i];
        bool ok = true;
        for(pair<char,int> p: numrep){
            if(rep[p.first] < p.second){
                ok = false;
                break;
            }
        }
        if(!ok) continue;

        map<char,int> nrep = rep;
        for(pair<char,int> p: numrep){
            nrep[p.first] -= p.second;
        }
        if(dp(nrep, i)){
            answer.push_back(i);
            return true;
        }
    }

    prune.insert(state);

    return false;
}

void solve(){
    string s;
    cin >> s;

    map<char,int> rep;
    for(char c: s){
        rep[c]++;
    }

    answer.clear();
    if(dp(rep, 10)){
        for(int d: answer){
            cout << d;
        }
    }else{
        cerr << "Answer not found " << endl;
    }

}

int main(){

    // Precalculate rep state;
    REP(i,10){
        for(char c: eng_rep[i]){
            rep_state[i][c]++;
        }
        rep_state_map[rep_state[i]] = i;
    }

    int T;
    cin >> T;

    REP(i,T){
        printf("Case #%d: ",i+1);
        solve();
        printf("\n");
    }
}
