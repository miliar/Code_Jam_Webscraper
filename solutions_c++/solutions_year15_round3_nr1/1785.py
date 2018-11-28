#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <string.h>
#include <strings.h>
#include <math.h>
#include <time.h>

using namespace std;

//Two of the most frequently used typical of long names, make life easier
typedef vector<int> VI;
typedef long long LL;

/* HEADERS */
// FOR - loop increasing 'x' from 'b' to 'e' inclusive
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
// FORD - loop decreasing 'x' from 'b' to 'e' inclusive
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
// REP - loop increasing 'x' from '0' to 'n'. Used to search and build DS
#define REP(x, n) for(int x = 0; x < (n); ++x)
// Clone long type of 'n'
#define VAR(v, n) __typeof(n) v = (n)
// ALL(c) represents the pair of iterators, indicating begin-end elements in the STL DS
#define ALL(c) (c).begin(), (c).end()
//Macro to get size of STL DS, used to avoid compilation warrning with int and uint comp
#define SIZE(x) ((int)(x).size())
// Very profitable macro aimed to iterate through all elements of STL DS
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
/* Shortcuts */
#define PB push_back
#define POP pop_back
#define ST first
#define ND second

int solution(int c, int r, int w);

int board[21];

inline void clean_board(){
	for(int j=0; j<21; j++)
		board[j] = 0;
}

int main()
{
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int tests;
    cin >> tests;

    REP(x, tests){
        
	int c, r, w;  
	cin >> r; cin >> c; cin >>w;
	clean_board();
        int result = solution(c, r, w);

        cout << "Case #" << x+1 << ": ";
        cout << result << endl;
    }


    return 0;
}

int solution(int c, int r, int w){
 	if(w==1) return c*r;
        int result = 0;	

	//eliminate 2D 
	result = (r-1)*c/(w-1);
//cout<< "w="<<w << " ";
	int li;
	//ship must be in last row
	for(int i=1; i<c; i++) {
		if(i%(w) == 0){
//cout << "i%(w-1)" <<i%(w-1) << " ";
			board[i] = 1;	
			result ++; li = i;		
		}
	}
	

	return result + w;
}
