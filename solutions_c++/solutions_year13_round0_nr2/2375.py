#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <cstdlib>
#include <string>
#include <sstream>

using namespace std;

#define VS vector<string>
#define VI vector<int>
#define VVI vector< VI >
#define pb push_back
#define mp make_pair
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORC(it,kont) for(__typeof((kont).begin()) it = (kont).begin(); it!=(kont).end(); ++it)

char buff[20000];

int ok[110][110];
int test( VVI s, int N, int M )
    {
    memset( ok, 0, sizeof(ok));
    int cnt = 0;
    int size = s.size() * s[0].size();
    
    while( cnt < size )
        {
        int inc = 0;
        VI rmin(N, 101);
        VI cmin(M, 101);
        VI rmax(N, 0);
        VI cmax(M, 0);
        int minmin = 101;
        FOR( i, 0, N ) 
            FOR( j, 0, M) 
                if( ok[i][j] == 0 )
                {
                rmin[i] = min( rmin[i], s[i][j] );
                cmin[j] = min( cmin[j], s[i][j] );
                rmax[i] = max( rmax[i], s[i][j] );
                cmax[j] = max( cmax[j], s[i][j] );
                minmin = min( minmin, s[i][j] );
                }
        FOR( i, 0, N )
            if( rmin[i] == rmax[i] && rmin[i] == minmin )
                {
                FOR ( j, 0, M )
                    { if( ok[i][j] == 0 ) ++cnt; ok[i][j] = 1; inc = 1; }
                }
        FOR( j, 0, M )
            if( cmin[j] == cmax[j] && cmin[j] == minmin )
                {
                FOR ( i,0, N )
                    { if( ok[i][j] == 0 ) ++cnt; ok[i][j] = 1; inc = 1;}
                }
        if( inc == 0 ) 
            return 0;
        }
    if ( cnt == size )
        {
        return 1;
        }
    return 0;
    }

int main()
    {
    int T;
    gets(buff);
    sscanf(buff,"%d",&T);

    FOR( t, 0, T )
        {
        int N, M;
        cin >> N  >> M;
        VVI s(N, VI(M) );
        FOR( i, 0, N ) FOR( j, 0, M ) cin >> s[i][j];

        //FOR( i, 0, N ) FOR( j, 0, M ) cout << s[i][j];

        if( test( s, N, M) )
            printf("Case #%d: YES\n",t+1);
        else
            printf("Case #%d: NO\n",t+1);
        }
    return 0;
    }
