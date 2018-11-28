#include<iostream>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<vector>
using namespace std;
#define FOR(i,l,n) for(int i=l;i<n;i++)
#define INT(c) int c;scanf("%d",&c);
#define LL(c) long long c;scanf("%ll",&c);
#define ULL(c) unsigned long long c;scanf("%llu",&c);
#define MOD 1000000007
#define Ull unsigned long long
#define Ll lnong long
#define chk(x) x%=MOD;
int main()
{
    INT(t)
    FOR(i,0,t)
    {
        INT(n1)
        int a[4][4];
        FOR(j,0,4)
            FOR(k,0,4)
                scanf("%d",&a[j][k]);
        INT(n2)
        int b[4][4];
        FOR(j,0,4)
            FOR(k,0,4)
                scanf("%d",&b[j][k]);
        int found=0,item_found;
        FOR(j,0,4)
            FOR(k,0,4)
                if(a[n1-1][j]==b[n2-1][k])
                {
                    found++;
                    item_found=b[n2-1][k];
                }
        if(found==0)
            cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
        else if(found==1)
            cout<<"Case #"<<i+1<<": "<<item_found<<endl;
        else if(found>1)
            cout<<"Case #"<<i+1<<": Bad magician!"<<endl;

    }
    return 0;
}

