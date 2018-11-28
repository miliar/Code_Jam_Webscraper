#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<cstring>
#include<string>
#include <sstream>
#include<set>
#include<stack>
#include<queue>
#include<cctype>
#include<math.h>
#include<cstdlib>

#define I64 long long int
#define pii pair<int, int>
#define SIZE 1000
#define MAX 20000
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

using namespace std;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int tc, r1, r2, data, res, Case=1;
    VI v1[5], v2[5];

    cin >> tc;

    while( tc-- ){

        int cnt = 0;
        cin >> r1;

        for(int i=1; i<5; i++){
            for(int j=0; j<4; j++){
                cin >> data;
                v1[i].pb(data);
            }
        }

        cin >> r2;

        for(int i=1; i<5; i++){
            for(int j=0; j<4; j++){
                cin >> data;
                v2[i].pb(data);
            }
        }

        for(int i=0 ; i<4; i++){

            int val = v1[r1][i];

            for(int j=0; j<4; j++){
                if( val == v2[r2][j] ){
                    cnt++;
                    res = val;
                    break;
                }
            }
        }

        if( cnt==1 ) printf("Case #%d: %d\n", Case++, res);
        if( cnt>1 ) printf("Case #%d: Bad magician!\n", Case++);
        else if( cnt==0 ) printf("Case #%d: Volunteer cheated!\n", Case++);

        for(int i=0; i<5; i++){
            v1[i].clear();
            v2[i].clear();
        }
    }
    return 0;
}

