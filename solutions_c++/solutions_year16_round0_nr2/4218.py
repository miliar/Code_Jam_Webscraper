/*
 Created by Saidolda Bayan.
 Copyright (c) 2015 Bayan. All rights reserved.
 LANG: C++
 */
#include <bits/stdc++.h>

#define _USE_MATH_DEFINES
#define y1 lalka
#define right napravo
#define left nalevo
#define pb push_back
#define mp make_pair
#define f first
#define s second

using namespace std;
using pii = pair<int, int>;
using ll = long long;

const int INF = (int)1e9+7, mod = (int)1e9+9, pw = 31, N = (int)1e5+123, M = (int)1e6+123;
const double eps = 1e-11;
const long long inf = 1e18;

int test;
string s;

int main ()
{
    ios_base::sync_with_stdio(0);cin.tie(NULL);
    freopen("B-large.in.txt","r",stdin);
    freopen("ans.txt","w",stdout);
    cin>>test;
    for(int c=1; c<=test; c++){
        cin>>s;
        cout<<"Case #"<<c<<": ";
        int ans = 0;
        for(int i=1; i<s.size(); i++){
            if(s[i] != s[i-1]){
                ans ++;
            }
        }
        ans += (*s.rbegin() == '-');
        cout<<ans<<"\n";
    }
    
    
    
    
    return 0;
}
