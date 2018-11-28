#include <iostream>
#include <bits/stdc++.h>
#include <string.h>
using namespace std;
int main()
{
    long long int t , j , l , count , i , k ;
    freopen("input_file_name.in","r",stdin);
    freopen("output_file_name.out","w",stdout);
    char s[101];
    cin >> t;
    j = 1;
    while(j <= t)
    {
        cin >> s;
        l = strlen(s);

        count = 0;
        for(i = l-1; i >= 0; )
        {
            if(s[i] == '+')
            {
                i--;
            }
            if(s[i] == '-')
            {
                count = 1;

                while((s[i] == '-') && (i >= 0))
                {
                    i--;

                }
                break;
            }

        }
        k = i;

        while(k >= 0)
        {
            if(s[k] == '-')
            {
                count++;
                while((s[k] == '-') && (k >= 0))
                {
                    k--;
                }
            }

            if(s[k] == '+')
            {
                count++;
                while((s[k] == '+') && (k >= 0))
                {
                    k--;
                }
            }
        }

        cout << "Case #" << j << ": " << count << endl;
        j++;

    }
    return 0;
}
