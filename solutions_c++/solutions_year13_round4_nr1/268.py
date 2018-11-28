#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <stack>
using namespace std;

#define For(i,n) for(int i=0; i<(n); i++)
#define mp(a,b) make_pair((a),(b))
#define MOD 1000002013
typedef long long ll;
typedef pair<int,int> pii;

bool cond(pii a, pii b) {
    if(a.first<b.first) return true;
    if(a.first==b.first && a.second>b.second) return true;
    return false;
}

int main() {
    int t;
    scanf("%d ",&t);
    For(i1,t) {
        int n,m;
        scanf("%d %d ",&n,&m);
        vector<pii> U;
        vector<pair<pii,int> > A;
        For(i,m) {
            int a,b,p;
            scanf("%d %d %d ",&a,&b,&p);
            A.push_back(mp(mp(a,b),p));
            U.push_back(mp(a,i+1));
            U.push_back(mp(b,-i-1));
        }
        sort(U.begin(),U.end(),cond);
        ll vys=0;
        int miesto=1;
        //zaciatok, pocet
        vector<pii> D;
        For(i,U.size()) {
            miesto=U[i].first;
            if(U[i].second>0) {
                int co=U[i].second-1;
                D.push_back(mp(A[co].first.first,A[co].second));
            }
            else {
                int co=-U[i].second-1;
                int kolko=A[co].second;
                while(kolko>0) {
                    int kde=D.size()-1;
                    ll rozd=miesto-D[kde].first;
                    if(D[kde].second>kolko) {
                        ll pom=(ll)rozd*n-(ll)rozd*(rozd-1ll)/2ll;
                        pom%=MOD;
                        pom*=(ll)kolko;
                        pom%=MOD;
                        vys+=pom;
                        D[kde].second-=kolko;
                        kolko=0;
                    }
                    else {
                        ll pom=(ll)rozd*n-(ll)rozd*(rozd-1ll)/2ll;
                        pom%=MOD;
                        pom*=(ll)D[kde].second;
                        pom%=MOD;
                        vys+=pom;
                        kolko-=D[kde].second;
                        D.pop_back();
                    }
                    vys%=MOD;
                }
            }
        }
        ll malo=0;
        For(i,A.size()) {
            ll rozd=A[i].first.second-A[i].first.first;
            ll pom=(ll)rozd*n-rozd*(rozd-1ll)/2ll;
            pom%=MOD;
            pom*=(ll)A[i].second;
            pom%=MOD;
            malo+=pom;
            malo%=MOD;
        }
        vys=malo-vys+MOD;
        vys%=MOD;
        printf("Case #%d: %lld\n",i1+1,vys);
    }
return 0;
}
