#include <iostream>
#include<bits/stdc++.h>
#define ll long long int
using namespace std;


int main()
{
    freopen("input_file_name.in","r",stdin);
    freopen("output_file_name.out","w",stdout);
    ll t , i , l , j;
    char temp;

    cin >> t;
    i = 1;
    while(i <= t)
    {
        string s , str;
        cin >> s;
        l = s.length();

        for(j = 0; j < l; j++)
        {
            if(j == 0)
            {
                temp = s[0];
                str = str + s[0];
            }
            else
            if(temp > s[j])
            {
                str = str + s[j];
            }
            else
            {
                str = s[j] + str;
                temp = s[j];
            }
        }

        cout << "Case #" << i << ": " << str << endl;

        i++;
    }



	return 0;
}
