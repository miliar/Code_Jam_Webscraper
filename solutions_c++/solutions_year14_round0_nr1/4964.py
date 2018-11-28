#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdlib>
#include <iomanip>
#include <ctime>
#include <utility>
#include <fstream>

#define x first
#define y second
#define mp make_pair
#define pb push_back
#define sqr(x) (x)*(x)
#define _with_file
#define TASK ""
#define forn(i, n) for(int i = 0; i < (int)n; ++i)

#define getb(x,y) (x&(1<<y))
#define setb(x,y) (1|(1<<y))
#define unsetb(x,y) (x&(~(1<<y)))

void quit(); 

using namespace std;

typedef long long i64;
typedef unsigned long long u64;
typedef long double ld;
typedef pair <int, int> PII;
typedef pair <i64, i64> PII64;
typedef pair <ld, ld> PLL;

const ld EPS = 1e-12;
double __t;

int T,f,s;
int a[4][4],b[4][4];
vector <int> ans;

int main()
{
    #ifdef local
        __t = clock();
        #ifndef _with_files
            freopen("z.in", "rt", stdin);
            freopen("z.out", "wt", stdout);
        #endif
    #endif
    #ifdef _with_files
        freopen(TASK".in", "rt", stdin);
        freopen(TASK".out", "wt", stdout);
    #endif
                                                           
    cin >>T;
    forn(I,T)
    {
    	ans.clear();
    	cin >>f;
    	forn(i,4)
    		forn(j,4)
    			cin >>a[i][j];
    	cin >>s;
    	forn(i,4)
    		forn(j,4)
    			cin >>b[i][j];

        f--,s--;
    	forn(i,4)
    		forn(j,4)
    			if(a[f][i]==b[s][j])
    				ans.pb(a[f][i]);

    	cout <<"Case #"<<I+1<<": ";
    	if(ans.size()==1)
    		cout <<ans[0]<<endl;
    	else if(ans.size()==0)
    		cout <<"Volunteer cheated!"<<endl;
    	else
    		cout <<"Bad magician!"<<endl;
    }

    quit();
}

void quit()
{
    #ifdef LOCAL
        cerr << "\n\nTOTAL TIME: "<< (clock() - __t)/1000.0 << " s\n";
    #endif
    exit(0);        
}