// includes {
#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <list>
#include <sstream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cctype>
// }
using namespace std;
// defines {
#define FOR(i,n) for((i)=0; (i)<(n); (i)++)
#define REP(i,n) for((i)=1; (i)<=(n); (i)++)
#define SET(a,v) memset(a, v, sizeof(a))
#define SZ(a) (int)(a).size()
#define LEN(a) (int)(a).length()
#define PB push_back
#define all(a) (a).begin(), (a).end()
#define sqr(a) (a)*(a)
#define inrange(lb,i,ub) ((lb) <= (i) && (i) <= (ub))
#define foreach(it, a) for(typeof((a).begin()) it=(a).begin(); it != (a).end(); it++)
// }
typedef pair<double,double> dd;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<ii> vii;
typedef vector<dd> vdd;
typedef unsigned int ui;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

void getRow(int R, int row[]){

    for ( int i = 0 ; i < 4 ; i++){
            for(int j = 0 ; j <4 ; j++ ){
                int aux; cin >> aux;
                if ( i == R )
                    row[j] = aux;
            }
        }

}
int card_number;
int countEquals (int* row1, int* row2){
     int cont = 0;
     for ( int i = 0 ; i < 4 ; i++){
            for(int j = 0 ; j <4 ; j++ ){
               if ( row1[i] == row2[j] ){
                    cont++;
                    card_number = row1[i];
               }
            }
        }
    return cont;
}
int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    int cont_case = 1;
	int T = 0; cin >> T;
	while(T--){
        int R1,R2;
        int row1[4], row2[4];
        cin >> R1;
        getRow(R1-1, row1);
        cin >> R2;
        getRow(R2-1,row2);

        int semejantes = countEquals(row1,row2);

        cout << "Case #" << cont_case++ << ": ";

        if ( semejantes == 0) cout << "Volunteer cheated!";
        else if ( semejantes == 1 ) cout << card_number;
        else cout << "Bad Magician!";

        cout << endl;
	}
	return 0;
	}
