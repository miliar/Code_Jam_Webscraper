#include <iostream>
#include <set>

using namespace std;

int main()
{
    int t;
    scanf("%d", &t);
    
    for( int tt = 1; tt<=t; tt++ )
    {
        int a, b;
        int first[16], second[16];
        scanf("%d", &a);
        
        for( int i=0; i<16; i++ )
            scanf("%d", &first[i]);
        
        scanf("%d", &b);
        for( int i=0; i<16; i++ )
            scanf("%d", &second[i]);
        
        set<int> row;
        int ans = 0;
        int flag = 0;
        
        for( int i=(a-1)*4; i<a*4; i++ )
            row.insert(first[i]);
        
        for( int i=(b-1)*4; i<b*4; i++ )
            if( row.find(second[i]) != row.end() )
            {
                ans = second[i];
                flag ++;
            }
        
        printf("Case #%d: ", tt);
        if( flag == 1 )
            printf("%d\n", ans);
        if( flag == 0 )
            printf("Volunteer cheated!\n");
        if( flag > 1 )
            printf("Bad magician!\n");
        
    }
    return 0;
}