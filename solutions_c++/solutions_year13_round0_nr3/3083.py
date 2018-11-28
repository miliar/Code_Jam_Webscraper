#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;
#define MAXN 10001000
int count[MAXN];

int low;
inline bool is_palindorme(long long p, long long up)
{
    up = up/10; low = 10;
    while(p){
        if((p/up) != (p%10))return false;
        p = (p%up)/10;
        up = up/100;
    }
    return true;
}

long long pp, ll;
inline int judge(int p, int l)
{
    if(!is_palindorme((long long)p, (long long)l))return 0;
    pp = (long long)p*(long long)p;
    ll = (long long)l*(long long)l /100;
    while(ll <= pp)ll*=10;
    if(!is_palindorme(pp, ll))return 0;
    return 1;
}

void initialization()
{
    memset(count, 0, sizeof(count));
    int l=10;
    for(int i = 1; i< MAXN; i++){
        if(i >= l) l*=10;
        count[i] = count[i-1] + judge(i, l);
        //printf("%d\n", count[i]);
    };
}

int main()
{
    initialization();
    int T;
    long long A, B;
    int rA, rB;
    cin>>T;
    for(int cas = 1; cas <= T; cas ++){
        cin>>A>>B;
        rA = sqrt(A); rB = sqrt(B);
        if(rA*rA == A) rA--;
        cout<<"Case #"<<cas<<": "<<count[rB]-count[rA]<<endl;
    }
    return 0;
}
