#include <iostream>
#include <cstdio>
#include <fstream>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <sstream>
#include <vector>
#include <utility>
#include <stack>
#include <queue>
#include <map>
#include <list>
#include <deque>
#include <set>

#define LL long long
#define ULL unsigned long long
#define ST string
#define do double
#define pi 2*acos(0.0)
#define gb 10000000
#define f(j,k) for ((j) = 1; (j) <= (k); (j)++)
#define F(j,k) for ((j) = (k); (j) >= 0; (j)++)
#define ff(j,k,l) for ((j) = (k); (j) < (l); (j)++)
#define br break
#define pb push_back
#define fx fixed
#define sp setprecision
#define ve vector
#define st first
#define nd second
#define bs binary_search
#define np next_permutation
#define pp previous_permutation
#define gl(j) getline(cin,(j))
#define sst(j,k) stringstream((j))>>(k)
#define C fin
#define co fout
#define E fout<<endl

using namespace std;

LL a,b,c,d,e,g,h,x,y;

int main() {
    ofstream fout ("B-small-attempt1.out");
    ifstream fin ("B-small-attempt1.in");
    C>>a;
    f(b,a) {
    	co<<"Case #"<<b<<": ";
    	C>>c>>d>>e; x=0;
    	ff(g,0,c) {
    		ff(h,0,d) {
    			y=(g&h);
    			if (y<e) x++;
    		}
    	}
    	co<<x;
    	E;
    }
    return 0;
}
