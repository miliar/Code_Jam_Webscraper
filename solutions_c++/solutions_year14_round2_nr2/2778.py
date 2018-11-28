#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <bitset>
#include <map>
#include <cstring>
#include <string>
#include <sstream>
#include <set>
#include <stack>
#include <queue>
#include <cctype>
#include <math.h>
#include <cstdlib>

using namespace std;

#define I64 long long int
#define pii pair<int, int>
#define SIZE 1000
#define MAX 200
#define VI vector <int>
#define VS vector <string>
#define MSI map <string, int>
#define MIS map <int, string>
#define MSS map <string, string>
#define pb push_back
#define pob pop_back
#define mp make_pair
#define IT iterator
#define SET(a, b) memset( a, b, sizeof (a) )
#define READ(f) freopen(f, "r", stdin);
#define WRITE(f) freopen(f, "w", stdout);

int main()
{
    READ("B-small-attempt0.in");
    WRITE("out.txt");

    int tc, Case=1, a, b, k;

    scanf("%d", &tc);

    while( tc-- ){

        long int cnt = 0;
        scanf("%d%d%d", &a, &b, &k);

        for(int i=0; i<a; i++){

            if( i==0 ) cnt += b;

            else{

                for(int j=0; j<b; j++){

                    if( (i&j)<k )cnt++;
                }
            }
        }

        printf("Case #%d: %ld\n", Case++, cnt);
    }

    return 0;
}

