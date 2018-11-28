#include <iostream>
#include <fstream>
#include <utility>
#include <string>
#include <cstring>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <vector>
#include <list>
#define pb(x) push_back(x)
#define FOR(i,n) for(;i<n;++i)
#define mod(x) (x<0)? -x:x
#define f first
#define s second
#define INF 1e9

using namespace std;
const int maxn = 1005;

int t;
char s[maxn];

int main()
{
	ifstream in("A-large.in");
	ofstream out("output.txt");

	in >> t;
	for( int x=1, n, sum, y; x<=t; ++x ){
        in >> n >> s;
        sum = s[0] - '0'; y = 0;
        for( int w=1; w<=n; ++w ){
            if( sum+y < w )
                y = w-sum;
            sum += s[w] - '0';
        }
        out << "Case #" << x << ": " << y << "\n";
	}

	return 0;
}
