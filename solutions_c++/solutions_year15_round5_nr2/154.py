#pragma comment(linker, "/STACK:512000000")
#define _CRT_SECURE_NO_WARNINGS

#include "lp_lib.h"

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;

const int NMAX = 1005;
const double EPS = 1e-6;

int n, k;
int sum[NMAX];

lprec* build_model()
{
    lprec *lp = make_lp(0, n + 2);

    for1(i, n + 2)
    	set_int(lp, i, TRUE);

    for1(i, n + 2)
    	set_unbounded(lp, i);

    set_add_rowmode(lp, TRUE);


    REAL row[NMAX];
    int colno[NMAX];

    forn(i, n - k + 1)
    {    	
		forn(j, k)
		{
			row[j] = 1;
			colno[j] = i + j + 1;
		}    	

        add_constraintex(lp, k, row, colno, EQ, sum[i]);
    }

    forn(i, n)
    {
    	// x[i] <= mx
    	row[0] = 1; row[1] = -1; 
    	colno[0] = i + 1; colno[1] = n + 1;
    	add_constraintex(lp, 2, row, colno, LE, 0.0);

    	// x[i] >= mn
    	row[0] = 1; row[1] = -1;
    	colno[0] = i + 1; colno[1] = n + 2;
		add_constraintex(lp, 2, row, colno, GE, 0.0);

    }
    
    set_add_rowmode(lp, FALSE);
    
    row[0] = 1; row[1] = -1;
    colno[0] = n + 1; colno[1] = n + 2;

    set_obj_fnex(lp, 2, row, colno);
    set_minim(lp);

    write_lp(lp, "model.lp");     

    return lp;
}

void solve(int test)
{
    printf("Case #%d: ", test);

    scanf("%d %d", &n, &k);
    forn(i, n - k + 1) scanf("%d", &sum[i]);

    lprec* lp = build_model();

    set_outputstream(lp, stderr);

    int ret = solve(lp);

    if (ret != OPTIMAL)
    {
        cerr << ret << endl;
    }
    else
    {
     //   print_objective(lp);
     //   print_solution(lp, n + 2);       
     
        cout << get_objective(lp) << endl;
    }

    delete_lp(lp);    
}
int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);

    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) solve(it + 1);
    
    return 0;
}
