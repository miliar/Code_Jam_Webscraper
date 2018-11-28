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
bool ExistsHigher(vector<pair<float,bool> > Ken, float n){
    for( vector<pair<float,bool> >::iterator itN = Ken.begin() ; itN != Ken.end(); itN++){
       if ( (*itN).first > n && (*itN).second == false){
            return (*itN).second = true;

       }
    }
    return false;
}
int getDW(vector<pair<float,bool> > P1, vector<pair<float,bool> > P2){
    int winsWar = 0;
    vector<pair<float,bool> >::iterator itK = P2.begin();
    for( vector<pair<float,bool> >::iterator itN = P1.begin() ; itN != P1.end(); itN++){
        if ( (*itN).first < (*itK).first )  itK++;
        else winsWar++;
    }
    return winsWar;
}
int getW(vector<pair<float,bool> > P1, vector<pair<float,bool> > P2){
    int winsWar = 0;
    vector<pair<float,bool> >::iterator itK = P2.begin();
    for( vector<pair<float,bool> >::iterator itN = P1.begin() ; itN != P1.end(); itN++){
        if ( (*itN).first > (*itK).first ) winsWar++;
        else itK++;
    }
    return winsWar;
}


int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.in", "r", stdin);
    freopen("output.txt","w",stdout);
    #endif
    int cont = 1;
	int T = 0; cin>> T;
    while (T--){
        int N = 0; cin >> N;
        int winsWar,winsDW;
        vector<pair<float,bool> > Naomi,KenW,KenDW;
        for( int i = 0 ; i < N ; i++){
            pair <float,bool> aux;
            float aux2; cin >> aux2;
            aux.first = aux2; aux.second = false;
            Naomi.push_back(aux);
        }
        for( int i = 0 ; i < N ; i++){
            pair <float,bool> aux;
            float aux2; cin >> aux2;
            aux.first = aux2; aux.second = false;
            KenW.push_back(aux);
            KenDW.push_back(aux);
        }
        sort(Naomi.begin(),Naomi.end());
        sort(KenW.begin(),KenW.end());
        reverse(Naomi.begin(),Naomi.end());
        reverse(KenW.begin(),KenW.end());
        winsDW = N-getDW(KenW,Naomi);
        winsWar=getW(Naomi,KenW);

        cout << "Case #" << cont++ << ": " << winsDW << " " << winsWar << endl;

    }
	return 0;
	}
