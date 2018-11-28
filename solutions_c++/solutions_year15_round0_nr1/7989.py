#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin>>T;
    for (int i = 0; i < T ; i++)
    {
        int y = 0;
        int sMax;
        string s;
        cin>>sMax;
        cin>>s;
        int counter = 0;
        for (int j = 0 ; j < sMax +1 ; j++)
        {
            if (j <= counter)
            {
                int x = s[j] - '0';
                counter+=x;
            }
            else
            {
                int x = s[j] - '0';
                if (x > 0)
                {
                    int add = j - counter;
                    y+=add;
                    counter+=add + x;
                }
            }
        }

        cout<<"Case #"<<i+1<<": "<<y<<endl;
    }
    fclose (stdin);
    fclose (stdout);
    return 0;
}


