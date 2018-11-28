#include<bits/stdc++.h>
using namespace std;
set <long long int> s;
int main()
{
    long long int t , i , n , m , a , ans , j , k;
    freopen("input_file_name.in","r",stdin);
    freopen("output_file_name.out","w",stdout);

    cin >> t;
    i = 1;
    while(i <= t)
    {
        j = 0;
        cin >> n;
        if(n == 0)
        {
             cout << "Case #" << i << ": INSOMNIA"<< endl;
        }
        else
        {
            m = n;
            k = n;
            loop: while(m > 0)
            {
                a = m%10;
                s.insert(a);
                m = m/10;

            }
            ans = s.size();


            if(ans == 10)
            {
                cout << "Case #" << i << ": " << k << endl;

            }
            else
            {
                j++;
                m = n*j;

                k = m;

                goto loop;
            }
        }
        i++;
        s.clear();

    }
    return 0;
}

