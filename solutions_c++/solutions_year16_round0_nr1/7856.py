#include <iostream>

using namespace std;

void funkcja (int t[] , int x)
    {
    while(x > 0)
        {
        t[x % 10] = 1 ;
        x /= 10 ;
        }
    }

main()
{
    int T ;
    cin >> T ;
    for(int a = 0 ; a < T ; a++)
        {
        int N , x = 0 , t[10] = {} ;
        cin >> N ;
        int b = N ;
        if(N == 0)
            {
            cout << "Case #" << a + 1 << ": INSOMNIA" << endl ;
            continue ;
            }
        while(1)
            {
            x += b ;
            funkcja(t,x) ;
            int c = 0 ;
            for( ; c < 10 ; c++)
                if(t[c] == 0) break ;
            if(c == 10) break ;
            }
        cout << "Case #" << a + 1 << ": " << x << endl ;
        }
    return 0 ;
}
