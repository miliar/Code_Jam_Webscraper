#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <cstring>
#include <climits>
#include <iostream>
#include <sstream>
#include <set>
#include <stack>
#include <queue>
#include <map>
#include <vector>
#include <algorithm>
#include <bitset>
#define ll long long
#define ull unsigned long long
#define inf 0x3f3f3f3f
#define infl 0x3FFFFFFFFFFFFFFFLL
#define np next_permutation
#define pp prev_permutation
#define mp make_pair
#define abs(x) (((x) < 0) ? - (x) : (x))
#define pi 3.1415926535897932384626433832795
#define sz(a) int((a).size()) 
#define fr first
#define sc second
#define pb push_back 
#define fors(i, s) for(int i = 0; i < sz(s); i++)
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for (__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define TRvii(c, it) for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define present(c,x) ((c).find(x) != (c).end()) 
using namespace std;

int main()
{
    freopen("D-small-attempt4.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
 
    int T=0;
    int x, r, c;
    
    cin >> T;
    for (int i=0; i<T ; i++)
    {
    	cin >> x;
    	cin >> r;
    	cin >> c;
    	cout << "Case #" << i+1;
    	
    	if (x == 1)
    	  cout << ": GABRIEL\n";
    	else if (r == 2 && c == 2)   //caso 1
    	{
    		if (x == 3 || x == 4)
    		   cout << ": RICHARD\n";
    		else 
    		  cout << ": GABRIEL\n";
		}
		else if ((r == 2 && c == 3) ||  (r == 3 && c == 2) )  //caso 2
		{
			if (x == 4)
    		   cout << ": RICHARD\n";
    		else 
    		  cout << ": GABRIEL\n";
		}
		else if ( r == 3 && c == 3 )  //caso 3
		{
			if (x == 2 || x == 4)
    		   cout << ": RICHARD\n";
    		else 
    		  cout << ": GABRIEL\n";
		}
		else if ( (r == 2 && c == 4) ||  (r == 4 && c == 2) ||  (r == 1 && c == 2) || (r == 2 && c == 1) ||  (r == 1 && c == 4) ||  (r == 4 && c == 1)  )  //caso 4, 8, 10
		{
			if (x == 3 || x == 4)
    		   cout << ": RICHARD\n";
    		else 
    		  cout << ": GABRIEL\n";
		}		
		else if ( (r == 3 && c == 4) ||  (r == 4 && c == 3)  )  //caso 5
		{
    		  cout << ": GABRIEL\n";
		}		
		else if (  (r == 4 && c == 4) )  //caso 6
		{
			if (x == 3)
    		   cout << ": RICHARD\n";
    		else 
    		  cout << ": GABRIEL\n";
		}
		else if ( (r == 1 && c == 1) || (r == 1 && c == 3) || (r == 3 && c == 1) )  //caso 7, 9
		{
			if (x == 2 || x == 3 || x == 4)
    		   cout << ": RICHARD\n";
    		else 
    		  cout << ": GABRIEL\n";  // não cai nessa
		}
	}
    
    return 0;
}


