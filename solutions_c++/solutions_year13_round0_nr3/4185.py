#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <deque>
#include <cmath>
using namespace std;

ifstream f("nume.in");
ofstream g("nume.out");

#define nmax 10000005
#define ll long long

int rez[nmax];

inline bool pal(ll X){
    ll invers = 0LL;
    ll X2 = X;
    while(X){
        invers = invers*10LL + X % 10;
        X /= 10;
    }
    //cout << X2 << " " << invers << "\n";
    if (X2 == invers) return 1;
    return 0;
}

void preproces(){
    ll sqrtX = sqrt(100000000000000) + 1;
    int cnt = 0;
    for(ll i=1LL; i<=sqrtX; ++i){
        ll newI = i*i;
        if ( pal(i)==1 && pal(newI)==1 ){
            ++cnt;
        }
        rez[i] = cnt;
        //cout << cnt << " ";
    }
}

void rezolva(){
    int t = 0;
    f >> t; ll A = 0LL; ll B = 0LL;
    preproces();
    for(int i=1; i<=t; ++i){
        f >> A >> B;
        ll sqrtA = sqrt(A);
        ll sqrtB = sqrt(B);
        //cout << sqrtA << " " << sqrtB << "\n";
        if (sqrtA * sqrtA != A) sqrtA+=1LL;
        //g << rez[sqrtB] - rez[sqrtA-1] << "\n";
        g << "Case #" << i << ": " << rez[sqrtB] - rez[sqrtA-1] << "\n";
    }
}

int main(){
    rezolva();

    f.close();
    g.close();

    return 0;
}

