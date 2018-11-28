#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string.h>
using namespace std;

#define LARGE 1

#if LARGE==1
char inname[]  = "A-large.in";
char outname[] = "A-large.out";
#else
char inname[]  = "A-small.in";
char outname[] = "A-small.out";
#endif

typedef long long LL;
typedef vector<int>  TVI;
typedef vector<int>::iterator TVII;
typedef vector<double>  TVD;
typedef vector<double>::iterator TVDI;

#define SIZE 1001
int ai[SIZE];
double ad[SIZE];

#define RW {cout << "RICHARD"; return;}
#define GW {cout << "GABRIEL"; return;}


void solve_case(void)
{
    int a[255];
    char S[2010];
    int y[10];
    cin >> S;
    int l=strlen(S);
    memset(a,0,sizeof(a));
    for(int i=0; i<l; i++)
    {
        a[S[i]]++;
    }
    //ZERO
    y[0]=a['Z'];
    a['Z']-=y[0];
    a['E']-=y[0];
    a['R']-=y[0];
    a['O']-=y[0];
    //TWO
    y[2]=a['W'];
    a['T']-=y[2];
    a['W']-=y[2];
    a['O']-=y[2];
    //FOUR
    y[4]=a['U'];
    a['F']-=y[4];
    a['O']-=y[4];
    a['U']-=y[4];
    a['R']-=y[4];
    y[6]=a['X'];
    a['S']-=y[6];
    a['I']-=y[6];
    a['X']-=y[6];
    y[5]=a['F'];
    a['F']-=y[5];
    a['I']-=y[5];
    a['V']-=y[5];
    a['E']-=y[5];
    y[7]=a['V'];
    a['S']-=y[7];
    a['E']-=y[7];
    a['V']-=y[7];
    a['E']-=y[7];
    a['N']-=y[7];
    y[1]=a['O'];
    a['O']-=y[1];
    a['N']-=y[1];
    a['E']-=y[1];
    y[3]=a['R'];
    a['T']-=y[3];
    a['H']-=y[3];
    a['R']-=y[3];
    a['E']-=y[3];
    a['E']-=y[3];
    y[8]=a['H'];
    a['E']-=y[8];
    a['I']-=y[8];
    a['G']-=y[8];
    a['H']-=y[8];
    a['T']-=y[8];
    y[9]=a['I'];
    a['N']-=y[9];
    a['I']-=y[9];
    a['N']-=y[9];
    a['E']-=y[9];
//    while(y[0]+y[1]+y[2]+y[3]+y[4]+y[5]+y[6]+y[7]+y[8]+y[9] != 0)
    {
        ;
    }
    for( int i=0; i<10; i++)
    {
        for(int j=0; j<y[i]; j++)
            cout << i;
    }
}

int main()
{
    assert( freopen( inname, "r", stdin));
    assert( freopen( outname, "w", stdout));
    int T;
    cin >> T;
    for(int i=1; i<=T; i++)
    {
        cout << "Case #" << i << ": ";
        solve_case();
        cout << endl;
    }
}

