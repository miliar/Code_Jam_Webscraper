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
        int x,c,r; cin >> x >>r >> c;
        if(r > c) swap(r,c);
        string win = "RICHARD";
        string lose = "GABRIEL";
        string res = lose;
        if(r == 1){
            if(c == 1){
                if( x >= 2) res = win;
            }
            if(c == 2){
                if(x >= 3) res =win;
            }
            if(c==3){
                if(x >= 2) res = win;
            }
            if(c == 4){
                if(x >=3) res = win;
            }
        }
        if(r == 2){
            if(c ==2){
                if(x >= 3) res =win;
            }
            if(c == 3){
                if(x >= 4) res = win;
            }
            if(c == 4){
                if(x >= 3) res = win;
            }

        }
        if(r == 3){
            if(c == 3){
                if(x >= 2 && x != 3) res = win;
            }
            if(c==4){
                ;
            }
        }
        if(r ==4){
            if(c == 4){
                if(x == 3) res = win;
            }
        }


        cout<<"Case #"<<test+1<<": "<<res<<endl;

    }

    return 0;
}
