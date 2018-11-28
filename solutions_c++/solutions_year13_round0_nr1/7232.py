/* Bismillahir rahmanir rahim */
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <numeric>
#include <utility>
#include <iomanip>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <numeric>
#include <sstream>
#include <fstream>
#include <iterator>
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

#define INT_MAX     2147483647
#define INT_MIN     -2147483648
#define pi          acos(-1.0)
#define siz         10000000
#define eps         1e-9;

#define rep(i, n)   for(int i = 0; i < (n); i++)
#define fill(a, v)  memset(a, v, sizeof (a))
#define pb          push_back
#define pf          push_front
#define mp          make_pair
#define all(a)      (a).begin(),(a).end()

typedef long long int LL;
typedef long double LD;
typedef vector<int> VI;

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A.txt", "w", stdout);

    int t, c = 1, i, j, k;
    char in[6][6], ch;
    bool O, X, D, C;

    cin>>t;
    getchar();

    while(t--){
        for(i=0; i < 4; i++)
            gets(in[i]);

        O = X = D = C = false;

        rep(i, 4){
            ch = in[i][0];
            if(ch == 'T')
                ch = in[i][1];
            for(j = 0; j < 4; j++){
                if(in[i][j] != ch && in[i][j] != 'T')
                    break;
            }
            if(j == 4){
                if(ch == 'O') O = true;
                else if(ch == 'X') X = true;
            }
        }

        rep(i, 4){
            ch = in[0][i];
            if(ch == 'T')
                ch = in[1][i];
            for(j = 0; j < 4; j++)
                if(in[j][i] != 'T' && in[j][i] != ch)
                    break;
            if(j == 4){
                if(ch == 'O') O = true;
                else if(ch == 'X') X = true;
            }
        }

        if(!O && !X){
            ch = in[0][0];
            if(ch == 'T')
                ch = in[1][1];
            for(i = 0; i < 4; i++)
                if(in[i][i] != ch && in[i][i] != 'T')
                    break;
            if(i == 4){
                if(ch == 'O') O = true;
                else if(ch == 'X') X = true;
            }
        }

        if(!O && !X){
            ch = in[0][3];
            if(ch == 'T')
                ch = in[1][2];
            for(i = 0, j = 3; i < 4; i++, j--)
                if(in[i][j] != ch && in[i][j] != 'T')
                    break;
            if(i == 4 ){
                if(ch == 'O') O = true;
                else if(ch == 'X') X = true;
            }
        }

        if(!O && !X)
            rep(i, 4)
                if(!C)
                    rep(j, 4)
                        if(in[i][j] == '.'){
                            C = true;
                            break;
                        }

        if(O)
            cout<<"Case #"<<c++<<": O won"<<endl;
        else if(X)
            cout<<"Case #"<<c++<<": X won"<<endl;
        else if(C)
            cout<<"Case #"<<c++<<": Game has not completed"<<endl;
        else
            cout<<"Case #"<<c++<<": Draw"<<endl;

        getchar();
    }

    return 0;
}
