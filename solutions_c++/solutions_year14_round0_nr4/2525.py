#include <iostream>
#include <fstream>
#include <math.h>
#include <algorithm>
#include <stdio.h>
#define out "case #"
#define fail "impossible"
#define MAXN 1000
#define FOR(i,a,b) for(i=a;i<=b;i++)

using namespace std;

ifstream fin;
ofstream fout;

int main()
{
    int i,j,k,t,n,score_war,score_dec_war;
    double naomi[MAXN+1],ken[MAXN+1];

    fin.open("1.in",ios::in);

    fout.open("1_0.out");

    fout.precision(7);

    fin.seekg(0);

    fin>>t;

FOR(j,1,t)
{
    fin>>n;

    score_war=n; score_dec_war=0;

    FOR(i,1,n)
        fin>>naomi[i];

    FOR(i,1,n)
        fin>>ken[i];

    sort(naomi+1,naomi+n+1);
    sort(ken+1,ken+n+1);

    k=1;

    FOR(i,1,n)
    {
        while(ken[i]>naomi[k] && k<n) k++;
        if(k>n) break;
        if(ken[i]<naomi[k]) score_dec_war++;
        k++;
    }

    k=1;
    FOR(i,1,n)
    {
        while(naomi[i]>ken[k] && k<n) k++;
        if(k>n) break;
        if(naomi[i]<ken[k]) score_war--;
        k++;
    }

    fout<<out<<j<<": "<<score_dec_war<<' '<<score_war<<'\n';
}
fin.close();
fout.close();
    return 0;
}
