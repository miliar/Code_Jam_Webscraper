#include <queue>
#include <map>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <stack>
#include <algorithm>
#include <bitset>
#include <sstream>
#include <string>
#include <cmath>
#include <stack>
#include <math.h>
#include <list>
#include <set>
#include <complex>
#include <string.h>

#define INF (1 << 29)
#define rep2(i,m,n) for(int i=(int)(m);i<(int)(n);i++)
#define rep(i,n) rep2(i,0,n)
#define squere(x) ((x)*(x))
#define EPS 1e-20

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> P;

int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};

int first[16],second[16];

string itos(int n){
    stringstream ss;
    ss << n;
    return ss.str();
}

string res(int ans1, int ans2)
{
    if(ans1<=0||ans1>4||ans2<=0||ans2>4) return "Volunteer cheated!";
    ans1--;
    ans2--;
    set<int> memo;
    rep(i,4) memo.insert(first[ans1*4+i]);
    set<int> memo2;
    rep(i,4){
        if(memo.find(second[ans2*4+i])!=memo.end()) memo2.insert(second[ans2*4+i]);
    }
    if(memo2.size()==1) return itos(*(memo2.begin()));
    else if(memo2.size()==0) return "Volunteer cheated!";
    else return "Bad magician!";
}

int main()
{
    int T;
    cin >> T;
    rep(i,T){
        int ans1,ans2;
        cin >> ans1;
        rep(j,16) cin >> first[j];
        cin >> ans2;
        rep(j,16) cin >> second[j];
        printf("Case #%d: %s\n",i+1,res(ans1,ans2).c_str());
    }
    return 0;
}

