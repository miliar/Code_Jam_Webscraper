/*
Author: aseemraj
Problem: Standing Ovation
*/

#include <bits/stdc++.h>
#define loop(i, a, b) for(int i=a; i<b; i++)
#define rloop(i, a, b) for(int i=b-1; i>=a; i--)
#define V(x) vector< x >
#define P(x, y) pair< x, y >
#define PI P(int, int)
#define PLL P(ll, ll)
#define VI V(int)
#define VLL V(ll)
#define VP V(PI)
#define ALL(c) c.begin(), c.end()
#define F first
#define S second
#define PB push_back
typedef long long ll;
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    int t, sm, standing, friends;
    string shy;
    cin>>t;
    loop(i, 1, t+1)
    {
        cout<<"Case #"<<i<<": ";
        cin>>sm;
        cin>>shy;
        standing = friends = 0;
        loop(j, 0, sm+1)
        {
            if(standing<j)
            {
                friends += j-standing;
                standing = j;
            }
            standing += shy[j]-48;
        }
        cout<<friends<<"\n";
    }
    
    return 0;
}
