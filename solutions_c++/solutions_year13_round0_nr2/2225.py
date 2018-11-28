#include <iostream>
#include <fstream>

#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>

#include <algorithm>
#include <functional>
#include <sstream>
#include <utility>

#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

typedef vector<int>     vi;
typedef pair<int,int>   ii;
typedef vector<ii>      vii;
typedef long long       ll;
typedef set<int>        si;
typedef map<string,int> msi;

#define sz(a)   int((a).size())
#define all(c)  (c).begin(),(c).end()
#define pb(a)      push_back(a);
#define rep(i,n)    for(int i(0);i<int(n);i++)
#define TRvi(c,it)  for(vi::iterator it=(c).begin();it!=(c).end();it++)
#define INF 2E9

int N,M;
int board[100][100];

bool isPossible()
{
    rep(i,N)
        rep(j,M){
            bool row(true),col(true);
                rep(k,M)    if(board[i][k]>board[i][j])  row=false;
                rep(k,N)    if(board[k][j]>board[i][j])  col=false;
                if(row==false && col==false)    return false;
        }
    return true;
}
int main()
{
    ifstream fin("B-large.in");
    ofstream fout("out.txt");
    int T;
    fin>>T;
    rep(i,T){
        fout<<"Case #"<<i+1<<": ";
        fin>>N>>M;
        rep(i,N)
            rep(j,M){
                int a;  fin>>a;
                board[i][j]=a;
            }

        if(isPossible())   fout<<"YES"<<endl;
        else                    fout<<"NO"<<endl;
    }
    return 0;
}
