#include <cstdlib>
#include <stdlib.h> 
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <bitset>
#include <iterator>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <complex>
#include <cmath>
#include <ctime>
#include <limits>
#include <cassert>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;

const double precision = 1e-11; // The E11 means 10 to the 11th power. So 1 E 11 means 1 times 10^11, or 100,000,000,000.

#define fr(i, a, b) for(i = (a); i < (b); ++i)
#define fre(i, a, b) for(i = (a); i <= (b); ++i)
#define rfr(i, a, b) for(i = (a) - 1; i >= (b); --i)
#define sz(a) int((a).size())
#define clr(a, b) memset(a, b, sizeof(a))
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find( all(c),x) != (c).end())
#define dbg(x) cerr << #x << " = " << x << "\n";

template<class T> bool isPalindrome(T x) 
{ 
    T t = x; T s = 0; T r = 0;
    
    if ( x < 10 ) return true;
    while(x)
    {
        r = x % 10;
        x = x / 10;
        s = s * 10 + r;
    }    
    if(t == s) return true;     
    return false; 
}

int main() 
{
    int T = 0, i = 0;
    ull A = 0, B = 0, k = 0;

    //ifstream fin("../src/input.txt");
    
    ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");
    
    fin >> T; 
    fr(i, 0, T)
    {   
        ull ans = 0;
        fin >> A >> B;
        k = 1;
        while(true)
        {
            ull n = k*k;
            if ( isPalindrome(k) ) 
            {                
                if ( n >= A && n <=B )
                    if ( isPalindrome(n) )
                        ans++;                
            }
            if ( n >= B ) break;
            k++;
        }
        fout << "Case #" << i+1 << ": " << ans << endl;
    }
}