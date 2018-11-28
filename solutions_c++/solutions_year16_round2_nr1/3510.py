#include <bits/stdc++.h>

using namespace std;

int cnt[10][26] ;

int main()
{
    ios_base::sync_with_stdio(0) ;
    cin.tie(0) ;
    freopen("A-small-attempt0.in","r",stdin) ;
    freopen("out.txt","w",stdout) ;
    cnt[0]['Z'-'A']++ ; cnt[0]['E'-'A']++ ; cnt[0]['R'-'A']++ ; cnt[0]['O'-'A']++ ;
    cnt[1]['O'-'A']++ ; cnt[1]['N'-'A']++ ; cnt[1]['E'-'A']++ ;
    cnt[2]['T'-'A']++ ; cnt[2]['O'-'A']++ ; cnt[2]['W'-'A']++ ;
    cnt[3]['T'-'A']++ ; cnt[3]['H'-'A']++ ; cnt[3]['R'-'A']++ ; cnt[3]['E'-'A'] += 2 ;
    cnt[4]['F'-'A']++ ; cnt[4]['O'-'A']++ ; cnt[4]['U'-'A']++ ; cnt[4]['R'-'A']++ ;
    cnt[5]['F'-'A']++ ; cnt[5]['I'-'A']++ ; cnt[5]['V'-'A']++ ; cnt[5]['E'-'A']++ ;
    cnt[6]['S'-'A']++ ; cnt[6]['I'-'A']++ ; cnt[6]['X'-'A']++ ;
    cnt[7]['S'-'A']++ ; cnt[7]['E'-'A']+=2; cnt[7]['V'-'A']++ ; cnt[7]['N'-'A']++ ;
    cnt[8]['E'-'A']++ ; cnt[8]['I'-'A']++ ; cnt[8]['G'-'A']++ ; cnt[8]['H'-'A']++ ; cnt[8]['T'-'A']++ ;
    cnt[9]['N'-'A']+=2; cnt[9]['I'-'A']++ ; cnt[9]['E'-'A']++ ;
    int t ;
    cin >> t ;
    string s ;
    for ( int ctr = 1 ; ctr <= t ; ctr++ )
    {
        cin >> s ;
        int a[26] = {};
        for ( int i = 0 ; i < s.size() ; i++ )
            a[s[i]-'A']++ ;
        printf("Case #%d: ",ctr) ;
        bool ans = 0 ;
        for ( int i = 0 ; i < 700&& !ans ; i++ )
        {
            int b[26] = {} ;
            bool k = 1 ;
            for ( int j = 0 ; j < 26 ; j++ )
                b[j] += cnt[0][j]*i ,
                k &= ( b[j] <= a[j]) ;
            if ( !k )
            {
                for ( int j = 0 ; j < 26 ; j++ )
                    b[j] -= cnt[0][j]*i ;
                break ;
            }
            for ( int i1 = 0 ; i1 < 700 && !ans; i1++ )
            {
                bool k1 = 1 ;
                for ( int j = 0 ; j < 26 ; j++ )
                    b[j] += cnt[1][j]*i1 ,
                    k1 &= ( b[j] <= a[j] ) ;
                if ( !k1 )
                {
                    for ( int j = 0 ; j < 26 ; j++ )
                        b[j] -= cnt[1][j]*i1 ;
                    break ;
                }
                for ( int i2 = 0 ; i2 < 700 && !ans; i2++ )
                {
                    bool k2 = 1 ;
                    for ( int j = 0 ; j < 26 ; j++ )
                        b[j] += cnt[2][j]*i2 ,
                        k2 &= ( b[j] <= a[j] ) ;
                    if ( !k2 )
                    {
                        for ( int j = 0 ; j < 26 ; j++ )
                            b[j] -= cnt[2][j]*i2 ;
                        break ;
                    }
                    for ( int i3 = 0 ; i3 < 700 && !ans; i3++ )
                    {
                        bool k3 = 1 ;
                        for ( int j = 0 ; j < 26 ; j++ )
                            b[j] += cnt[3][j]*i3 ,
                            k3 &= ( b[j] <= a[j] ) ;
                        if ( !k3 )
                        {
                            for ( int j = 0 ; j < 26 ; j++ )
                                b[j] -= cnt[3][j]*i3 ;
                            break ;
                        }
                        for ( int i4 = 0 ; i4 < 700 && !ans; i4++ )
                        {
                            bool k4 = 1 ;
                            for ( int j = 0 ; j < 26 ; j++ )
                                b[j] += cnt[4][j]*i4 ,
                                k4 &= ( b[j] <= a[j] ) ;
                            if ( !k4 )
                            {
                                for ( int j = 0 ; j < 26 ; j++ )
                                    b[j] -= cnt[4][j]*i4 ;
                                break ;
                            }
                            for ( int i5 = 0 ; i5 < 700 && !ans; i5++ )
                            {
                                bool k5 = 1 ;
                                for ( int j = 0 ; j < 26 ; j++ )
                                    b[j] += cnt[5][j]*i5 ,
                                    k5 &= ( b[j] <= a[j] ) ;
                                if ( !k5 )
                                {
                                    for ( int j = 0 ; j < 26 ; j++ )
                                        b[j] -= cnt[5][j]*i5 ;
                                    break ;
                                }
                                for ( int i6 = 0 ; i6 < 700 && !ans; i6++ )
                                {
                                    bool k6 = 1 ;
                                    for ( int j = 0 ; j < 26 ; j++ )
                                        b[j] += cnt[6][j]*i6 ,
                                        k6 &= ( b[j] <= a[j] ) ;
                                    if ( !k6 )
                                    {
                                        for ( int j = 0 ; j < 26 ; j++ )
                                            b[j] -= cnt[6][j]*i6 ;
                                        break ;
                                    }
                                    for ( int i7 = 0 ; i7 < 700 && !ans; i7++ )
                                    {
                                        bool k7 = 1 ;
                                        for ( int j = 0 ; j < 26 ; j++ )
                                            b[j] += cnt[7][j]*i7 ,
                                            k7 &= ( b[j] <= a[j] ) ;
                                        if ( !k7 )
                                        {
                                            for ( int j = 0 ; j < 26 ; j++ )
                                                b[j] -= cnt[7][j]*i7 ;
                                            break ;
                                        }
                                        for ( int i8 = 0 ;i8 < 700 && !ans; i8++ )
                                        {
                                            bool k8 = 1 ;
                                            for ( int j = 0 ; j < 26 ; j++ )
                                                b[j] += cnt[8][j]*i8 ,
                                                k8 &= ( b[j] <= a[j] ) ;
                                            if ( !k8 )
                                            {
                                                for ( int j = 0 ; j < 26 ; j++ )
                                                    b[j] -= cnt[8][j]*i8 ;
                                                break ;
                                            }
                                            for ( int i9 = 0 ; i9 < 700 && !ans ; i9++ )
                                            {
                                                bool k9 = 1 ;
                                                for ( int j = 0 ; j < 26 ; j++ )
                                                    b[j] += cnt[9][j]*i9 ,
                                                    k9 &= ( b[j] <= a[j] ) ;
                                                if ( !k9 )
                                                {
                                                    for ( int j = 0 ; j < 26 ; j++ )
                                                        b[j] -= cnt[9][j]*i9 ;
                                                    break ;
                                                }
                                                if ( k9 )
                                                {
                                                    for ( int j = 0 ; j < 26 ; j ++ )
                                                        k9 &= (a[j] == b[j]) ;
                                                    if ( k9 )
                                                    {
                                                        ans = 1 ;
                                                        for ( int j = 0 ; j < i ; j++ ) printf("0") ;
                                                        for ( int j = 0 ; j < i1 ; j++ ) printf("1") ;
                                                        for ( int j = 0 ; j < i2 ; j++ ) printf("2") ;
                                                        for ( int j = 0 ; j < i3 ; j++ ) printf("3") ;
                                                        for ( int j = 0 ; j < i4 ; j++ ) printf("4") ;
                                                        for ( int j = 0 ; j < i5 ; j++ ) printf("5") ;
                                                        for ( int j = 0 ; j < i6 ; j++ ) printf("6") ;
                                                        for ( int j = 0 ; j < i7 ; j++ ) printf("7") ;
                                                        for ( int j = 0 ; j < i8 ; j++ ) printf("8") ;
                                                        for ( int j = 0 ; j < i9 ; j++ ) printf("9") ;
                                                    }
                                                }
                                                for ( int j = 0 ; j < 26 ; j++ )
                                                    b[j] -= cnt[9][j]*i9 ;
                                            }
                                            for ( int j = 0 ; j < 26 ; j++ )
                                                b[j] -= cnt[8][j]*i8 ;
                                        }
                                        for ( int j = 0 ; j < 26 ; j++ )
                                            b[j] -= cnt[7][j]*i7 ;
                                    }
                                    for ( int j = 0 ; j < 26 ; j++ )
                                        b[j] -= cnt[6][j]*i6 ;
                                }
                                for ( int j = 0 ; j < 26 ; j++ )
                                    b[j] -= cnt[5][j]*i5 ;
                            }
                            for ( int j = 0 ; j < 26 ; j++ )
                                b[j] -= cnt[4][j]*i4 ;
                        }
                        for ( int j = 0 ; j < 26 ; j++ )
                            b[j] -= cnt[3][j]*i3 ;
                    }
                    for ( int j = 0 ; j < 26 ; j++ )
                        b[j] -= cnt[2][j]*i2 ;
                }
                for ( int j = 0 ; j < 26 ; j++ )
                    b[j] -= cnt[1][j]*i1 ;
            }
            for ( int j = 0 ; j < 26 ; j++ )
                b[j] -= cnt[0][j]*i ;
        }
        printf("\n") ;
    }
    return 0;
}
