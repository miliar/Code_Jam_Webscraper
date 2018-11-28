#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<vector>
#include<list>
#include<set>
#include<deque>
#include<cmath>

#define FOR(i,j,k,l) for(((i)=(j));((i)<(k));((i)+=(l)))
#define REP(i,n) for((i)=0;(i)<(n);(i)++)
//#define min(a,b) ((a<b)?(a):(b))
//#define max(a,b) ((a>b)?(a):(b))
typedef long long int ll;
typedef long double ld;

using namespace std;

int main() {
    int nin, inum;
    int x, y, z, i, j, k, n;
    ll r,c;
    cin >> nin;char ans[50];int b[105][105],a[105][105];int rmax[105];int cmax[105];
    FOR(inum, 0, nin, 1) {
        //each test case
        cin>>r>>c;
        FOR(i,0,r,1){
            FOR(j,0,c,1){
                cin>>a[i][j];
                b[i][j]=100;
            }
        }
        FOR(i,0,r,1){
            rmax[i]=a[i][0];
            FOR(j,0,c,1){ rmax[i]=max(rmax[i],a[i][j]);}
        }
        FOR(i,0,c,1){
            cmax[i]=a[0][i];
            FOR(j,0,r,1){cmax[i]=max(cmax[i],a[j][i]);}
        }
        //for(i=0;i<r;i++){cerr<<rmax[i]<<" ";}cerr<<endl;
        //for(i=0;i<c;i++){cerr<<cmax[i]<<" ";}cerr<<endl;
        FOR(i,0,r,1){
            FOR(j,0,c,1){ if(b[i][j]>rmax[i])b[i][j]=rmax[i];}
        }
        FOR(i,0,c,1){
            FOR(j,0,r,1){if(b[j][i]>cmax[i])b[j][i]=cmax[i]; }
        }
        int ispossible=1;
        FOR(i,0,r,1){
            FOR(j,0,c,1){
                if(a[i][j]!=b[i][j]){ispossible=0;
                        //cerr<<"Mismatch at i, j, aij, bij"<<i<<" "<<j<<" "<<a[i][j]<<" "<<b[i][j]<<endl;
                }
            }
        }
        
        if(ispossible)sprintf(ans,"YES");
        else sprintf(ans,"NO");
        cout<<"Case #"<<inum+1<<": "<<ans<<endl;
    }

    return 0;
}

