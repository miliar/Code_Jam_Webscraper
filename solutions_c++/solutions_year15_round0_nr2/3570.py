#include <iostream>
#include <queue>
#include <algorithm>
#include <math.h>
#include <set>
#include <map>


using namespace std;
#define     FOR(i,s,e)      for(int (i) = (s); (i) <  (e); ++(i))
#define     FORE(i,s,e)     for(int (i) = (s); (i) <= (e); ++(i))
#define     REP(i,n)        FOR(i,0,n)

typedef     pair<int, int>  pii;
typedef     vector<pii>     vii;

const int Nmax = 1010;

vii PairsOf[Nmax];


int N;
int A[Nmax];

void init(){
    REP(i,Nmax) PairsOf[i].clear();
    REP(i,Nmax) A[i] = 0;

    REP(i,Nmax){
        REP(j,Nmax){
            int x = ceil((double)i/(j+1));
            if (j<=x) PairsOf[i].push_back(make_pair(j,x));
            else break;
        }
    };
};

int solve(){
    int res = Nmax;

    vii F;
    F.clear();


    sort(A, A+N, std::greater<int>());

    REP(i, PairsOf[A[0]].size()){
        F.push_back(PairsOf[A[0]][i]);
    };

    map<int, int> BestOf;

    FOR(i,1,N){

        BestOf.clear();

        REP(k,PairsOf[A[i]].size()){
            pii P = PairsOf[A[i]][k];
            int x = P.first, y = P.second;

            REP(j, F.size()){
                pii Q = F[j];
                int u = Q.first, v = Q.second;
                //cout <<"x y ="<<x <<" "<<y<<" -- u v ="<<u<<" "<<v<<endl;
                int xu = x+u, yv = max(y,v);
                if (BestOf.count(yv)<1) BestOf[yv] = xu;
                else{
                    BestOf[yv] = min(BestOf[yv], xu);
                }
            }
        };// for k
        F.clear();
        for(map<int, int>::iterator it = BestOf.begin(); it != BestOf.end(); it++){
            int yv = (*it).first, xu = (*it).second;
            F.push_back(make_pair(xu, yv));
        };
    };

    res = Nmax;
    REP(j, F.size()){
        res = min(res, F[j].first +  F[j].second);
        //cout <<F[j].first <<" "<<  F[j].second<<F[j].first +  F[j].second<<endl;
    }


    return res;
};

int main()
{
    int T;
    cin >>T;
    int t = 0;
    init();
    while(T--){
        cin >>N;

        REP(i,N){
            cin >>A[i];
        };

        t++;
        cout << "Case #"<<t<<": "<<solve()<<endl;
    }

    return 0;
}
