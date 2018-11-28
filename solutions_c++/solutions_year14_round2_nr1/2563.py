#include <iostream>
#include <algorithm>

using namespace std;

int makeRef( char* a, char* b )
{
    int j=0;
    a[0] = b[0];
    for( int i=1; b[i]!=0; i++ )
        if( a[j] != b[i] )
        {
            a[++j] = b[i];
        }
    
    a[++j] = 0;
    
    //printf("--- %s %s\n", b, a);
    return j;
}

void setCount( char* a, int* b )
{
    char last = a[0];
    int cnt = 1;
    int j=0;
    for( int i=1; ; i++ )
    {
        if( a[i] != last )
        {
            b[j++] = cnt;
            cnt = 1;
            last = a[i];
        }
        else cnt++;
        
        if( a[i] == 0 )
            break;
    }
    
    //printf("@@@ %s", a);
    //for( int i=0; i<j; i++ )
    //    printf(" %d", b[i]);
    //puts("");
}

int compRef( char* ref, char* a )
{
    char test[110];
    makeRef( test, a );
    
    int i;
    for( i=0; test[i]!=0 && ref[i]!=0; i++ )
        if( test[i] != ref[i] )
            break;
    //printf("#### %s %s\n", ref, a);
    
    if( test[i] == 0 && ref[i] == 0 )
        return 1;
    return 0;
}

int main()
{
    int tt;
    scanf("%d", &tt);
    for( int t=1; t<=tt; t++ )
    {
        int n;
        char str[110][110];
        int cnt[110][110];
        char ref[110];
        int size = 0;
        int flag = 1;
        
        scanf("%d", &n);
        
        scanf("%s", str[0] );
        size = makeRef( ref, str[0] );
        setCount( str[0], cnt[0] );
        
        for( int i=1; i<n; i++ )
        {
            scanf("%s", str[i]);
            
            setCount( str[i], cnt[i] );
            flag &= compRef( ref, str[i] );
            //printf("^^^^ %d\n", flag);
        }
        
        int cost = 0;
        if( flag == 1 )
        {
            for( int i=0; i<size; i++ )
            {
                int sum = 0;
                for( int j=0; j<n; j++ )
                    sum += cnt[j][i];
                
                int avg = (int)(0.5 + sum/(double)n);
                
                for( int j=0; j<n; j++ )
                    cost += abs(cnt[j][i] - avg);
            }
            
            printf("Case #%d: %d\n", t, cost);
        }
        else printf("Case #%d: Fegla Won\n", t);
    }
    
    return 0;
}