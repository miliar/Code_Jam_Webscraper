#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
#include <bitset>
#include <climits>
#include <stack>
#include <cctype>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;


int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    vector<double> p1  , p2 ;
    int T ;
    cin>>T ;
    int cnt = 1;
    while(T--)
    {
        int N ;
        double t  ;
        p1.clear() ;
        p2.clear() ;
        cin>>N ;
        for(int i=0 ; i < N ; i++ )
        {
            cin>>t ;
            p2.push_back(t) ;
        }
        for(int i=0 ; i < N ; i++ )
        {
            cin>>t ;
            p1.push_back(t) ;
        }

        sort(p1.begin() , p1.end() ) ;
        sort(p2.begin() , p2.end() ) ;





        int cnt1  = 0 ;

        int i = 0 , j = 0 ;

        while(i<N && j<N )
        {
            if(p2[i]>p1[j])
            {
                cnt1++ ;
                i++ ;
                j++ ;
            }
            else
            {
                i++ ;
            }
        }

        i = 0 ;
        j = 0 ;
        int cnt2  = 0 ;
        while(i<N && j<N )
        {

            while( p1[j] <= p2[i] && j<N  )
                j++ ;

            if(j==N)
                break ;

            if( p1[j] > p2[i] )
            {
                cnt2++ ;
                i++ ;
                j++ ;
            }
        }

        cout<<"Case #"<<cnt++<<": "<<cnt1<<" "<<N-cnt2<<endl ;


    }
    return 0 ;
}
