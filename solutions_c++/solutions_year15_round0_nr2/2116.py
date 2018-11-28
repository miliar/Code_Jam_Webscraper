#include <bits/stdc++.h>
#define mp make_pair
#define ll long long

using namespace std;

vector<int>v;

int solve(int x , vector <int> v)
{
    sort(v.rbegin() , v.rend());
    int t=0;
    for(int i = 0 ; i < v.size() ; i++)
    {
        t+=(v[i]-1)/x;
    }
    return t;
}

int main()
{
    freopen( "in.txt" , "r" , stdin);
    freopen( "out.txt" , "w" , stdout);
    int t;
    cin >> t;
    int a=1;
    while(a<=t)
    {
        int d;
        cin >> d;
        v.clear();
        for(int i = 0 ; i < d ; i++)
        {
            int x;
            cin >> x;
            v.push_back(x);
        }
        sort(v.rbegin() , v.rend());
        int m = v[0];
        for(int i = 1 ; i < m ; i++)
        {
            m = min (m , solve( i , v)+i);
        }
        cout << "Case #" << a++ <<": " << m << endl;
    }
}
