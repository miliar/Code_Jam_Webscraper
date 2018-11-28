#include <bits/stdc++.h>

using namespace std;

int n ;
int a[1010] , x ;
int main()
{
    freopen("C-small-attempt0.in","r",stdin) ;
    freopen("OUT.txt","w",stdout) ;
    int t ;
    cin >> t ;
    a[0] = -1 ;
    for ( int ct = 1 ; ct <= t ; ct++ )
    {
        cin >> n ;
        for ( int i = 0 ; i < n ; i++ ) cin >> a[i]  ,a[i]--;
        int arr[11] ;
        for ( int i = 0 ; i < n ; i++ ) arr[i] = i ;
        int ans = 0 ;
        do
        {
            for ( int i = 1 ; i <= n ; i++ )
            {
                int cnt = 0 ;
                for ( int j = 0 ; j < i ; j++ )
                {
                    if ( a[arr[j]] == arr[(j+1)%i] || a[arr[j]] == arr[(j-1+i)%i] ) cnt++ ;
                    else cnt = -1e5 ;


                }

                ans = max(ans,cnt) ;
            }
        }
        while ( next_permutation(arr,arr+n)) ;
        cout << "Case #" << ct << ": " << ans << endl;
    }
    return 0;
}
