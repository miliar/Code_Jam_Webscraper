#include <iostream>
#include <bits/stdc++.h>
using namespace std;

string flip(string str , int start , int k)
{

    for (int i = start ;  i < k+start ; i++)
    {
        if (str[i] == '+') str[i] = '-' ;
        else str[i] = '+' ;
    }
    return str ;
}
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out1.txt", "w", stdout);
    int t , k ;
    cin >> t ;
    for(int i = 1 ; i <= t ; i++)
    {
        string str ;
        cin >> str ;
        cin >> k ;
        int mn = 0 ;
        for (int j = 0 ; j < str.size()-k+1 ; j++)
        {
            if (str[j] == '-')
            {
                str = flip(str , j , k) ;
                mn ++ ;
            }
        }

        for (int j = 0 ; j < str.size() ; j++)
            if (str[j] == '-') mn = -1 ;
        cout << "Case #" << i << ": " ;
        if (mn < 0)  cout << "IMPOSSIBLE\n" ;
        else cout << mn << endl ;
    }
    return 0;
}
