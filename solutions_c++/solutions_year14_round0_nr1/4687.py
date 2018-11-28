//Bismillahir Rahmanir Rahim
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <sstream>

using namespace std;


#define mp make_pair
#define rep(i,n) for(int i=0,_n=n;i<_n;i++)
#define reps(i,s,n) for(int i=s,_n=n;i<_n;i++)
#define pi 2.0*acos(0.0)
#define MAX 2147483647
#define MIN -2147483647
#define torad(a) (a*pi)/180.0;
#define eps 0.000000001
#define pb push_back
#define pf push_front
#define pob pop_back
#define pof pop_front

typedef long long ll;
typedef vector<int>VI;
typedef map<string,int> MSI;
typedef set<int>SI;
typedef pair<int,int>PAR;
typedef vector<PAR>VP;
int gcd(int a, int b) {
    if(!b) {
        return a;
    } else {
        return gcd(b, a%b);
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int N, M, T;
    int mark[17];

    cin >> T;
    for(int cas = 1; cas <= T; cas ++ ) {
        cin >> N;
        N --;
        memset(mark, 0, sizeof(mark));
        for(int i = 0; i < 16; i ++) {
            int a;
            cin >> a;
            if( i / 4 == N ) {
                mark[a] ++;
            }
        }
        cin >> M;
        M --;
        for(int i = 0; i < 16; i++) {
            int a;
            cin >> a;
            if(i / 4 == M ) {
                mark[a] ++;
            }
        }
        int ret = -1;
        for(int i = 1; i <= 16; i++) {
            if( mark[i] == 2 ) {

                if(ret != -1 ) {
                    ret = -2;
                } else {
                    ret = i;
                }
            }
        }

        printf("Case #%d: ", cas);

        if(ret == -1 ) {
            cout << "Volunteer cheated!" << endl;
        } else if ( ret == -2 ) {
            cout << "Bad magician!" << endl;
        } else {
            cout << ret << endl;
        }
    }
    return 0;
}
