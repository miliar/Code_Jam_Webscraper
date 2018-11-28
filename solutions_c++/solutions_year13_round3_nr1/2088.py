#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
using namespace std;

bool canBeTaken(string str, int n)
{
    int sum = 0;

    if(str.length() >= n)
    {
        for(int p = 0; p < str.length() && sum < n; p++)
        {
            if( str[p] == 'a' || str[p] == 'e' || str[p] == 'i' || str[p] == 'o' || str[p] == 'u' || str[p] == 'A' || str[p] == 'E' || str[p] == 'I' || str[p] == 'O' || str[p] == 'U' )
                sum = 0;
            else
                sum++;
        }
    }

    if(sum >= n)
        return true;

    return false;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T, CV = 1 ;
    cin >> T;

    while(T--)
    {


        string str;     int n;
        cin >> str >> n;

        vector<string> v;

        for(int i = 0; i < str.length(); i++)
            for(int j = 1; j <= str.length()-i; j++)
                v.push_back( str.substr(i,j) );

        int total = 0;

        for(int i = 0; i < v.size(); i++)
        {
            if(canBeTaken( v[i], n ))
                ++total;
        }

        cout << "Case #" << CV++ << ": " << total << endl;
    }

    return 0;
}
