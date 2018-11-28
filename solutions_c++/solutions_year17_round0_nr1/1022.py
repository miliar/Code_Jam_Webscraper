#include <vector>
#include <iostream>

using namespace std ;


int T, ans, K ;
string s ;

int main()
{
    ios::sync_with_stdio(false) ;
    cin.tie(0) ;

    cin >> T ;

    for(int c = 1 ; c <= T ; c++)
    {
        cin >> s >> K ;

        s = " " + s ;
        int till = (int)s.size() ;
        till-- ;

        ans = 0 ;
        for(int i = 1 ; i <= till-K+1 ; i++)
        {
          //  cout << "I = " << i << ", string = " << s << "\n" ;

            if(s[i] == '+')
                continue ;

            ans++ ;
            for(int j = i ; j <= i+K-1 ; j++)
            {
                if(s[j] == '+')
                    s[j] = '-' ;
                else
                    s[j] = '+' ;
            }
        }

        for(int i = 1 ; i <= till ; i++)
            if(s[i] == '-')
                ans = -1 ;

        cout << "Case #" << c << ": " ;

        if(ans == -1)
            cout << "IMPOSSIBLE\n" ;
        else
            cout << ans << "\n" ;
    }   

    
    
    
    return 0;
}