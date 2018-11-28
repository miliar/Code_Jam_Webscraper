#include <bits/stdc++.h>

using namespace std;

int main()
{

    freopen("dip124.txt", "r", stdin);
    freopen("output2.txt", "w", stdout);


    long long int tc, i, j, len, count = 0;
    char str[1000001];

    cin >> tc;

    for(j = 1; j <= tc; j++)
    {
        count = 0;

        cin >> str;

        len = strlen(str);

        while(1)
        {
            i = 0;

            if(str[i] == '+')
            {
                while(str[i] == '+' && i < len) i++;

                if(i == len) break;
                else
                {
                    memset(str, '-', sizeof(char)*(i+1));
                    count += 1;
                }
            }

            else if(str[i] == '-')
            {
                while(str[i] == '-' && i < len) i++;
              
                if(i == len)
                {
                    count += 1;
                    break;
                }
                else
                {
                    memset(str, '+', sizeof(char)*(i+1));
                    count += 1;
                }

            }
        }
        cout << "case #" << j << ": " << count << "\n";
    }
    return 0;
}