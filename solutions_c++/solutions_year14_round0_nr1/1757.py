#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
#include <conio.h>
#include <iomanip>
#include <sstream>

#define fo(a, b, c) for(a = ( b ); a < ( c ); a++)
#define fr(a, b) fo(a, 0, ( b ))
#define fi(a) fr(i, ( a ))
#define fj(b) fr(j, ( b ))
#define fk(c) fr(k, ( c ))

#define ul64 uint_least64_t
#define vs vector<string>
#define vi vector<int>
#define vd vector<double>
#define vul64 vector<ul64>
#define vc vector<char>
#define pb push_back
#define ppb pop_back
#define ss stringstream

#define ROWS 4
#define COLS 4

using namespace std;

char outs[][20] = {"Bad magician!", "Volunteer cheated!"};

vi fetch(int n)
{
    vi l;
    l.clear();
    int t, i, j;
    //cout<<n<<endl;
    fi(ROWS) fj(COLS){
        cin>>t;
        if((i+1) == n) l.pb(t);
    }
    return l;
}


int solve(vi a, vi b, int n)
{
    int i, j, k = -1;
    cout<<"Case #"<<n<<": ";
    fi(ROWS) fj(COLS){
        if((a[i] == b[j]) && k != -1){ cout<<outs[0]<<endl; return 0; }
        if((a[i] == b[j]) && k == -1)
        k = i;
    }

    if(k == -1) { cout<<outs[1]<<endl; return 1; }
    else { cout<<a[k]<<endl; return 2; }
    return -1;
}
int main()
{
    int i, j, k, tt, cases, one, two;
    vi row, col;
    int t;

    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-0.out", "w", stdout);
    cin>>tt;
    fr(cases, tt)
    {
        row.clear();
        col.clear();

        cin>>one;
        row = fetch(one);

        cin>>two;
        col = fetch(two);

        solve(row, col, cases+1);
    }
}
