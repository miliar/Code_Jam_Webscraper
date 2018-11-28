#include <iostream>
#include <fstream>
#include <string>
using namespace std;
bool digits(long long x , bool arr[])
{
    while(x)
    {
        arr[x%10] = 1 ;
        x/=10 ;
    }
    for(int i = 0 ; i < 10 ; i++)
    {
        if(arr[i] == 0)
            return 0;
        else if(i == 9)
            return 1;
    }
}
int main()
{
    freopen("A-large.in" ,"r",stdin);
    freopen("he.out","w",stdout);
    int t ;
    cin >> t ;
    int cnt = 1 ;
    while(t--)
    {
        long long n , i = 1 ;
        bool arr[10] = {0} ;
        cin >> n ;
        int m = n*i ;
        if(n == 0)
        {
            cout << "Case #" << cnt << ": INSOMNIA" << endl ;
        }
        else
        {
            while(digits(m,arr) == 0)
            {
                i++ ;
                m=n*i ;
            }
            cout << "Case #" << cnt << ": " << m << endl ;
        }
        cnt++ ;
    }
    return 0;
}
