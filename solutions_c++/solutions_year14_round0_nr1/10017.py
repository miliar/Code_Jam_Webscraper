#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <stack>
#include <cstring>
#include <iomanip>
#include <ctime>
using namespace std;
#define pb push_back
#define INF 1001001001
#define FOR(i,n) for(int (i)=0;(i)<(n);++(i))
#define FORE(i,n) for(int (i)=1;(i)<=(n);++(i))
#define mp make_pair
#define pii pair<int,int>
#define ll long long
#define vi vector<int>
#define SZ(x) ((int)((x).size()))
#define fi first
#define se second
#define inp(n) int (n); scanf("%d",&(n));
#define inp2(n,m) int (n),(m); scanf("%d %d",&(n),&(m));
#define inp3(n,m,k) int (n),(m),(k); scanf("%d %d %d",&(n),&(m),&(k));
#define SSD(x) (scanf("%d",&x))
#define SSL(x) (scanf("%lld",&x))
#define SSF(x) (scanf("%f",&x))
#define SSS(x) (scanf("%s",x))
inline void prt(int n) { printf("%d\n",n); }
template<typename T,typename TT> ostream& operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream& operator<<(ostream &s,vector<T> t){FOR(i,SZ(t))s<<t[i]<<" ";return s; }
#define IN(x,y) ((y).find((x))!=(y).end())
#define DBG(vari) cout<<#vari<<" = "<<(vari)<<endl;
#define ALL(t) t.begin(),t.end()
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define TESTS inp(testow)while(testow--)
#define REP(i,a,b) for(int (i)=(a);(i)<=(b);++i)
#define REPD(i,a,b) for(int (i)=(a); (i)>=(b);--i)
#define MAX(a,b) (a)=max((a),(b));
#define MIN(a,b) (a)=min((a),(b));
#define INRAN(a,b,c) ((a)>=(b) && (a)<(c))
#define MOD 1000000009
ll power(ll po, ll n)
{
    ll ans=1;
    while(n>0)
    {
        if(n&1)
        {
            ans=((ans%MOD)*(po%MOD))%MOD;
        }
        po=(po*po)%MOD;
        n/=2;
        
    }
    return ans;
}
int main ()
{
    freopen("../../../../Downloads/A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1-output.txt","w+",stdout);
    inp(test);
    int a[5][5], b[5];
    FORE(t, test) {
        cout << "Case #" << t << ": ";
        inp(no);
        FORE(i, 4) {
            FORE(j, 4) {
                cin>>a[i][j];
                if(i == no) {
                    b[j] = a[i][j];
                }
            }
        }
        cin>>no;
        int found = 0, foundno = -1;
        FORE(i, 4) {
            FORE(j, 4) {
                inp(no2);
                if(i == no) {
                    FORE(k,4) {
                        if(b[k] == no2) {
                            found++;
                            foundno = no2;
                        }
                    }
                }
            }
        }
        if(!found) {
            cout<<"Volunteer cheated!";
        }
        else if(found == 1) {
            cout<< foundno;
        }
        else {
            cout<<"Bad magician!";
        }
        cout<<endl;
    }
    
    return 0;
    
}
