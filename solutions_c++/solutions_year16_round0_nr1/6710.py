//small worked.
#include <bits/stdc++.h>
using namespace std;
#define LL long long int
#define SI short int
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define pbc pair<bool,char>
#define pcc pair<char,char>
#define vi vector<int>
#define vii vector<vector<int> >
#define vb vector<bool>
#define FOR(i,st,end) for(int (i)=(st);i<(end);i++)
#define FORD(i,st,end) for(int (i)=(st);i>=(end);i--)
#define FASTIO ios::sync_with_stdio(false);
#define ABS(i) ((i)>0)?(i):(-(i))
#define sci(m) scanf(" %d",&m)
#define SORT(x) sort(x.begin(),x.end())
#define MOD 1000000007

void clearMask(LL m,int &mask){
    while(m){
        int d = m%10;
        m/=10;
        if((mask&(1<<d))>0)
            mask ^= (1<<d);
    }
}

int main(void){
    int T;
    sci(T);
    FOR(t,0,T){
        int mask = 1023;
        int n;
        LL m=0;
        sci(n);
        printf("Case #%d: ",t+1);
        if(n==0)
            printf("INSOMNIA\n");
        else{
            while(mask){
                m += n;
                clearMask(m,mask);
            }
            printf("%lld\n",m);
        }
    }
    return 0;
}
