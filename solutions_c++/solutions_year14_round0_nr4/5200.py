#include <bits/stdc++.h>
using namespace std ;
int main()
{
    freopen("input.txt","r",stdin) ;
    freopen("output.txt","w",stdout) ;
    int t ;
    cin >> t ;
    for ( int cs = 1 ; cs <= t ; ++cs )
    {
        int n ;
        vector <double> naomi , ken ;
        cin >> n ;
        for ( int i = 1 ; i <= n ; ++i )
        {
            double a ;
            scanf("%lf",&a) ;
            naomi.push_back(a) ;
        }
        for ( int i = 1 ; i <= n ; ++i )
        {
            double a ;
            scanf("%lf",&a) ;
            ken.push_back(a) ;
        }
        int x , y ;
        sort(naomi.begin(),naomi.end()) ;
        sort(ken.begin(),ken.end()) ;
        int cnt = 0 , j = 0 ;
        for ( int i = 0 ; i < ken.size() ; ++i )
        {
            if( ken[i] > naomi[j] )
            {
                ++cnt ;
                ++j ;
            }
        }
        y = n - cnt ;
        cnt = 0 ;
        map < double , int > flag ;
        for ( int i = naomi.size()-1 ; i >= 0 ; --i )
        {
            for ( int j = ken.size()-1 ; j >= 0 ; --j )
            {
                if ( naomi[i] > ken[j] && flag[ken[j]] == 0 )
                {
                    flag[ken[j]] = 1 ;
                    ++cnt ;
                    break ;
                }
            }
        }
        x = cnt ;
        printf("Case #%d: ",cs) ;
        cout << x << " " << y << endl ;
    }
}
