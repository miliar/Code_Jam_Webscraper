
#include <stdio.h>



#include <string>

#include <iostream>

using namespace std;
#define forn(i, n) for(int i = 0; i < (int)(n); i++)

// Problem B //
// H - 짤랐을 때의 요청된 길이 (1~100 밀리미터)
// N lines * M width..

int N,M;

string possibility[2] = {"NO", "YES"}; // 0 - NO, 1 - YES

// small : 1 <= N,M <= 10 , H 2;
// larget : 1 <= N,M <= 100, H 100
#define MAX_ELEMENT 10000
#define MAX_HEIGHT  100

int    lawn[MAX_ELEMENT];

#define toIndex(row,column) ((row)*M+(column) )

bool    checkPossible2 ( int row, int col , int height)
{
    int blocked = 0;

    
    // column check..
    forn(i,N)
    {
        if( lawn[toIndex(i, col)] > height)
        {
            blocked++;
            break;
        }
    }
    // row check..
    forn(j,M)
    {
        if( lawn[toIndex(row, j)] > height)
        {
            blocked++;
            break;
        }
    }
    
    //check if all the way is blocked..
    if (blocked == 2) {
        return false;
    }
    else
    {
        return true;
    }
}


void solve() {

    
    scanf("%d %d", &N, &M);
    
    forn(i, (N*M))
        scanf("%d", &lawn[i]);
    
    forn(i, N)
        forn(j, M)
        {
            if ( checkPossible2(i,j,lawn[toIndex(i, j)]) == false )
            {
                
                cout << possibility[0] << endl;
                return;
            }
        }
    cout << possibility[1] << endl;

}



int main() {
    
#ifdef ALEX_PRIVATE_TEST
    freopen("/Users/admin/Documents/input.txt", "rt", stdin);
    freopen("/Users/admin/Documents/output.txt", "wt", stdout);
#endif
    
    int tt;
    scanf("%d", &tt);
    forn(ii, tt) {
        printf("Case #%d: ", ii + 1);
        solve();
    }
    
    return 0;
}


