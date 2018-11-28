#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    freopen("B-large.in" ,"r",stdin);
    freopen("out.out","w",stdout);
    int t , x = 0 ;
    cin >> t ;
    while(t--)
    {
        x++ ;
        int cnt = 0 ;
        string s ;
        cin >> s ;
        char c = '-' ;
        for(int i = 0 ; i < s.size() ; i++)
        {
            if(c != s[i])
            {
                if(c == '+' && s[i] == '-')
                {
                    cnt++ ;
                    c = '-' ;
                }
                else
                    c = '+';
            }
        }
        cnt*=2 ;
        if(s[0] == '-')
        {
            cnt++ ;
        }
        cout << "Case #" << x << ": " << cnt << endl ;
    }

    return 0;
}
