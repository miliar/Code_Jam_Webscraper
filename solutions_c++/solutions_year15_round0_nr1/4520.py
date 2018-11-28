#include <iostream>
#include <sstream>
#include <bitset>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdlib>

#define mp make_pair
#define pb push_back
#define debug( x ) cout << #x << " = " << x << endl
#define all(x) (x).begin() , (x).end()
#define rall(x) (x).rbegin() , (x).rend()
#define f(i,a,b) for(int i = a ; i < b ; i++)
#define EPS 1E-9
#define INF 1000000000

using namespace std;

typedef pair<int,int> ii ;
typedef long long ll ;
typedef vector<int> vi;

int main(){

    int T; cin >> T;
    f(test,0,T){
        int smax; cin >> smax;
        string s; cin >> s;

        int parados = 0;
        int extra = 0;

        f(necesita,0,smax+1){
            int cant = s[necesita]-'0';
            if(cant == 0) continue;
            if(parados >= necesita){
                parados+=cant;
            }else{
                extra += (necesita-parados);
                parados+=cant+necesita-parados;
            }
            //debug(extra);
            //debug(parados);
        }
        cout<<"Case #"<<test+1<<": "<<extra<<endl;

    }

    return 0;
}
