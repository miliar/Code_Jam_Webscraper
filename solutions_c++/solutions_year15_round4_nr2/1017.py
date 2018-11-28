//Przemysław Jakub Kozłowski
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <iomanip>
#define FI first
#define SE second
#define MP make_pair
using namespace std;
typedef long long LL;
typedef long double LD;
const int N = 103;
const LL W = 1000006, PODZ = 10000000;
const LD EPS = 0.000000000000001L;

bool cmp(const pair<LD,LD> &A, const pair<LD,LD> &B)
{
    return A.SE < B.SE;
}

int n;
LD OV, OX;
pair<LD, LD> A[N];

LD OA, OB;
pair<LD, LD> B[N];

LD obl(LD sr)
{
    LD obj = 0, temp = 0;
    for(int i = 1;i <= n;i++)
    {
        LD add = max(0.0L,min(sr, (OA-obj)/B[i].FI));
        obj += add*B[i].FI;
        temp += add*B[i].SE;
    }
    
    if(abs(obj-OA) > EPS) return 0;
    return temp;
}

bool check(LL sr) // sr 1/PODZ sek
{
    LD mini = obl((LD)sr/PODZ);
    reverse(B+1,B+n+1);
    LD maxi = obl((LD)sr/PODZ);
    reverse(B+1,B+n+1);
    
    bool ret = (mini-EPS <= OB && OB <= maxi+EPS);
    
    //cerr << "Sr/PODZ: " << setprecision(7) << (LD)sr/PODZ << " Mini: " << mini << " Maxi: " << maxi << " OB: " << OB << " Ret: " << ret << endl;
    return ret;
}

LL bin(LL p, LL k)
{
    LL ret = k;
    LL sr;
    
    while(p < k)
    {
        sr = (p+k)/2;
        if(check(sr))
        {
            k = sr;
            ret = sr;
        }
        else
            p = sr+1;
    }
    return ret;
}

int main()
{
    int t;
    scanf("%d", &t);
    for(int ti = 1;ti <= t;ti++)
    {
        printf("Case #%d: ", ti);
        scanf("%d%Lf%Lf", &n, &OV, &OX);
        
        for(int i = 1;i <= n;i++)
        {
            LD r, c;
            scanf("%Lf%Lf", &r, &c);
            A[i] = MP(r,c);
        }
        
        sort(A+1,A+n+1,cmp);
        
        OA = OV;
        OB = OV*OX;
        for(int i = 1;i <= n;i++)
            B[i] = MP(A[i].FI, A[i].FI*A[i].SE);
        
        LL wyn = bin(1, W*PODZ);
        if(wyn == W*PODZ) printf("IMPOSSIBLE\n");
        else printf("%.7Lf\n", (LD)wyn/PODZ);
    }
    return 0;
}
