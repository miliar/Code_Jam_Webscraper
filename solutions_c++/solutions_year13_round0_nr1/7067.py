/*
http://codingaquarium.wordpress.com/
Shaikh shiam Rahman

*/
#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <memory>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#include <iomanip>

using namespace std;

/*** typedef ***/

#define MEMSET_INF 127
#define MEMSET_HALF_INF 63
#define stream istringstream
#define rep(i,n) for(__typeof(n) i=0; i<(n); i++)
#define repl(i,n) for(__typeof(n) i=1; i<=(n); i++)
#define FOR(i,a,b) for(__typeof(b) i=(a); i<=(b); i++)
#define INF (1<<30)
#define PI acos(-1.0)
#define pb push_back
#define ppb pop_back
#define all(x) x.begin(),x.end()
#define mem(x,y) memset(x,y,sizeof(x))
#define memsp(x) mem(x,MEMSET_INF)
#define memdp(x) mem(x,-1)
#define memca(x) mem(x,0)
#define eps 1e-9
#define pii pair<int,int>
#define pmp make_pair
#define ft first
#define sd second
#define vi vector<int>
#define vpii vector<pii>
#define si set<int>
#define msi map<string , int >
#define mis map<int , string >
typedef long long i64;
typedef unsigned long long ui64;

/** function **/

#define SDi(x) sf("%d",&x)
#define SDl(x) sf("%lld",&x)
#define SDs(x) sf("%s",x)
#define SD2(x,y) sf("%d%d",&x,&y)
#define SD3(x,y,z) sf("%d%d%d",&x,&y,&z)
#define pf printf
#define sf scanf

#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

int main()
{
#ifndef ONLINE_JUDGE
	READ("in.txt");
	WRITE("out_large.txt");
#endif
    int tc,cas=1;
    cin>>tc;
    //getchar();
    while(tc--)
    {
        pf("Case #%d: ",cas++);
        string ss[4];
        rep(i,4)
            cin>>ss[i];

        int countX,countO,freeCell = 0;
        bool failure = true;

        /**** checking main diagonal ****/
        if(failure){
            countX = countO = 0;
            rep(i,4)
                if(ss[i].at(i) == 'X')
                    countX++;
                else if(ss[i].at(i) == 'O')
                    countO++;
                else if(ss[i].at(i) == 'T'){
                    countO++;countX++;
                }

            if(countX == 4 ) puts("X won");
            else if(countO == 4) puts("O won");

            if(countO == 4 or countX == 4)
                failure = false;
        }

        /**** checking sub diagonal ****/
        if(failure){
            countX = countO = 0;
            rep(i,4){
                unsigned pter = 3 - i;//nxt_pter = 3 - i - 1;
                if(ss[i].at(pter) == 'X')
                    countX++;
                else if(ss[i].at(pter) == 'O')
                    countO++;
                else if(ss[i].at(pter) == 'T'){
                    countO++;countX++;
                }

                if(countX == 4 ) puts("X won");
                else if(countO == 4) puts("O won");

                if(countO == 4 or countX == 4)
                    failure = false;
            }
        }

        /***** checking row ***/
        if(failure){
            rep(i,4){
                countO = countX = 0;
                rep(j,4)
                    if(ss[i].at(j) == 'X')
                        countX++;
                    else if(ss[i].at(j) == 'O')
                        countO++;
                    else if(ss[i].at(j) == 'T'){
                        countO++;countX++;
                    }
                    else if(ss[i].at(j) == '.' )
                        freeCell++;

                if(countX == 4 ) puts("X won");
                else if(countO == 4) puts("O won");

                if(countO == 4 or countX == 4) {
                    failure = false;
                    break;
                }
            }
        }

        /***** checking column ***/
        if(failure){
            rep(i,4){
                countO = countX = 0;
                rep(j,4)
                    if(ss[j].at(i) == 'X')
                        countX++;
                    else if(ss[j].at(i) == 'O')
                        countO++;
                    else if(ss[j].at(i) == 'T'){
                        countO++;countX++;
                    }
                    else if(ss[i].at(j) == '.' )
                        freeCell++;

                if(countX == 4 ) puts("X won");
                else if(countO == 4) puts("O won");

                if(countO == 4 or countX == 4) {
                    failure = false;
                    break;
                }
            }
        }

        /**** if no one wins ***/
        if(failure){
            if(freeCell)
                puts("Game has not completed");
            else puts("Draw");
        }
    }
    return 0;
}
