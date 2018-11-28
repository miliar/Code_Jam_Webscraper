#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int x;
int t;
int a[20][20],b[20][20],we[2000000],l,n;
string s,w;
int main() {
    freopen("c-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(0);
    cin >> t;
    int tk=0;
    a[1][1]=1;
    a[1][2]=2;
    a[1][3]=3;
    a[1][4]=4;
    a[2][1]=2;
    a[2][2]=1;
    a[2][3]=4;
    a[2][4]=3;
    a[3][1]=2;
    a[3][2]=4;
    a[3][3]=1;
    a[3][4]=2;
    a[4][1]=4;
    a[4][2]=3;
    a[4][3]=2;
    a[4][4]=1;
    b[2][2]=1;
    b[2][4]=1;
    b[3][2]=1;
    b[3][3]=1;
    b[4][4]=1;
    b[4][3]=1;
    for (;t>=1;t--) {
        cin >> l >> x;
        cin  >> w;
        string s;
        for (int i=1;i<=x;i++) s+=w;
        int mul=1;
        int st=0;
        int zn=0;
        l=l*x;
        for (int i=1;i<=l;i++) we[i]=s[i-1]-'i'+2;
        for (int i=1;i<=l;i++) {
            zn^=b[mul][we[i]];
            mul=a[mul][we[i]];
            if (mul==2 && zn==0 && st==0) {
                st++;
                mul=1;
                zn=0;
            }
            else
            if (mul==3 && zn==0 && st==1) {
                st++;
                mul=1;
                zn=0;
            }
            else
            if (mul==4 && zn==0 && st==2 && i==l) {
                st++;
                mul=1;
                zn=0;
            }
        }
        tk++;
        if (st==3) cout << "Case #" << tk << ": YES\n";
        else cout << "Case #" << tk << ": NO\n";
    }
    return 0;
}
