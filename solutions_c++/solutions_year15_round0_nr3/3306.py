//  C
//

#include <iostream>
#include <cstdio>
#include <cstring>
#define MM 10009
int table[5][5]=
{   {0, 0, 0, 0, 0},
    {0, 1, 2, 3, 4},
    {0, 2, -1, 4, -3},
    {0, 3, -4, -1, 2},
    {0, 4, 3, -2 ,-1}};
using namespace std;
char s[MM];

int solve(int k){
    int  l, x ;
    bool foundi=false, foundk=false;
    char curc;
    int v, curi;
    scanf("%d %d", &l, &x);
    scanf("%s", s);

    v=1;
    for (int i=0; i< x; i++) {

    for(int ii=0; ii < strlen(s); ii++){
        curc=s[ii]; curi=curc-'g';
        v=(v*table[abs(v)][curi]<0)? - abs(table[abs(v)][curi]): abs(table[abs(v)][curi]);

        if (v==2) foundi=true;
        if (v==4 && foundi) foundk= true;
        }
    }

    if (foundi && foundk && v==-1) cout << "Case #" << k  <<": " << "YES" << endl;
    else cout << "Case #" << k  <<": " << "NO" << endl;
    return 0;
}

int main(int argc, const char * argv[]) {
    int t;
    scanf("%d", &t);
    for(int x =1; x <=t; x++){
        solve(x);
    }
    return 0;
}