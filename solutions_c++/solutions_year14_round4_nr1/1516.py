#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include "/home/mips/Desktop/codejam2014/utils.cpp"
#define FOR(i,n) for (int i = 0 ; i< n;i++)
#define FORI(i,s,e) for (int i = s ; i<= e;i++)
#define MP(x,y) make_pair(x,y)
#define PB(x) push_back(x)
#define ALL(x) x.begin(),x.end()
#define SZ(x) x.size()
#define FZ(x) memset(x,0,sizeof(x))
using namespace std;
FILE* fin;
FILE* fout;
int nTESTS;
int res;
int n,a,x;
vector<int> pk;
bool used[10001];
void read()
{
    pk.clear();
    fscanf(fin,"%d %d",&n,&x);
    FOR(i,n)
    {
        used[i] = false;
        fscanf(fin,"%d",&a);
        pk.PB(a);
    }
    sort(ALL(pk));
}

void solve()
{
    res = 0;
    for(int i = n-1; i>=0; i--)
    {
    for(int j = 0; j<n; j++)
    if (!used[j] && !used[i] && (pk[i] + pk[j] <=x))
    {
        used[i] = true;
        used[j] = true;
        res++;
    }
        if (!used[i])
        {
        used[i] = true;
        res++;
        }
    }
}

void write()
{
    fprintf(fout,"%d",res);
}



int main()
{
    fin = fopen("input.txt","r");
    fout = fopen("output.txt","w");

    fscanf(fin,"%d",&nTESTS);

    FOR(crtTest,nTESTS)
    {
        read();
        solve();
        fprintf(fout,"Case #%d: ",crtTest+1);
        write();
        fprintf(fout,"\n");
    }
    fclose(fout);

    return 0;
}
