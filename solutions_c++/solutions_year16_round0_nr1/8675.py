/*** peace && PES College of Engineering, mandya ***** Krishna Keshav */
#include<iostream>
#include<vector>

using namespace std;
#define ll long long
int main()
{
    int digit[10];
    int t;
    cin >> t;
    int test = t;
    while(t--)
    {
        ll n , temp = 0 , ans , counter = 1;
        for(ll i = 0 ; i < 10 ; i++)
            digit[i] = 0;
        cin >> n;
        //cout << "Case #" << test - t << ": ";
        if(n == 0)
        {
            //cout << "INSOMNIA" << endl;
            cout << "Case #" << test - t << ": " << "INSOMNIA" << endl;
            continue;
        }
        while(1)
        {
            //n *= counter;
            ll num = n * counter;
            ans = n * counter;
            while(num != 0)
            {
                int r = num % 10;
                if(digit[r] == 0)
                    temp++;
                digit[r] = 1;
                num /= 10;
                //if(temp == 10)
                //    break;
            }
            if(temp >= 10)
                break;
            counter++;
           // cout << ans << " ";
        }
        cout << "Case #" << test - t << ": "  << ans << endl;

    }
    return 0;
}
