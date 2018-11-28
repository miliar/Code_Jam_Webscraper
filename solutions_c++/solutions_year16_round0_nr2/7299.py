#include<bits/stdc++.h>
using namespace std;
string flip(string s , int ind , int &cnt)
{
    for(int i = 0; i < ind + 1 ;i ++)
    {
        if(s[i] == '+')
            s[i] = '-';
        else s[i] = '+';
    }
    cnt ++ ;
    reverse(s.begin() , s.begin() + ind + 1);
    return s;
}
int last(string s)
{
    for(int i = s.size() - 1; i >= 0 ;i --)
        if(s[i] == '-')
            return i;
    return -1;
}
string begin(string s , int &cnt)
{
    int dx = -1;
    for(int i = 0; i < s.size() && s[i] == '+' ; i ++)
        dx = i;
    if(dx != -1)
        return flip(s , dx , cnt);
    return s;
}
bool f(string s)
{
    for(int i = 0; i < s.size() ;i ++)
        if(s[i] == '-')
            return 1;
    return 0;
}
int main()
{
    string s;
    int t;
    freopen("Revenge of the Pancakes.in" , "r" , stdin);
    freopen("Revenge of the Pancakes.out" , "w" , stdout);
    cin >> t;
    for(int i = 1 ;i <= t ;i ++){
        cin >> s;
        int cnt = 0;
        while(f(s))
        {
            s = begin(s , cnt);
            int k = last(s);
            if(k != -1)
                s = flip(s , k , cnt);
        }
        cout << "Case #" << i << ": " << cnt << endl;
    }
}
