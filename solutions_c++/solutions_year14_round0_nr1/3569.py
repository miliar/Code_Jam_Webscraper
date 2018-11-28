#include <cstdio>
#include <cstdlib>

using namespace std;

int s1[5][5], s2[5][5];
bool row1[17], row2[17];

int main()
{
    int cases;
    scanf("%d", &cases);
    for( int tt = 1; tt <= cases; tt++ )
    {
        int a, b;
        int cnt = 0, ans;
        for( int i = 1; i <= 16; i++ ) row1[i] = row2[i] = false;
        
        scanf("%d", &a);
        for( int i = 0; i < 4; i++ )
            for( int j = 0; j < 4; j++ ) scanf("%d", &s1[i][j]);
        scanf("%d", &b);
        for( int i = 0; i < 4; i++ )
            for( int j = 0; j < 4; j++ ) scanf("%d", &s2[i][j]);
        
        for( int i = 0; i < 4; i++ ) row1[s1[a - 1][i]] = true;
        for( int i = 0; i < 4; i++ ) row2[s2[b - 1][i]] = true;
        
        for( int i = 1; i <= 16; i++ )
            if( row1[i] && row2[i] )
            {
                cnt++;
                ans = i;
            }
        
        printf("Case #%d: ", tt);
        if( cnt == 0 ) puts("Volunteer cheated!");
        else if( cnt == 1 ) printf("%d\n", ans);
        else puts("Bad magician!");
    }
    return 0;
}
