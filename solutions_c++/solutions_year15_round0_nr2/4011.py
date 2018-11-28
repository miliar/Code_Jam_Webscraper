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
int tope;
int solve(int depth,vi donas){
    bool pasa = true;
    f(i,0,donas.size()){
        if(donas[i] != 0){
            pasa = false; break;
        }
    }
    if(pasa) return 0;
    if(depth == tope){
        return 1e9;
    }
    int maxi = 0;
    int pmax;
    f(i,0,donas.size()){
        if(donas[i] > maxi){
            pmax= i;
        }
        maxi = max(maxi,donas[i]);
    }
    int res = 1e9;
    f(i,0,maxi/2+1){
        vi tmp = donas;
        if(i == 0){

            f(j,0,donas.size()){
                tmp[j] = max(0,tmp[j]-1);
            }
            int val = solve(depth+1,tmp);
            res = min(res,1+val);
        }
        else{
            tmp.pb(i);
            tmp[pmax] -= i;
            int val = solve(depth+1,tmp);
            res = min(res,1+val);
        }
    }
    return res;
}

int main(){

    int T; cin >> T;
    f(test,0,T){
        int d; cin >> d;
        vi donas;
        f(i,0,d){
            int a; cin >> a;
            donas.pb(a);
        }
        sort(rall(donas));
        tope = donas[0];
        int t = solve(0,donas);
        cout<<"Case #"<<test+1<<": "<<t<<endl;

    }

    return 0;
}
