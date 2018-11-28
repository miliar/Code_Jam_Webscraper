#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <cstring>
#include <climits>
#include <cstdio>
#include <stack>
#include <list>
using namespace std;
typedef pair<int,int> pi;
typedef set<int> si;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef long long ll;
#define sz size()
#define mp make_pair
#define pb push_back
#define ri(a, b) for(int i=((int)(a)); i < ((int)(b)); i++)                // i -> [a, b)
#define rie(a, b) for(int i=((int)(a)); i <= ((int)(b)); i++)            // i -> [a, b]
#define rj(a, b) for(int j=((int)(a)); j < ((int)(b)); j++)               // j -> [a, b)
#define rje(a, b) for(int j=((int)(a)); j <= ((int)(b)); j++)           // j -> [a, b]
#define rk(a, b) for(int k=((int)(a)); k < ((int)(b)); k++)           // k -> [a, b)
#define rke(a, b) for(int k=((int)(a)); k <= ((int)(b)); k++)       // k -> [a, b]
#define fi(b) for(int i=0; i < ((int)(b)); i++)                             // i -> [0, b)
#define fie(b) for(int i=0; i <= ((int)(b)); i++)                         // i -> [0, b]
#define fj(b) for(int j=0; j < ((int)(b)); j++)                            // j -> [0, b)
#define fje(b) for(int j=0; j <= ((int)(b)); j++)                        // j -> [0, b]
#define fk(b) for(int k=0; k < ((int)(b)); k++)                        // k -> [0, b)
#define fke(b) for(int k=0; k < ((int)(b)); k++)                      // k -> [0, b]
#define fle(b) for(int l=0; l <= ((int)(b)); l++)                        // l -> [0, b]

bool isOk(map<char, int> M){
    
    int n = 0;
    // cout<<"===isOk==="<<endl;
    for(char c = 'A'; c <= 'Z'; c++){
        // cout<<c<<endl;
        n += M[c];
        // if(M[c]) cout<<c<<" => "<<M[c]<<endl;
    }
    // cout<<"=========="<<endl;
    for(char c = 'A'; c <= 'Z'; c++){
        if(M[c] > n/2) return false;
    }
    return true;
}

list<string> compute(map<char, int> M){
    for(char c = 'A'; c <= 'Z'; c++){
        if(M[c] < 2) continue;
        M[c] -= 2;
        if(isOk(M)){
            list<string> t = compute(M);
            string r = {c, c};
            t.push_front(r);
            return t;
        }
        M[c] += 2;
    }
    for(char c = 'A'; c <= 'Z'; c++)
    for(char d = c+1; d <= 'Z'; d++)
    {
        if(M[c] == 0 || M[d] == 0) continue;
        M[c]--;
        M[d]--;
        if(isOk(M)){
            list<string> t = compute(M);
            string r = {c, d};
            t.push_front(r);
            return t;
        }
        M[c]++;
        M[d]++;
    }
    for(char c = 'A'; c <= 'Z'; c++){
        if(M[c] == 0) continue;
        M[c]--;
        if(isOk(M)){
            list<string> t = compute(M);
            string r = {c};
            t.push_front(r);
            return t;
        }
        M[c]++;
    }
    return list<string>();
}

int main(){

    int n, t;

    map<char, int> M;
    list<string> ans;
    // isOk(M);
    cin>>t;

    rke(1, t){
        M.clear();
        for(char c = 'A'; c <= 'Z'; c++){
            M[c] = 0;
        }
        cin>>n;
        fi(n){
            cin>>M[(char)('A' + i)];
        }
        ans = compute(M);
        cout<<"Case #"<<k<<":";
        for(auto c : ans) cout<<" "<<c;
        cout<<endl;
    }
}
// END CUT HERE 
